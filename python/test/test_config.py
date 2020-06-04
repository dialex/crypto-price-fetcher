import unittest
from helpers.config import read_file


class TestHelpers(unittest.TestCase):

    def test_read_file_should_output_lines(self):
        config_path = "config.txt"
        output = read_file(config_path)
        self.assertGreater(len(output), 0)


if __name__ == '__main__':
    unittest.main()
