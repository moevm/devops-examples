import unittest
from calculator import Calculator
#Test cases to test Calulator methods
#You always create  a child class derived from unittest.TestCase
class TestCalculator(unittest.TestCase):
  #setUp method is overridden from the parent class TestCase
  def setUp(self):
    self.calculator = Calculator()
  #Each test method starts with the keyword test_
  def test_add(self):
    self.assertEqual(self.calculator.add(4,7), 11, 'Substraction is working wrong')
  def test_subtract(self):
    self.assertEqual(self.calculator.subtract(10,5), 5, 'Substraction is working wrong')
  def test_multiply(self):
    self.assertEqual(self.calculator.multiply(3,7), 21, 'Multiplication is working wrong')
  def test_divide(self):
    self.assertEqual(self.calculator.divide(10,2), 5, 'Division is working wrong')
# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()
