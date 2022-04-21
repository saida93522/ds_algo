import unittest

from Data_Structures.Array import contains_duplicate as duplicate
from Data_Structures.Array import merge_sorted_array as merged_array
from Data_Structures.Array import rotate_array as rotate_array


class TestArrays(unittest.TestCase):
    def test_if_it_contains_duplicates(self):
        #check returns True if duplicates
        dup = duplicate.check_for_duplicates4([1,1,2,4])
        self.assertTrue(dup)
        self.assertEqual(True,dup)
        
        #check returns False if no duplicates
        no_dup = duplicate.check_duplicate5([1,2,3])
        self.assertFalse(no_dup)
        self.assertEqual(True,dup)

    def test_sorted_merged_array(self):
        arr1 = [1,2,3,4,5]
        arr2 = [6,7,8,9,10]
        expected = merged_array.merge_arrays(arr1,arr2)
        actual = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(expected,actual)

    def test_array_rotated_right(self):
        arr = [10,11,12,13,14,15,16,17]
        n = 4
        expected = rotate_array.rotate_right(arr,n)
        self.assertEqual(expected, [14,15,16,17,10,11,12,13])

    def test_array_rotated_left(self):
        arr = [14,15,16,17,10,11,12,13]
        n = 4
        expected = rotate_array.rotate_left(arr,n)
        self.assertEqual(expected, [10,11,12,13,14,15,16,17])