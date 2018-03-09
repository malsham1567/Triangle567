# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
@author: jrr
@author: rk
"""

import unittest

from Triangle import classify_triangle


class TestTriangles(unittest.TestCase):
    """ k """

    # define multiple sets of tests as functions with names that begin

    def test_right_triangle_a(self):
        """ m """
        self.assertEqual(classify_triangle(3, 4, 5), 'Right Scalene Triangle',
                         '3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(2, 2, 2), "Equilateral Triangle",
                         '2,2,2 is a Equilateral triangle')
        self.assertEqual(classify_triangle(4, 4, 4), "Equilateral Triangle",
                         '4,4,4 is a Equilateral triangle')
        self.assertEqual(classify_triangle(4, 3, 4), "Isosceles Triangle",
                         '4,3,4 is not a Isosceles triangle')
        self.assertEqual(classify_triangle(2, 3, 4), "Scalene Triangle",
                         '2,3,4 is a Scalene triangle')
        self.assertEqual(classify_triangle(3, 4, 6), "Scalene Triangle",
                         '3,4,6 is a Scalene triangle')
        self.assertEqual(classify_triangle(5, 3, 4), 'Right Scalene Triangle',
                         '5,3,4 is a Right triangle')
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral Triangle',
                         '1,1,1 should be equilateral')
        self.assertEqual(classify_triangle(7, 24, 25), 'Right Scalene Triangle',
                         '7,24,25 is a Right triangle')
        self.assertEqual(classify_triangle(5, 12, 13), 'Right Scalene Triangle',
                         '5,3,4 is a Right triangle')
        self.assertEqual(classify_triangle(7, 7, 4), "Isosceles Triangle",
                         '4,3,4 is an Isosceles triangle')
        self.assertEqual(classify_triangle(2, 2, 2.8), "Right Isosceles Triangle",
                         '2,2,2.8 is an Right Isosceles Triangle')

    def test_right_triangle_b(self):
        """" m """
        self.assertNotEqual(classify_triangle(222, 222, 222),
                            'Equilateral Triangle', '222,222,222 is invalid')
        self.assertEqual(classify_triangle('A', 'B', 'C'), 'InvalidInput', 'A,B,C is invalid input')
        self.assertEqual(classify_triangle(-4, 3, 9), 'InvalidInput',
                         '-4,3,9 is invalid input')
        self.assertEqual(classify_triangle(2, '/', 'M'), 'InvalidInput', '2,/,M is invalid input')
        self.assertEqual(classify_triangle(0, 10, 101), 'InvalidInput', '0,10,101 is invalid input')
        self.assertEqual(classify_triangle(33, 110, 469),
                         'InvalidInput', '33,110,469 is invalid input')
        self.assertEqual(classify_triangle(2, 0, 2), "InvalidInput", '2,0,2 is invalid input')

    def test_right_triangle_c(self):
        """ nnn """
        self.assertEqual(classify_triangle(1, 2, 3), "NotATriangle", '1,2,3 is NotATriangle')
        self.assertEqual(classify_triangle(1, 1, 5), "NotATriangle", '1,1,5 is NotATriangle')
        self.assertEqual(classify_triangle(10, 1, 5), "NotATriangle", '10,1,5 is NotATriangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
