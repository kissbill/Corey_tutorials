# # Generikus hiba elkapas #######################################
# try:
# 	f = open('testfile.txt')
# except Exception as e:
# 	print("Nincs meg a fajl")
# else:
# 	pass
# finally:
# 	pass
# File hiba elkapas #######################################
# try:
# 	f = open('testfile.txt')
# 	var = bad_var
# except FileNotFoundError as e:
# 	print(e)
# except Exception as e :
# 	print(e)

# # Else ag futattasa #######################################
# try:
# 	f = open('31_testfile.txt')
# except Exception as e:
# 	print("Nincs meg a fajl")
# else:
# 	print(f.read())
# 	f.close()
# finally:
# 	pass
# # Finally ag futattasa #######################################
# try:
# 	f = open('31_testfile.txt')
# except Exception as e:
# 	print("Nincs meg a fajl")
# else:
# 	print(f.read())
# 	f.close()
# finally:
# 	print("vegul en futok le ")
# # Sajat exepction ag futattasa #######################################
try:
	f = open('31_corrupt_file.txt')
	if f.name == '31_corrupt_file.txt':
		raise Exception
except Exception as e:
	print("Error !")
else:
	print(f.read())
	f.close()
finally:
	print("vegul en futok le ")