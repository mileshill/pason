class Battery:
    """
    Battery
    Acts as a resource for storing charge
    """

    def __init__(self, max_capacity, max_flux=None, current_charge_level=None):
        self.max_capacity = max_capacity
        self.max_flux = max_flux if not None else max_capacity

        # Default to charged
        self.current_level = current_charge_level if current_charge_level is not None else max_capacity

        # Track battery actions
        self.flux_history = [self.current_level]

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
        val =  max(self.current_level - value, 0)
        self.current_level = val
        self.flux_history.append(val)

    def __isub__(self, value):
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
        val = max(self.current_level - value, 0)
        self.current_level = val
        self.flux_history.append(val)
        return self

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
        val = min(self.current_level + value, self.max_capacity)
        self.current_level = val
        self.flux_history.append(val)

    def __iadd__(self, value):
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
        val = min(self.current_level + value, self.max_capacity)
        self.current_level = val
        self.flux_history.append(val)
        return self

    def __bool__(self):
        """
        True if current_level > 0 else false
        Returns
        -------

        """
        return True if self.current_level > 0 else False

    def drain(self):
        """
        Set self.current_level to 0

        Returns
        -------
        None
        """
        self.flux_history.append(-self.current_level)
        self.current_level = 0

    def charge(self):
        """
        Set self.current_level to self.max_capacity

        Returns
        -------
        None
        """
        self.flux_history.append(self.max_capacity - self.current_level)
        self.current_level = self.max_capacity
