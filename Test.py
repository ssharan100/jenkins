#! /usr/bin/python3
# Test code for adding two numbers

import unittest

from Prog1 import summation

class TestSum(unittest.TestCase):
  def test_list_int(self):
    """
    Test case for adding two numbers
    """
    data = [21, 51]
    result = summation(data)
    self.assertEqual(result, 72)
      
if __name__ == "__main__":
  unittest.main()
