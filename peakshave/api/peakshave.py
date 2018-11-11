import numpy as np
import pandas as pd
from peakshave.api.battery import Battery

def compute_daily_threshold(series, battery_max=120):
    """
    Computes daily threshold value be aggregating values above a selected threshold.
    Thresholds selection is executed in the following steps:
        1. Compute value of quantile
        2. If the sum of those values greater/equal is less than battery_max, decrement threshold
        3. Repeat until sum of values greater/equal is greater than battery_max

    Assumptions:
        1. Computed threshold is higher than true optimal. This is due to the characteristic morning
            energy spike
    Parameters
    ----------
    series: pd.Series of KWH
    battery_max

    Returns
    -------
    float of best daily threshold
    """
    values = series.values
    optimal = None
    thresholds = np.quantile(values, np.arange(0.99, 0.80, -0.001))  # Quantiles [0.99, 0.80)
    for threshold in thresholds:
        peak = values[np.where(values >= threshold)]
        if peak.sum() <= battery_max:
            optimal = threshold
            continue
        return optimal
    return None


def cache_optimal_value(series, cache=None):
    """
    Load a caches with precomputed optimal values

    Parameters
    ----------
    series pd.Series
    cache  redis.client.Redis

    Returns
    -------
    None
    """
    assert isinstance(cache, redis.client.Redis) or isinstance(cache, dict)
    *keys, kwh = series.values
    key = '-'.join(str(int(x)) for x in keys)

    if isinstance(cache, redis.client.Redis):
        cache.set(key, kwh)
    else:
        cache[key] = kwh


def daily_battery_strategy(daily_df):
    """

    Parameters
    ----------
    daily_df dataframe of single day

    Returns
    -------

    """
    assert isinstance(daily_df, pd.DataFrame)
    demand = daily_df.kwh
    timestamp = daily_df.timestamp
    threshold = compute_daily_threshold(demand)

    best = list()
    end_search = False
    while not end_search and threshold > 1:
        shaved_dmd = list()
        battery = Battery(max_capacity=120)

        for dmd in demand:
            discharge_battery = dmd > threshold
            charge_battery = (dmd < threshold) and (battery.current_level < battery.max_capacity)

            # Discharge
            if discharge_battery:
                # Levels
                delta = dmd - threshold

                # If battery is not empty
                if battery:
                    # Drain battery completely
                    if delta > battery.current_level:
                        shaved = dmd - battery.current_level
                        shaved_dmd.append(shaved)
                        battery.drain()

                    # Drain slightly
                    else:
                        shaved = threshold
                        shaved_dmd.append(shaved)
                        battery -= delta
                # Battery is empty
                else:
                    # batt.charge()
                    shaved_dmd.append(shaved)
                    end_search = True

            # Charge
            if charge_battery:
                # Battery not fully charged
                if battery.current_level < battery.max_capacity:
                    delta = threshold - dmd
                    avail_capacity = battery.max_capacity - battery.current_level

                    # Only charge available capacity
                    if delta < avail_capacity:
                        battery += delta * .1  # slow down battery chargnng
                        shaved = dmd + (delta *.1)  # slow down battery charging

                    # Full charge
                    if delta > avail_capacity:
                        battery.charge()
                        shaved = threshold
                    shaved_dmd.append(shaved)

                # Battery fully charged
                else:
                    shaved_dmd.append(dmd)
                    battery += 0

            # Standby
            if not charge_battery and not discharge_battery:
                battery += 0  # standby operation
                shaved_dmd.append(dmd)
        best.append(shaved_dmd)
        threshold *= .98

    df = daily_df.copy()
    df['shaved'] = best[-2]
    return df
