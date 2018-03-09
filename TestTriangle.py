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
        
    def testInvalidInput(self): 
        self.assertEqual(classifyTriangle(0,1,1),'InvalidInput','0,1,1 should be InvalidInput')
        self.assertNotEqual(classifyTriangle("$",1,1),'NotATriangle','"$",1,1 should be InvalidInput')
        self.assertEqual(classifyTriangle("A",1,1),'InvalidInput','"A",1,1 should be InvalidInput')
        self.assertNotEqual(classifyTriangle(201,100,140),'Scalene','201,100,140 should be InvalidInput')
        self.assertEqual(classifyTriangle(-1,100,140),'InvalidInput','-1,100,140 should be InvalidInput')  
        
    def testEqualInput(self):      
        self.assertEqual(classifyTriangle(4,8,15),'NotATriangle','4,8,5 should be NotATriangle')        
        self.assertEqual(classifyTriangle(7,7,7),'Equilateral','7,7,7 should be Equilateral')       
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 should be Right')
        self.assertEqual(classifyTriangle(9,40,41),'Right','9,40,41 should be Right')        
        self.assertEqual(classifyTriangle(5,6,7),'Scalene','5,6,7 should be Scalene')
        self.assertEqual(classifyTriangle(10,20,25),'Scalene','10,20,25 should be Scalene')        
        self.assertEqual(classifyTriangle(3,7,7),'Isosceles','3,7,7 should be Isosceles')

        
    def testNotEqualInput(self): 
        self.assertNotEqual(classifyTriangle(1,2,3),'Isosceles','1,2,3 should be NotATriangle')
        self.assertNotEqual(classifyTriangle(5,3,3),'Right','5,3,3 should be Isosceles')
        self.assertNotEqual(classifyTriangle(8,15,17),'Equilateral','8,15,17 should be Right')
        self.assertNotEqual(classifyTriangle(1,1,1),'NotATriangle','1,1,1 should be Equilateral')
         

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
