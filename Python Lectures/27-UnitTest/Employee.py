import requests

class Employee:

	def __init__(self,firstname,lastname,salary):
		self._firstname = firstname
		self._lastname = lastname
		self._salary = salary

	@property
	def firstname(self):
		return self._firstname
	@firstname.setter
	def firstname(self,name):
		self._firstname = name

	@property
	def lastname(self):
		return self._lastname
	@lastname.setter
	def lastname(self,name):
		self._lastname = name

	@property
	def fullname(self):
		return f'{self._firstname} {self._lastname}'

	@property
	def emailid(self):
		return f'{self._firstname}.{self._lastname}@test.com'

	@property
	def salary(self):
		return self._salary
	@salary.setter
	def salary(self,value):
		self._salary = value

	def savings(self,expense):
		if expense > self._salary:
			raise ValueError('Expense cannot be greater than Salary')
		return self._salary - expense
	
	def monthly_schedule(self, month):
		response = requests.get(f'http://company.com/{self._lastname}/{month}')
		if response.ok:
			return response.text
		else:
			return 'Bad Response'