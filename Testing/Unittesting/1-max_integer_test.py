#!/usr/bin/python3

"""Unittests for max_integer([..]).
To test the codes,we must create another Python file in the same directory and name it as the file only
ending it "_test.py".  or start it with "test_". """

import unittest # first the unittest module must be imported
max_integer = __import__('1-max_integer').max_integer #then import the exact function to be tested, or class
"""
this is used to import the module with the string name "1-max_integer", and then acceses the function
called max_integer in the module. IT IS NOT SAME HING AS "import 1-max_integer as mx". The later
imports all the module, and allows you to access a function like this : mx.max_integer().
The former can be done like this: from 1-max_integer import max_integer.
Remember a valid module name must not have "-".  """


class TestMaxInteger(unittest.TestCase): #creat a test class, that inherits from unittest.testcase which has multiple test asser methods.
    """Define unittests for max_integer([..])."""

    def test_module_docstring(self): #now begin writing different test method which must start with "test_". Tests to see if there are doctstring in the module
        """Tests for module docsting"""
        m = __import__('6-max_integer').__doc__ # this is how to call or print the modules docstring
        self.assertTrue(len(m) > 1) # uses the assert true to make ssure docstring has more than one letter.

    def test_function_docstring(self): # tests to see if there are docstrings in the function
        """Tests for funstion docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_non_int_arg(self): 
        """Tests for a non-int type in list of int"""
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError): # this tests to see if error would be raissed when string is made to be sorted along with ints
            max_integer(string)

    def test_ordered_list(self): # now begin writing different test method which must start with "test_"
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4) # asserts that first arguments(which is the action of your intended code to test) equals second argument 

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

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

"""
test file is always ended this way to run the imported unitest file first, only then does our test run.
The code line states that if this test file is sensed as main file(ie: if the file is run as a script, to run instantly),
then the code will execute the imported unittest module first, before running the test codes.
With out this , the test code wont just run on its own

THIS CAN ALSO BE Run ON the COMMAND LINE LIKE THIS : python3 -m unittest 1-max_integer_test.py .
This asks the  command line to go inside the 1-max_integer_test.py file, and run the unittest module 
as main(run it first) , before executing other codes.
"""