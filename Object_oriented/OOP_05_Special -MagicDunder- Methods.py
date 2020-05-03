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

	def __repr__(self):
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay )

	def __str__(self):
		return '{} - {}'.format(self.fullname(), self.email)

	def __add__(self,other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.fullname())

emp_1 = Employee('Erik', 'Dubrovszkij', 50000 )
emp_2 = Employee('Test', 'User', 2000 )


print(str(emp_1))
# print(repr(emp_1))

# ez egy beepitet py fgv-t hiv meg
print(1+2)
# same -> 
print(int.__add__(1,2))

print(str.__add__('a','ccc'))

# Same
print(Employee.__add__(emp_1,emp_2))
print((emp_1 + emp_2))

# Alap fgv , ez at irva
print(len('test'))
print('test'.__len__())
# atirva az emp full nevenek a hosszat adja meg:
print(len(emp_2))