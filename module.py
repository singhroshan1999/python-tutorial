### IMPORTING ANY MODULE

# 1

"""use math.xxx namespace to access elements of math"""
# import math
# print(math.sin(3.14))

# 2

"""multiple import in one line"""
# import math, random
# print(math.cos(random.random()*3.14))

# 3

"""import elements of module into user namespace and access without modname.xxx"""
# from math import sin, pi
# print(sin(pi))

# 4

"""import all element of module into user namespace. NOT RECOMMENDED"""
# from math import *
# print(sin(pi),cos(pi),e)

# 5

"""import module with alias name. modname ~ mn"""
# import random as rd
# print(rd.random())

# 6

"""import element of module in user namespace with alias name"""
# from math import cos as cosine,pow as power
# print(cosine(3.14),pow(2,4))

# ## Module Search path
# where file is being executed --> directories of PYTHONPATH --> standard installation path /python3.5

# USER MODULE

# import demo_module  # importing user module
#
# print(demo_module.fib(5))  # calling user module
# print(demo_module.fib(10))
# print(demo_module.ifib(15))
# print(demo_module.ifib(20))
#
# fib = demo_module.fib  # assigning local name to module
#
# print(fib(5))
# print(fib(10))


# ## Executing module's statment

import demo_module2 # this will execute plain statment of module

import demo_module2 # executed only once cannot be RELOADED

# #Reloading module

# import implib


# ##Executing module as script

# use: if executed as script then if statment is true else false

# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))
# --> SEE demo_module.py

# ## Return all built-in module
# import sys
# print(sys.builtin_module_names)

# getting all valid attribute and method of module

import math
print(dir(math))  #--> for math module
print(dir())  #--> for user namespace

import builtins
print(dir(builtins)) # --> for all builtin