import unittest
from helpers.config import *


class TestHelpers(unittest.TestCase):

    def test_read_target_coins_should_output_lines(self):
        config_filepath = "config.txt"
        output = read_target_coins(config_filepath)
        self.assertGreater(len(output), 0)


if __name__ == '__main__':
    unittest.main()
