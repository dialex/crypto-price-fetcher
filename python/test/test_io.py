import unittest
import os
from helpers.io import *

test_output_dir = "test/output"


class TestHelperIO(unittest.TestCase):

    if not os.path.exists(test_output_dir):
        os.makedirs(test_output_dir)

    def test_read_file_should_return_lines(self):
        file_path = "test/fixtures/config.txt"
        lines_read = read_file(file_path)
        self.assertGreater(len(lines_read), 0)

    def test_read_file_should_return_empty_if_not_exists(self):
        file_path = "some-file-that-doesnt-exist.txt"
        lines_read = read_file(file_path)
        self.assertEqual(len(lines_read), 0)

    def test_write_list_file_should_write_one_line_per_element(self):
        file_path = f"{test_output_dir}/write_list_file.txt"
        elements = ["A", "B", "C"]
        write_list_file(file_path, elements)

        lines_written = read_file(file_path)
        self.assertEqual(len(elements), len(lines_written))

    def test_write_list_file_should_write_empty_file_given_empty_list(self):
        file_path = f"{test_output_dir}/write_list_file_empty.txt"
        elements = []
        write_list_file(file_path, elements)

        lines_written = read_file(file_path)
        self.assertEqual(0, len(lines_written))


if __name__ == '__main__':
    unittest.main()
