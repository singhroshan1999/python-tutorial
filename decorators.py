"""Some important aspect of function"""

# 1. function names are just reference and can be more than one.

# def one():
#     print("roshan")
# one_2 = one  # creating another reference
# one()
# one_2()
# del one  # deleting one reference dont remove function till there is reference
# one_2()

# 2. nested function

# def two(n):
#     def two_2(n):
#         return n*n*n
#     result = two_2(n)
#     print(result)
#
# two(4)

# 3. passing function as parameter.

# def g():
#     print("Hi, it's me 'g'")
#     print("Thanks for calling me")
# def f(func):
#     print("Hi, it's me 'f'")
#     print(f"I will call '{func.__name__}' now")  # original function name
#     func()
# f(g)

# 4. function returning function

# def f(x):
#     def g(y):
#         return y + x + 3
#     return g
# nf1 = f(1)
# nf2 = f(3)
# print(nf1(1))
# print(nf2(1))

# ### DECORATOR

# simple decorator

# def decor_func(func):  # decorator function
#     def modified_func(n):  # modifier function
#         print("about to call {0}()".format(func.__name__))
#         func(n)
#         print("called {0}()".format(func.__name__))
#     return modified_func  # decorator returns modified function
#
# def my_function(n):
#     print(n*n*n)
#
# my_function(5)  # non decorated function

# my_function = decor_func(my_function) # decorating
# my_function(5)  # calling decorated function

# usual/actual syntax for python decorator

# @decor_func  # decorating function
# def my_function2(n):
#     print(n*n*n*n)
#
# my_function2(5)  # calling decorated function

# ## decorating third party function

# from math import sin, cos
#
# def absolute_maker(func):
#     """this decorator makes any function's argument absolute i.e +ve"""
#     def modifier_func(n):
#         return func(abs(n))
#     return modifier_func
#
# print("Undecorated function: %f %f"%(sin(-20),cos(-20)))
# sin = absolute_maker(sin)
# cos = absolute_maker(cos)
# print("Decorated function: %f %f"%(sin(-20),cos(-20)))


# ## Decorator with parameter

# def deco_param(arg):  # makes decorator parameterized, just a wrapper function
#     def deco_func(func):  # original decorator function
#         """ it is called before even funnction func() is called"""
#         print("Inside {0}() calling parameter {1}".format(func.__name__,arg))
#         def modifier_func(n):  # modifier function
#             print("about to call {0}()".format(func.__name__))
#             func(n)
#             print("called {0}()".format(func.__name__))
#         return modifier_func
#     return deco_func
#
#
# @deco_param("THIS_IS_PARAMETERIZED_DECORATER")
# def cube(n):
#     print(n*n*n)
#
# cube(5)


"""NOTE: during decoration of function __name__,__doc__,__module__ is lost
to avoid this we do following things:"""

# ## Example illustrate simple technique to overcome above mentiioned problem

def decor_func(func):  # decorator function
    def modified_func(n):  # modifier function
        """this is modified_func docstring"""
        print("about to call {0}()".format(func.__name__))
        func(n)
        print("called {0}()".format(func.__name__))
    return modified_func  # decorator returns modified function

@decor_func
def my_function(n):
    """this is my func docstring"""
    print(n*n*n)

print("__name__",my_function.__name__)
print("__doc__",my_function.__doc__)
print("__module__",my_function.__module__)

#------------------------------------------------------
def decor_func(func):  # decorator function
    def modified_func(n):  # modifier function
        """this is modified_func docstring"""
        print("about to call {0}()".format(func.__name__))
        func(n)
        print("called {0}()".format(func.__name__))
    modified_func.__name__ = func.__name__
    modified_func.__doc__ = func.__doc__
    modified_func.__module__ = func.__module__
    return modified_func  # decorator returns modified function


@decor_func
def my_function(n):
    """this is my func docstring"""
    print(n * n * n)


print("__name__", my_function.__name__)
print("__doc__", my_function.__doc__)
print("__module__", my_function.__module__)

# ## USING wraps from functools module

from functools import wraps

def decor_func(func):  # decorator function
    @wraps(func)
    def modified_func(n):  # modifier function
        """this is modified_func docstring"""
        print("about to call {0}()".format(func.__name__))
        func(n)
        print("called {0}()".format(func.__name__))
    return modified_func  # decorator returns modified function

@decor_func
def my_function(n):
    """this is my func docstring"""
    print(n*n*n)

print("__name__",my_function.__name__)
print("__doc__",my_function.__doc__)
print("__module__",my_function.__module__)


"""decorator as class NOT DONE"""