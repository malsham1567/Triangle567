# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple python program to classify triangles
@author: jrr
@author: rk
"""


def classify_triangle(aaa, bbb, ccc):
    try:
        if aaa > 200 or bbb > 200 or ccc > 200:
            return 'InvalidInput'

        if aaa <= 0 or bbb <= 0 or ccc <= 0:
            return 'InvalidInput'

        if (aaa >= (bbb + ccc)) or (bbb >= (aaa + ccc)) or (ccc >= (aaa + bbb)):
            return 'NotATriangle'

    except TypeError:
        return "InvalidInput"

    if round((aaa * aaa) + (bbb * bbb)) == round(ccc * ccc) or \
            round((bbb * bbb) + (ccc * ccc)) == round(aaa * aaa) or \
            round((aaa * aaa) + (ccc * ccc)) == round(bbb * bbb):
        if (aaa != bbb) and (bbb != ccc) and (aaa != ccc):
            return 'Right Scalene Triangle'
        else:
            return 'Right Isosceles Triangle'
    else:
        if (aaa != bbb) and (bbb != ccc) and (aaa != ccc):
            return 'Scalene Triangle'
        elif aaa == bbb and bbb == ccc:
            return 'Equilateral Triangle'
        else:
            return 'Isosceles Triangle'

