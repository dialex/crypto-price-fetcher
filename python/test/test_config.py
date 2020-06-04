import unittest
from helpers.config import read_file


class TestHelperConfig(unittest.TestCase):

    def test_read_file_should_output_lines(self):
        file_path = "config.txt"
        output = read_file(file_path)
        self.assertGreater(len(output), 0)

    def test_read_file_should_print_warning_and_return_empty_if_not_exists(self):
        file_path = "some-file-that-doesnt-exist.txt"
        output = read_file(file_path)
        self.assertEqual(len(output), 0)


if __name__ == '__main__':
    unittest.main()
