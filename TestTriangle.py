# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle( 2 , 2 , 2 ) , "Equilateral",'2,2,2 is a Equilateral triangle')
        self.assertEqual(classifyTriangle( 4 , 4 , 4 ) , "Equilateral",'4,4,4 is a Equilateral triangle')
        self.assertEqual(classifyTriangle( 4 , 3 , 4 ) , "Isoceles",'4,3,4 is not a Isosceles triangle')
        self.assertEqual(classifyTriangle( 2 , 3 , 4 ), "Scalene",'2,3,4 is a Scalene triangle')
        self.assertEqual(classifyTriangle(3, 4, 6), "Scalene",'3,4,6 is a Scalene triangle')
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(7,24,25),'Right','7,24,25 is a Right triangle')
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,3,4 is a Right triangle')
        self.assertEqual(classifyTriangle( 7 , 7 , 4 ),"Isoceles",'4,3,4 is a Isosceles triangle')





    def testRightTriangleB(self): 
        self.assertNotEqual(classifyTriangle(222, 222, 222), 'Equilateral', '222,222,222 is invalid')
        self.assertEqual(classifyTriangle('A', 'B', 'C'), 'InvalidInput', 'A,B,C is invalid input')
        self.assertEqual(classifyTriangle(-4, 3, 9), 'InvalidInput', '-4,3,9 is invalid input')
        self.assertEqual(classifyTriangle(2, '/', 'M'), 'InvalidInput', '2,/,M is invalid input')
        self.assertEqual(classifyTriangle(0, 10, 101), 'InvalidInput', '0,10,101 is invalid input')
        self.assertEqual(classifyTriangle(33, 110, 469), 'InvalidInput', '33,110,469 is invalid input')
        self.assertEqual(classifyTriangle(2, 0, 2), "InvalidInput", '2,0,2 is invalid input')

        
    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle( 1 , 2 , 3 ) , "NotATriangle",'1,2,3 is NotATriangle')
        self.assertEqual(classifyTriangle( 1 , 1 , 5 ) , "NotATriangle",'1,1,5 is NotATriangle')
        self.assertEqual(classifyTriangle( 10 , 1 , 5 ) , "NotATriangle",'10,1,5 is NotATriangle')




if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

