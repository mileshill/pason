class Battery:
    """
    Battery
    Acts as a resource for storing charge
    """

    def __init__(self, max_capacity, max_flux, current_charge_level=None):
        self.max_capacity = max_capacity
        self.max_flux = max_flux

        # Default to charged
        self.current_level = current_charge_level if current_charge_level is not None else max_capacity

    def __sub__(self, value):
        """
        Subtract charge without accessing properties
        Prevents subtraction past 0

        Parameters
        ----------
        value - value to subtract

        Returns
        -------
        None
        """
        self.current_level = max(self.current_level - value, 0)

    def __add__(self, value):
        """
        Add charge without accessing properties
        Prevents addition past self.max_capacity

        Parameters
        ----------
        value - value to add

        Returns
        -------
        None
        """
        self.current_level = min(self.current_level + value, self.max_capacity)

    def drain(self):
        """
        Set self.current_level to 0

        Returns
        -------
        None
        """
        self.current_level = 0

    def charge(self):
        """
        Set self.current_level to self.max_capacity

        Returns
        -------
        None
        """
        self.current_level = self.max_capacity
