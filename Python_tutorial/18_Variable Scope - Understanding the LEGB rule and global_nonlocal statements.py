'''
LEGB
Local , Enclosing , Global, Built-in
'''
# PELDA 1 ##############################################
# x = 'global x'

# def test():
# 	y = 'local y'
# 	print(y)
# 	# print(x)

# test()
# print(x)

# PELDA 2 ##############################################
# x = 'global x'

# def test():
# 	# globalisa teszem az x valtozot
# 	# global x
# 	x = 'local x'
# 	print(x)
# 	# print(x)

# test()
# print(x)


# PELDA 3 ##############################################

# import builtins

# # milyen cuccok vannak beepitve
# print(dir(builtins))


# # beepitett fgv felul irhatod
# # lokal scope-ban atirod es utana mar nem nezi a builtin-be
# def min():
# 	pass

# m = min([5,4,2,3])
# print(m)

# PELDA 4 ##############################################
x = 'global x'

def outer():
	x = 'outer'

	def inner():
		# most mar az outer-ben is elerheto
		# felulrija azt
		# nonlocal x
		x = "inner"
		print(x)

	inner()
	print(x)

outer()
print(x)