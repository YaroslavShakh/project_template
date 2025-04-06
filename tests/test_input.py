import unittest
import os
import pandas as pd
from app.io.input  import read_file_builtin, read_file_pandas

class TestReadFileFunctions(unittest.TestCase):

    def setUp(self):
        # Create a test text file
        self.text_file_path = 'test_file.txt'
        self.test_text_content = "Hello, this is a test file.\nSecond line."
        with open(self.text_file_path, 'w', encoding='utf-8') as f:
            f.write(self.test_text_content)

        # Create a test CSV file
        self.csv_file_path = 'test_file.csv'
        self.test_csv_data = {
            'Name': ['Alice', 'Bob'],
            'Age': [25, 30]
        }
        pd.DataFrame(self.test_csv_data).to_csv(self.csv_file_path, index=False)

    def tearDown(self):
        # Remove test files after tests run
        os.remove(self.text_file_path)
        os.remove(self.csv_file_path)

    # -------- Tests for read_file_builtin --------
    def test_read_file_builtin_correct_content(self):
        content = read_file_builtin(self.text_file_path)
        self.assertEqual(content, self.test_text_content)

    def test_read_file_builtin_empty_file(self):
        empty_path = 'empty.txt'
        with open(empty_path, 'w', encoding='utf-8') as f:
            pass
        self.assertEqual(read_file_builtin(empty_path), '')
        os.remove(empty_path)

    def test_read_file_builtin_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_file_builtin('non_existent_file.txt')

    # -------- Tests for read_file_pandas --------
    def test_read_file_pandas_content(self):
        expected_output = "Name  Age\nAlice   25\n  Bob   30"
        output = read_file_pandas(self.csv_file_path)
        self.assertEqual(output.strip(), expected_output)

    def test_read_file_pandas_empty_file(self):
        empty_csv = 'empty.csv'
        with open(empty_csv, 'w', encoding='utf-8') as f:
            f.write('')
        with self.assertRaises(pd.errors.EmptyDataError):
            read_file_pandas(empty_csv)
        os.remove(empty_csv)

    def test_read_file_pandas_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_file_pandas('non_existent.csv')


if __name__ == '__main__':
    unittest.main()