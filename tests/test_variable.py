import sys
import os
import unittest
from unittest.mock import patch
from io import StringIO

# Add src directory to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.variable import (
    get_integer, get_string, get_name, get_details, print_variable_types,
    print_boolean_values, print_combined_details, print_datetime, print_final_details, print_all
)

class TestVariables(unittest.TestCase):
    
    def setUp(self):
        # This method is called before each test method for initialization now for illustration purposes
        self.value = 42

    def tearDown(self):
        # This method is called after each test method for clean up now for illustration purposes
        pass

    def test_example(self):
        # A test method for example now for illustration purposes
        self.assertEqual(self.value, 42)

    def test_another_example(self):
        # Another test method for example now for illustration purposes
        self.assertTrue(isinstance(self.value, int))


    def test_get_integer(self):
        self.assertEqual(get_integer(), 25)

    def test_get_string(self):
        self.assertEqual(get_string(), "twenty five")

    def test_get_name(self):
        self.assertEqual(get_name(), "Ahmet Ahmetoglu")

    def test_get_details(self):
        self.assertEqual(get_details(), "25 72.5 True")

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_variable_types(self, mock_stdout):
        print_variable_types()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertEqual(output[0], "<class 'int'>")
        self.assertEqual(output[1], "<class 'str'>")
        self.assertEqual(output[2], "<class 'str'>")
        self.assertEqual(output[3], "<class 'bool'>")

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_boolean_values(self, mock_stdout):
        print_boolean_values()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertEqual(output[0], "True")
        self.assertEqual(output[1], "True")
        self.assertEqual(output[2], "True")
        self.assertEqual(output[3], "True")

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_combined_details(self, mock_stdout):
        print_combined_details()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertEqual(output[0], "26 72.5 False")

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_datetime(self, mock_stdout):
        print_datetime()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertEqual(output[0], "2021-09-01 12:00:00")

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_final_details(self, mock_stdout):
        print_final_details()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertEqual(output[0], "Ahmet - Ahmetoglu - 25 - 74.5 - True")

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_all(self, mock_stdout):
        print_all()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertEqual(output[0], "25")
        self.assertEqual(output[1], "<class 'int'>")
        self.assertEqual(output[2], "twenty five")
        self.assertEqual(output[3], "Ahmet Ahmetoglu")
        self.assertEqual(output[4], "25 72.5 True")
        self.assertEqual(output[5], "<class 'int'>")
        self.assertEqual(output[6], "<class 'str'>")
        self.assertEqual(output[7], "<class 'str'>")
        self.assertEqual(output[8], "<class 'bool'>")
        self.assertEqual(output[9], "True")
        self.assertEqual(output[10], "True")
        self.assertEqual(output[11], "True")
        self.assertEqual(output[12], "True")
        self.assertEqual(output[13], "26 72.5 False")
        self.assertEqual(output[14], "2021-09-01 12:00:00")
        self.assertEqual(output[15], "<class 'str'>")
        self.assertEqual(output[16], "True")
        self.assertEqual(output[17], "Ahmet - Ahmetoglu - 25 - 74.5 - True")

if __name__ == '__main__':
    unittest.main()