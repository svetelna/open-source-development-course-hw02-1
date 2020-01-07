#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ossdev

import unittest
from ossdev import Vector


class VectorTest(unittest.TestCase):
    """Simple vector tests"""

    def __init__(self, *args, **kwargs):
        super(VectorTest, self).__init__(*args, **kwargs)

    def test_add(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        c = a + b

        self.assertEqual(c.get(), [3, 3, 3, 3])

    def test_dot(self):
        a = Vector([1, 2])
        b = Vector([2, -1])
        self.assertEqual(a.dot(b), 0)

    def test_lenght(self):
        # Uncomment after passing
        # self.assertAlmostEqual(Vector([2, 4]).length(), 4.47213595499, 3)
        # self.assertAlmostEqual(Vector([2, 4, 5]).length(), 6.708203932499369, 3)
        return

    def test_set(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])
        a[1] = 5
        self.assertEqual(a.get(), [0, 5, 2, 3])
        b[3] = 5
        b[0] = 5
        self.assertEqual(b.get(), [5, 2, 1, 5])

    def test_reversed(self):
        a = Vector([0, 1, 2, 3])
        self.assertEqual(reversed(a), [3,2,1,0])

    def test_sub(self):
        a = Vector([ 2, 2, 2])
        b = Vector([1,1,1])
        self.assertEqual(a-b, [1,1,1])

    def test_mul(self):
        a = Vector([ 2, 2, 2])
        b = 3
        self.assertEqual(a*b, [6,6,6])

    def test_neg(self):
        a = Vector([1, 2])
        b = Vector([-1,-2])
        self.assertListEqual(list(-b), list(a))

    def test_and(self):
        a = Vector([1, 2])
        b = Vector([1, 2])
        self.assertListEqual(list(a&b), list(a))

    def test_xor(self):
        a = Vector([ 2, 2, 2])
        b = 1
        self.assertEqual(a^b, [3,3,3])

    def test_trans(self):
        a = Vector([1, 2])
        self.assertListEqual(list(a), list(a))

    def test_len(self):
        a = Vector([ 2, 2, 2])
        self.assertEqual(a.length(), 3.4641016151377544)

    def test_dot(self):
        a = Vector([1, 2])
        b = Vector([2, -1])
        self.assertEqual(a.dot(b), 0)

    def test_lenght(self):
        # Uncomment after passing
        self.assertAlmostEqual(Vector([2, 4]).length(), 4.47213595499, 3)
        self.assertAlmostEqual(Vector([2, 4, 5]).length(), 6.708203932499369, 3)
        return


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
