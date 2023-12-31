import unittest
'''
Unit tests for max integer function
'''

max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    '''
    Test class for max_integer function
    '''
    def test_max_integer(self):
        '''
        Tests output of regular function output
        '''
        self.assertAlmostEqual(max_integer([1, 3, 4, 5, 6, 7]), 7)

    def test_empty_list(self):
        '''Tests an empty list
        '''
        self.assertAlmostEqual(max_integer([]), None)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_double_occurence(self):
        '''Tests two occurences of the max int
        '''
        self.assertAlmostEqual(max_integer([1, 2 , 3, 4, 4]), 4)

    def test_errors(self):
        '''Tests for error cases in the function
        '''
        self.assertRaises(TypeError, max_integer, 2)


    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()