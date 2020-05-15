# Decorators - Dynamically Alter The Functionality Of Your Functions
# https://www.youtube.com/watch?v=FsAPt_9Bf3U&t=3s
# 1.################################################################
# def outer_function(msg):
# 	message = msg

# 	def inner_function():
# 		print(message)
# 	return inner_function()

# hi_func = outer_function('HI')
# bye_func = outer_function('BYE')


# hi_func()
# bye_func()

# 2.################################################################
# def decorator_function(original_function):
# 	def wrapper_function():
# 		return original_function()
# 	return wrapper_function

# @decorator_function # --> ezzel egyenlo -->decorator_display = decorator_function(display)
# def display():
# 	print('display function run')

# decorator_display = decorator_function(display)

# # decorator_display()
# display()

# 3.################################################################
# def decorator_function(original_function):
# 	def wrapper_function(*args,**kwargs):
# 		print('wrapper ecexute this before {}'.format(original_function.__name__))
# 		return original_function(*args,**kwargs)
# 	return wrapper_function

# @decorator_function
# def display():
# 	print('display function run')

# @decorator_function
# def display_info(name, age):
# 	print('display_info ran with arguments ({}, {})'.format(name, age))

# display_info('Jane', 22)
# display()

# 4.################################################################
# decarator as a class usage : 

# class decorator_class(object):

# 	def __init__(self,original_function):
# 		self.original_function = original_function

# 	def __call__(self,*args,**kwargs):
# 		print('call method ecexute this before {}'.format(self.original_function.__name__))
# 		return self.original_function(*args,**kwargs)

# @decorator_class
# def display_info(name, age):
# 	print('display_info ran with arguments ({}, {})'.format(name, age))

# display_info('Jane', 22)

# 5.################################################################

# Decorators
from functools import wraps


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time


@my_logger #chaining --> display_info = my_logger(my_timer(display_info))
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Tom', 22)