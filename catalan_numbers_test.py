import unittest
from catalan_numbers import get_catalan_value


class TestCatalanNumbers(unittest.TestCase):

    def test_function_validation(self):
        catalan_seq = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900]
        for i in range(0, len(catalan_seq)):
            self.assertEqual(get_catalan_value(i), catalan_seq[i])

    def test_non_positive(self):
        self.assertRaises(ValueError, get_catalan_value, -1)
        self.assertRaises(ValueError, get_catalan_value, -2)
        self.assertRaises(ValueError, get_catalan_value, -3)

    def test_value_type(self):
        self.assertRaises(TypeError, get_catalan_value, 'test')
        self.assertRaises(TypeError, get_catalan_value, [1, 2, 3])
        self.assertRaises(TypeError, get_catalan_value, True)