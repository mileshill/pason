import unittest

from peakshave.api.battery import Battery


class TestBattery(unittest.TestCase):
    def setUp(self):
        max_capacity = 10
        max_flux = 10
        self.battery = Battery(max_capacity, max_flux)

    def test_drain(self):
        """
        Full drain on battery
        """
        self.battery.drain()
        self.assertEqual(self.battery.current_level, 0)

    def test_charge(self):
        """
        Full charge on battery
        """
        self.battery.drain()
        self.battery.charge()
        self.assertEqual(self.battery.current_level, self.battery.max_capacity)

    def test_single_decrement(self):
        """
        Single discharge
        :return:
        """
        self.battery - 5
        self.assertEqual(self.battery.current_level, 5)

    def test_isub_decrement(self):
        """
        Single discharge
        Returns
        -------
        """
        self.battery -= 5
        self.assertEqual(self.battery.current_level, 5)

    def test_decrement_to_min_level(self):
        """
        No decrements past 0
        """
        self.battery - 15
        self.assertEqual(self.battery.current_level, 0)

    def test_single_increment(self):
        """
        Full drain then partial charge
        """
        self.battery.drain()
        self.battery + 5
        self.assertEqual(self.battery.current_level, 5)

    def test_increment_to_max_level(self):
        """
        No charge past max_capacity
        """
        self.battery + 5
        self.assertEqual(self.battery.current_level, self.battery.max_capacity)

    def test_initial_charge_level(self):
        """
        Not max charge at creation
        """
        initial_charge_level = 5
        battery = Battery(max_capacity=10, max_flux=10, current_charge_level=initial_charge_level)
        self.assertEqual(battery.current_level,initial_charge_level)

    def test_bool_true(self):
        self.assertTrue(self.battery)

    def test_bool_false(self):
        self.assertFalse((self.battery.drain()))

    def test_flux_history(self):
        self.battery.drain()
        self.battery.charge()
        self.battery -= 1
        self.battery += 1
        self.assertEqual(len(self.battery.flux_history), 5)

if __name__ == '__main__':
    unittest.main()
