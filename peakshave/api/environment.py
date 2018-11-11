import os

import numpy as np
from peakshave.api.battery import Battery


class Environment:
    """
    Simulation environment
    """

    def __init__(self, battery, demand):
        assert isinstance(battery, Battery)
        assert isinstance(demand, np.ndarray)
        self.battery = battery
        self.demand = demand


    def simple_simulation(self, battery, path_to_demand):
        assert os.path.exists(path_to_demand)
        assert os.path.isfile(path_to_demand)
        d



if __name__ == '__main__':
    # Create an environment
    battery = Battery(10, 10)
    env = Environment(battery)
