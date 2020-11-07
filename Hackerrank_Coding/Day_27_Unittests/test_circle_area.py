# Write unit test

import unittest
from math import pi
from circles import circle_area

# Create a class that is a subclass of the test case class of the unittest module 

class TestCircleArea(unittest.TestCase):
	
	def test_area(self):
	# Test areas when radius >= 0
		self.assertAlmostEqual(circle_area(1), pi)
		self.assertAlmostEqual(circle_area(0), 0)
		self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

	def test_values(self):
	# Make sure value errors are raised when necessary
		self.assertRaises(ValueError, circle_area, -2)

	def test_types(self):
	
		self.assertRaises(TypeError, circle_area, 3+5j)
		self.assertRaises(TypeError, circle_area, True)
		self.assertRaises(TypeError, circle_area, 'radius')


	


