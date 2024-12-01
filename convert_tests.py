# convert_tests.py

import unittest
import convert


class TestStrToFloat(unittest.TestCase):

#Part 1 - test str_to_float
    def test_str_to_float_1(self):
        input = "123.2"
        expected = 123.2
        result = convert.str_to_float(input)
        self.assertEqual(expected, result)

    def test_str_to_float_2(self):
        input = "Hello"
        expected = None
        result = convert.str_to_float(input)
        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()

