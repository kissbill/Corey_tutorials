class Employee:

	raise_amount = 1.04

	# consturctor
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first +'.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.last,self.first)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount) 

class Developer(Employee):
	raise_amount = 1.10

	def __init__(self, first, last, pay, prog_lang ):
		super().__init__(first, last, pay)
		# Employee.__init__(self, first, last, pay)
		# igy is lehet az os konsturktort meghivni
		self.prog_lang = prog_lang


class Manager(Employee):
	"""docstring for Manager"""
	def __init__(self, first, last, pay, employees=None ):
		# ezzel inicializalta a sublime osztaly krealaskor
		# super(Manager, self).__init__() 
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees: 
			self.employees.append(emp)

	def remove_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		if not self.employees:
			print('There is none empleyee')
		else:
			for emp in self.employees:
				print('--> ', emp.fullname())
			
				

dev_1 = Developer('Erik', 'Dubrovszkij', 50000 , 'Python')
dev_2 = Developer('Test', 'User', 2000, 'Java')


mgr_1 = Manager('Sue', 'Smith', 900, [dev_1])

# print(mgr_1.email)
# mgr_1.print_emps()

# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# print(dev_1.__dict__)

# kiir minden informaciot az osztalyrol
# print(help(Developer))

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# megmondja, h egy peldany, adott osztaly peldanya-e
print(isinstance(mgr_1,Manager))
print(isinstance(mgr_1,Developer))
print(isinstance(mgr_1,Employee))

print( 'is it subclass ? --> ' + str(issubclass(Developer,Manager)))
print( 'is it subclass ? --> ' + str(issubclass(Developer,Employee)))