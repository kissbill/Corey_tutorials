# 1. pelda kod ########################################################
# def square_numbers(nums):
# 	result = []
# 	for i in nums:
# 		result.append(i * i)
# 	return result

# my_nums = square_numbers([1,2,3,4,5])


# print(my_nums)


# 2. pelda kod ########################################################
def square_numbers(nums):
    for i in nums:
        yield (i * i)
        # 1 result at a time

# my_nums = square_numbers([1,2,3,4,5])
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(my_nums)

# for num in my_nums:
# 	print(num)

# 3. pelda kod ########################################################
# memoriaba kerul
# my_nums = [x*x for x in [1,2,3,4,5]]

# print(my_nums)


# 4. pelda kod ########################################################
# GENERATOR - nincs memoriaban
my_nums = (x * x for x in [1, 2, 3, 4, 5])

# listava konvertalom
# viszont elvesztem az perfomance elonyt urja memoriat olvass
print(list(my_nums))
