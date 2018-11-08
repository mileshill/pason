from peakshave.api.battery import Battery


class Environment:
    """
    Simulation environment
    """

    def __init__(self, battery):
        assert isinstance(battery, Battery)
        self.battery = battery

if __name__ == '__main__':
    # Create an environment
    battery = Battery(10, 10)
    env = Environment(battery)