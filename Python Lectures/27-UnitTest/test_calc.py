import unittest
import mathOperations as py

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(py.add(10,5),15)
        self.assertEqual(py.add(1,-1),0)
        self.assertEqual(py.add(-12,-5),-17)
    def test_sub(self):
        self.assertEqual(py.sub(10,5),5)
        self.assertEqual(py.sub(1,-1),2)
        self.assertEqual(py.sub(-12,-5),-7)
    def test_mul(self):
        self.assertEqual(py.mul(10,5),50)
        self.assertEqual(py.mul(1,-1),-1)
        self.assertEqual(py.mul(-12,-5),60)
    def test_div(self):
        self.assertEqual(py.div(10,5),2)
        self.assertEqual(py.div(1,-1),-1)
        self.assertEqual(py.div(-10,-5),2)

        self.assertRaises(ValueError, py.div, 10,0) # We write function name and arguments differently
        											# because otherwise our test will run that function 
        											# and it will get failed 

        with self.assertRaises(ValueError): # Other way to test exceptions
        	py.div(10,0)

# Run unittest code - 
        # python -m unittest test_calc.py


if __name__ == '__main__':
	unittest.main()




