import unittest

class TddPython(unittest.TestCase):

def test_calc_subtract_method(self):
    calc = Calculator()
    result = calc.subtract(4,1)
    self.assertEqual(3, result)
if __name__ == '__main__':
   unittest.main()
