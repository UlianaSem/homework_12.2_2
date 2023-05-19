import unittest
from utils import arrs

class TestArrs(unittest.TestCase):
    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([1, 2, 3], -3, 'test'), "test")
        with self.assertRaises(IndexError):
            arrs.get([], 0, "test")

    def test_slice(self):
        self.assertEquals(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEquals(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEquals(arrs.my_slice([]), [])
        self.assertEquals(arrs.my_slice([0, 1], -4), [0, 1])
        self.assertEquals(arrs.my_slice([1, 2, 3], -2, 2), [2])
