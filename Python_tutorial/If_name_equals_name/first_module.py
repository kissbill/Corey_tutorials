
# print( "First module's Name : {}".format(__name__))

# def main():
# 	pass

# if __name__ == '__main__':
# 	main()

# 	# python direktbe futattja, vagy import-knet ?
# 	# ezt ellenorzi

# direktbe meghivjuk #################################
# def main():
# 	print( "First module's Name : {}".format(__name__))

# if __name__ == '__main__':
# 	main()


# if elif meghivjuk #################################

# if __name__ == '__main__':
# 	print( "Run directly")
# else:
# 	print( "Run from import")

# kulon fgv vagy csak az egesz scope-ban van #################################

print("WIll be run always")

def main():
	print( "First module's Name : {}".format(__name__))

if __name__ == '__main__':
	main()