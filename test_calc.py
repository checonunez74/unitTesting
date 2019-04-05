import unittest
import calculator

class TestCalc(unittest.TestCase):

	def test_add(self):
		
		self.assertEqual(calculator.add(10, 5), 15)
		self.assertEqual(calculator.add(-1, 1), 0)
		self.assertEqual(calculator.add(-1, -1), -2)
		


if __name__ == '__main__':
	unittest.main()