 # Comprehensions - How they work and why you should be using them
 # https://youtu.be/3dt4OGnU5sM
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1. example ########################################
 # i want 'n' for each 'n' nums
# my_list = []

# for n in nums:
# 	my_list.append(n)
# print(my_list)

# 2. list Comprehensions ############################

# my_list = [n for n in nums]
# print(my_list)


# 3. example ########################################
 # i want 'n*n' for each 'n' nums

# my_list = []
# for n in nums:
# 	my_list.append(n*n)
# print(my_list)

# 4. example ########################################

# my_list = [n*n for n in nums]
# print(my_list)

# 5. example ########################################
# even # or not
# my_list=[]
# for n in nums:
# 	if n%2 == 0:
# 		my_list.append(n)
# print(my_list)

# 6. example ########################################

# my_list = [n for n in nums if n%2 == 0 ]
# print(my_list)

# my_list = filter(lambda n: n%2 == 0, nums)
# print my_list
# 6. example ########################################
# my_list= []

# for letter in 'abcd':
# 	for num in range(4):
# 		my_list.append((num,letter))
# print(my_list)

# my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
# print(my_list)

# 6. example ########################################
# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(list(zip(names,heros)))

# https://stackoverflow.com/questions/31683959/the-zip-function-in-python-3
# Unlike in Python 2, the zip function in Python 3 returns an iterator. 
# Iterators can only be exhausted 
# (by something like making a list out of them) once. 
# The purpose of this is to save memory by 
# only generating the elements of the iterator as you need them,
#  rather than putting it all into memory at once


# I want a dict{'nama':heros} for each name , hero in zip(names,heros)

# my_dict = {}
# for name, hero in zip(names,heros):
# 	my_dict[name]=hero
# print(my_dict)

# my_dict = {name : hero for name, hero in zip(names, heros) if name != 'Peter'}
# print(my_dict)
# 7. example ########################################
# nums = [0, 1,1,1, 2,2, 3, 4,4,4, 5, 6,6,6, 7, 8, 9]

# my_set = set()

# for n in nums:
# 	my_set.add(n)

# print(my_set)

# my_set = {n for n in nums}
# print(my_set)
# 8. example ########################################
nums1 = [0, 1,1,1, 2,2, 3, 4,4,4, 5, 6,6,6, 7, 8, 9]

# def gen_func(nums1):
# 	for n in nums1:
# 		yield n*n

# my_gen = gen_func(nums1)

# generator -> () bracket helyett --> []
my_gen = ( n*n for n in nums) 

for i in my_gen:
	print(i)