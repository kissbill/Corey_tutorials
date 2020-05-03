class Employee:

	raise_amount = 1.04

	# consturctor
	def __init__(self, first, last ):
		self.first = first
		self.last = last

	@property
	def fullname(self):
		return '{} {}'.format(self.last,self.first)

	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		print('Delete name')
		self.first = None
		self.last = None

	@property
	def email(self):
		return '{}.{}@company.com'.format(self.last,self.first)



emp_1 = Employee('Erik','Kovacs')

emp_1.fullname = 'Erik Dubrovszkij'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname


