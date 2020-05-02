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

emp_1 = Employee('Erik', 'Dubrovszkij', 50000 )
emp_2 = Employee('Test', 'User', 2000)

# emp_1.first = 'Erik'
# emp_1.last = 'Dubrpvszlok'
# emp_1.email = 'erik@free.hu'
# emp_1.job = 6000

# emp_2.first = 'Test'
# emp_2.last = 'vszlok'
# emp_2.email = 'test@free.hu'
# emp_2.job = 444

# print(emp_1.fullname())

# nem tudjuk melyik peldany, ezert kell parameterben megadni az emp_1-et
print(Employee.fullname(emp_1))

# fizu emeles, utana 
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# ebben nincs benne a raise_amount
# print(emp_1.__dict__)

# benne van a raise_amount attribute
print(Employee.__dict__)

Employee.raise_amount = 1.05 

# sajat mezeje lett , namespace-en belul
emp_1.raise_amount = 1.06
print(emp_1.__dict__)

print(Employee.nums_of_emps)

# Instance variable -> emp_1
# Class variable -> Employee
