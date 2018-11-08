from unittest import TestCase

from peakshave.api.battery import Battery
from peakshave.api.environment import Environment


class TestEnvironment(TestCase):
    def setUp(self):
        self.battery = Battery(10, 10)

    def test_environment_creation_no_args(self):
        with self.assertRaises(TypeError):
            Environment()

    def test_environment_creation_not_battery(self):
        with self.assertRaises(AssertionError):
            Environment('not a battery')

    def test_environment_creation_valid(self):
        env = Environment(self.battery)
        self.assertIsInstance(env, Environment)