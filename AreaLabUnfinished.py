import math #math library has pre-written math functions
import unittest

def circleArea(radius): 
    """Return the area of a circle"""
    return math.pi * radius * radius 

def rectArea(base, height):
    """Return the area of a rectangle"""
    return base * height

def trapArea(base1, base2, height):
    """Return the area of a trapezoid"""
    return base1 + base2 /2 * height

def triArea(base,height):
    """Return the area of a triangle"""
    return base * height /2 
    
	
class MyTest(unittest.TestCase):
    def testCircleArea(self):
        self.assertEqual(CircleArea(5), 25*math.pi)
    def testRectArea(self):
        self.assertEqual(RectArea(2,3), 6)
    def testTrapArea(self):
        self.assertEqual(TrapArea(3,3,3), 9)
    def testTriArea(self):
        self.assertEqual(TriArea(3,3), 4.5)
    
    