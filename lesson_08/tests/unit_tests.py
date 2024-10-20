import unittest
from function_for_test import middle, sorted_by_len, num_of_even_numbers

class TestMiddleValue(unittest.TestCase):
    def test_middle_positive(self):
        actual_result = middle([1, 2, 3])
        expected_result = 2

        self.assertEqual(actual_result, expected_result)

    def test_middle_negative(self):
        actual_result = middle([1, 2, 3])
        expected_result = 0

        self.assertEqual(actual_result, expected_result)

    def test_middle_put_text_in_list(self):
        with self.assertRaises(TypeError):
            middle([1, "2", 3])

    def test_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            middle([])


input_list = ['qqqqqwert', 'ee', 'rrrr']
class TestSortedByLen(unittest.TestCase):

    def test_len_positive(self):
        actual_result = sorted_by_len(input_list)
        expected_result = 'qqqqqwert'
        self.assertEqual(actual_result, expected_result)
    def test_len_negative(self):
        actual_result = sorted_by_len(input_list)
        expected_result = 'ee'
        self.assertEqual(actual_result, expected_result)

    def test_same_len(self):
        self.assertEqual(sorted_by_len(['aaa', 'bbb', 'ccc']), 'ccc')

    def test_single_element(self):
        self.assertEqual(sorted_by_len(['one']), 'one')

    def test_empty_list(self):
        self.assertIsNone(sorted_by_len([]))

class TestNumOfEvenNumbers(unittest.TestCase):

    def test_even_numbers_positive(self):
        actual_result = num_of_even_numbers([1, 2, 3, 4])
        expected_result = 6
        self.assertEqual(actual_result, expected_result)

    def test_no_even(self):
        actual_result = num_of_even_numbers([1, 3, 5])
        expected_result = 0
        self.assertEqual(actual_result, expected_result)


    def test_empty_list(self):
        actual_result = num_of_even_numbers([])
        expected_result = 0
        self.assertEqual(actual_result, expected_result)

    def test_negative_even_numbers(self):
        actual_result = num_of_even_numbers([-2, -4, -6])
        expected_result = -12
        self.assertEqual(actual_result, expected_result)

    def test_zero_in_list(self):
        actual_result = num_of_even_numbers([0, 1, 2])
        expected_result = 2
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main()

