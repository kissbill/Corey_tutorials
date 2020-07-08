# 1 ###############################################
# li = [2, 4, 5, 8, 1, 3, 6, 9]

# # sorted uj listat ad vissza
# # s_li = li.sort()
# s_li = sorted(li, reverse=True)

# print('Sorted variable: ', s_li)

# li.sort()
# print('unSorted variable: ', li)

# 2 ###############################################

# tup = (2, 4, 5, 8, 1, 3, 6, 9)
# s_tup = sorted(tup)
# print(s_tup)

# 3 ###############################################

# dict = {'name': 'Erik', 'hobby': ' reading', 'age': 'above'}
# s_dict = sorted(dict)
# print(s_dict)


# 4 ###############################################

# li = [-6, -4, -5, 1, 3, 2]
# s_li = sorted(li, key=abs)
# print(s_li)

# 5 ###############################################
# class Employee():
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def __repr__(self):
#         return '({},{},${})'.format(self.name, self.age, self.salary)


# e1 = Employee('Carl', 44, 3222)
# e2 = Employee('Fefe', 22, 2222)
# e3 = Employee('Eroi', 19, 1299)

# employee = [e1, e2, e3]


# def e_sort(emp):
#     return emp.name
#     # return emp.age
#     # return emp.salary


# s_emp = sorted(employee, key=e_sort)
# print(s_emp)
# 6 ###############################################
# class Employee():
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def __repr__(self):
#         return '({},{},${})'.format(self.name, self.age, self.salary)


# e1 = Employee('Carl', 44, 3222)
# e2 = Employee('Fefe', 22, 2222)
# e3 = Employee('Eroi', 19, 1299)

# employee = [e1, e2, e3]


# s_emp = sorted(employee, key=lambda e: e.age)
# print(s_emp)

# 7 ###############################################


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


from operator import attrgetter

e1 = Employee('Carl', 44, 3222)
e2 = Employee('Fefe', 22, 2222)
e3 = Employee('Eroi', 19, 1299)

employee = [e1, e2, e3]


s_emp = sorted(employee, key=attrgetter('age'))
print(s_emp)
