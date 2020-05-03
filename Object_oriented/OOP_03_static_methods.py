class Employee:

	# olyan mezo, amit nem akarunk felulirni
	# objektum peldannyal, mennyi dolgozo van
	nums_of_emps = 0
	raise_amount = 1.04

	# consturctor
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first +'.' + last + '@company.com'

		Employee.nums_of_emps += 1
		# Employee -> self helyett, csak ez az osztaly 
		# tudja elerni es valtoztatni

	def fullname(self):
		return '{} {}'.format(self.last,self.first)

	def apply_raise(self):
		# self.pay = int(self.pay * Employee.raise_amount) 
		self.pay = int(self.pay * self.raise_amount) 
		# self-fel az objektum peldany felulirhatja a fizu emelest
		# sot masik osztaly is megteheti ezt
		# emp_1.raise_amount = 1.06 peldaul

	# alterelja a metodusunk funkciojat, a dekorator
	# class elso argumentum -> instance helyett
	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amount = amount
	
	# alternativ konstruktor
	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True
	# staticmethod -> nak kene lennie, ha nem hasznalja az instance-t
	# vagy a class-t a funkcioban

emp_1 = Employee('Erik', 'Dubrovszkij', 50000 )
emp_2 = Employee('Test', 'User', 2000)


import datetime
my_date = datetime.date(2044, 5, 1 )

print(my_date.weekday())
print(Employee.is_workday(my_date))