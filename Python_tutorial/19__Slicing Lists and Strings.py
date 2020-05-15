# Slicing Lists and Strings
# https://youtu.be/ajrtAuDg3yw

# 1 ########################################################################
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 		 # 0  1  2  3  4  5  6  7  8  9	
# 	    #-10 -9 -8 -7 -6 -5 -4 -3 -2 -1


# # list[start:end:stop]



# print(my_list[0:5])
# print(my_list[2:5])
# print(my_list[:5])

# print(my_list[4:])

# print(my_list[2:8:2])
# print(my_list[-1:0:-2])

# print(my_list[::-1])

# 2 ########################################################################

sample_url = 'https://mail.google.com/mail/u/0/?pli=1#inbox'

# Revese the URL
print(sample_url[::-1])

# get the top domain url
print(sample_url[-6:])

# get the http out
print(sample_url[8:])

# no domain and http
print(sample_url[8:-6])