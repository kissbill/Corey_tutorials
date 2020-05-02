class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first +'.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.last,self.first)

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

print(Employee.fullname(emp_1))