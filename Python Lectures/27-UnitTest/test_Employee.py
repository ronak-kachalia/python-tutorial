#%%
import unittest
from unittest.mock import patch
import Employee as emp

#%%
class TestEmployee(unittest.TestCase):

	# method names must always start with 'test_'

	def test_email(self):
		x = emp.Employee('Ronak','Kachalia',30000)
		y = emp.Employee('Vijay','Jha',40000)

		self.assertEqual(x.emailid,'Ronak.Kachalia@test.com')
		self.assertEqual(y.emailid,'Vijay.Jha@test.com')

	def test_savings(self):
		x = emp.Employee('Ronak','Kachalia',30000)
		y = emp.Employee('Vijay','Jha',40000)

		self.assertEqual(x.savings(10500),19500)
		self.assertEqual(y.savings(21456),18544)

		with self.assertRaises(ValueError):
			x.savings(40000)
			y.savings(43000)

#%%
class TestEmployee2(unittest.TestCase):

	# Runs once BEFORE any of the test cases runs
	@classmethod
	def setUpClass(cls):
		print('setUpClass')
	
	# Runs once AFTER all the test cases are executed 
	@classmethod
	def tearDownClass(cls):
		print('tearDownClass')

	# This will run before each test case
	def setUp(self):
		self.x = emp.Employee('Ronak','Kachalia',30000)
		self.y = emp.Employee('Vijay','Jha',40000)
	
	# This will will run after each test case
	def tearDown(self):
		print('tearDown')

	def test_email(self):
		self.assertEqual(self.x.emailid,'Ronak.Kachalia@test.com')
		self.assertEqual(self.y.emailid,'Vijay.Jha@test.com')

	def test_savings(self):
		self.assertEqual(self.x.savings(10500),19500)
		self.assertEqual(self.y.savings(21456),18544)

		with self.assertRaises(ValueError):
			self.x.savings(40000)
			self.y.savings(43000)
	
	def test_monthly_schedule(self):
		with patch('Employee.requests.get') as mocked_get:
			# For 'ok' response
			mocked_get.return_value.ok = True
			mocked_get.return_value.text = 'Success'

			schedule = self.x.monthly_schedule('May')
			mocked_get.assert_called_with('http://company.com/Kachalia/May') # To check URL
			self.assertEqual(schedule, 'Success')

			# For 'false' response
			mocked_get.return_value.ok = False

			schedule = self.y.monthly_schedule('June')
			mocked_get.assert_called_with('http://company.com/Jha/June') # To check URL
			self.assertEqual(schedule, 'Bad Response')

#%%
if __name__ == '__main__':
	unittest.main() 

