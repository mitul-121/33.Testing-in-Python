import unittest
from addition import add

class TestAddition(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(1,1),2)
    @unittest.skip("skip")
    def test_negative(self):
        self.assertEqual(add(-1,1),10)
    @unittest.expectedFailure
    def test_zero(self):
        self.assertEqual(add(0,0),10)
    def test_float(self):
        self.assertEqual(add(1.1,1.1),2.2)
    def test_int_flot(self):
        self.assertEqual(add(1,1.1),2.1)
    def test_addition_int_string(self):
        with self.assertRaises(TypeError):
            add(1,"1")

if __name__ == '__main__':
    unittest.main()