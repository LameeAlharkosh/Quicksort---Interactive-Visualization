import unittest
from algorithm import quicksort_with_steps

class TestQuicksort(unittest.TestCase):
    def test_sorted_array(self):
        array = [1, 2, 3, 4, 5]
        # Unpack to get the sorted array from the tuple
        sorted_arr, _, _ = quicksort_with_steps(array.copy(), strategy="First Element")
        self.assertEqual(sorted_arr, sorted(array))

    def test_reverse_array(self):
        array = [5, 4, 3, 2, 1]
        sorted_arr, _, _ = quicksort_with_steps(array.copy(), strategy="Last Element")
        self.assertEqual(sorted_arr, sorted(array))

    def test_random_array(self):
        array = [8, 2, 4, 7, 1, 3]
        sorted_arr, _, _ = quicksort_with_steps(array.copy(), strategy="Random")
        self.assertEqual(sorted_arr, sorted(array))

    def test_duplicate_elements(self):
        array = [5, 3, 8, 3, 9, 1, 3]
        sorted_arr, _, _ = quicksort_with_steps(array.copy(), strategy="Median Element")
        self.assertEqual(sorted_arr, sorted(array))

if __name__ == "__main__":
    unittest.main()

