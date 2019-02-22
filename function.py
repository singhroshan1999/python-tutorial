## function
# def fun_name(argList):
#   statments....


# def cube(n):  # simple example
#     print(n*n*n)
#
#
# cube(12)
#
#
# def cube(n,sign = 1):  # with optional/default argument and docstring
#     """This function returns cube
# with optional sign parameter"""
#     print(n*n*n*sign)
#
#
# cube(12)  # +ve  default value assigned
# cube(12,-1)  # -ve asigining optional argument value
# print(cube.__doc__)  # getting docstring


# def calc(a,b=0,c=0,d=1,e=1):
#     """add, sub, mult, div all in one function"""
#     print(((a+b-c)*d)/(e*1.0))
#
# calc(10,5)
# calc(10,c=5)
# calc(10,d=5)
# calc(10,e=5)
# calc(10,5,d=3)
# calc(10,b=5,e=4)
#
#
# def calc(a,b=0,c=0,d=1,e=1):
#     """same as above but returns value"""
#     return((a+b-c)*d)/(e*1.0)
#
#
# print(calc(10,b=5,e=4))


# def sqube(n):
#     """returning multiple values"""
#     return n*n,n*n*n
#
# s,c = sqube(3)
#
# print(f"square: {s}  cube: {c}")


## global variable

# def prn():
#     # print(s)  # s not defined
#     s="hello"
#     print(s)
# s="hiii"
# prn()
# print(s)

# def prn():
#     """ To access/change any global variable "global" keyword must be used"""
#     global s  # accessing global variable
#     print(s)
#     s="hello"
#     print(s)
#
#
# s="hiii"
# prn()
# print(s)
#


## arbitrary no of argument

# def printf(*val):  # using tuple
#     for i in val:
#         print(i,end=".")
#     print(f"\n {val}")
#
# printf(123,"gsfgdfg",12.34)


## arbitrary no of keyword parameteer

# def printd(**val):  # using dictionary
#     print(val["first"],val["middle"],val["last"])
#     print(val)
#
# printd(first="roshan",middle="kumar",last="singh")


# ### Passing Arguments

# def ref_demo(x):  # different IDs
#     print("x=",x," id=",id(x))  # argument
#     x=42
#     print("x=",x," id=",id(x))  # local variable
#
# ref_demo(5)

# sideeffects

# def no_sideeffect(l):
#     print(l)
#     l = l + [6,7,8]  # simple assignment dont create sideeffect
#     print(l)
#
# lst = [1,2,3,4,5]
# no_sideeffect(lst)
# print(lst)
#
# def sideeffect(l):
#     print(l)
#     l += [6,7,8]  # augumented assignment creates sideeffect
#     print(l)
#
# lst = [1,2,3,4,5]
# sideeffect(lst)
# print(lst)
#
# def sideeffect(l):
#     print(l)
#     l += [6,7,8]
#     print(l)
#
# lst = [1,2,3,4,5]
# sideeffect(lst[:])  # it can be avoided by using simple shallow copy (in this case)
# print(lst)


# ### command line argument using sys.argv

# import sys
#
# for i in sys.argv:  # sys.argv[0] is program file name (function.py) it self
#     print(i)
#

# ### asterisk and double asterisk

def arb_arg(first,secont,*nth):  # arbitrary number of argument
    print(first)
    print(secont)
    for i in nth:
        print(i)

arb_arg("roshan","singh",313123,123123,23,435,456,456,57,68,678,79)

def zip_arg(first,sec,third):
    print(first,sec,third)

t = "roshan","singh",20
zip_arg(*t)  # expanding tuple into argument of caller


def key_arg(**arg):  # arbitrary keyword argument
    print(arg["first"],arg["sec"],arg["third"])

key_arg(first="roshan",sec = "singh",third=20)


def zip_key(first,second,third):
    print(first,second,third)

d = {"first":"roshan","second":"singh","third":20}
zip_key(**d)  # expand dictionary into arbitrary keyword




