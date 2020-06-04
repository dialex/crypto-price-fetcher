import unittest
import helpers.config as config


class TestHelpers(unittest.TestCase):

    def test_read_file_should_output_lines(self):
        config_filepath = "config.txt"
        output = config.read_file(config_filepath)
        self.assertGreater(len(output), 0)


if __name__ == '__main__':
    unittest.main()
