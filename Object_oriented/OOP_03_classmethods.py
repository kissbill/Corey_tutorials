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


emp_1 = Employee('Erik', 'Dubrovszkij', 50000 )
emp_2 = Employee('Test', 'User', 2000)

# classmethod-ban allitjuk be -> self helyett az osztalyon dolgozunk
# Employee.set_raise_amt(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-700'
emp_str_2 = 'Steve-Smith-500'
emp_str_3 = 'Kiss-Mate-300'

# Manual meghajtassal:
# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)
# print(new_emp_1.email)

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.__dict__)