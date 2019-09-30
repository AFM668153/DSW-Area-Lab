import math #math library has pre-written math functions
import unittest

def circleArea(radius): 
    return 1

def rectArea(base, height):
    return 1

def trapArea(base1, base2, height):
    return 1

def triArea(base,height):
    return 1
    
	
class MyTest(unittest.TestCase):
    def testCircleArea(self):
        self.assertEqual(circleArea(5), 25*math.pi)
    #def testRectArea(self):
    
    #def testTrapArea(self):
    
    #def testTriArea(self):
    
    