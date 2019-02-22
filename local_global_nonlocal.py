## How to use global variable?

# def one():
#     print(s)  # global variable
#
# s="roshan"
# one()
#
# def sec():
#     s = "singh"  # local variable
#     print(s)  # local variable overrides global variable
# s="roshan"
# sec()
#
# def thr():
#     """NOTE: for ambiguity any variable in scope may be local or global.
#      therefore  using global variable and declaring it local later will throw error"""
#     print(s)  # <-- error
#     s="singh"
#     print(s)
# s="roshan"
# thr()


"""USING global keyword"""

# def four():
#     """this will specify variable global so that
#     we can assign/change value of variable
#     and change get reflected over whole module."""
#     global s
#     print(s)
#     s="singh"
#     print(s)
# s="roshan"
# four()
# print(s)

# def five():
#     """this demonstrate that we can create global variable instde
#     function that prior dont exist but it cant be accessed without
#     assigining value"""
#     global x
#     # print(x)  # --> error since x is not yet defined
#     x="qaz"
#     print(x)
# five()
# print(x)
#

# ------GLOBAL VARIABLE IN NESTED FUNCTION--------

def f():
    """this demonstrate that despite of what global variable
    is, it dont affect local variable and local variable is accessed first"""
    x = 42
    def g():
        global x
        x = 43
    print("Before calling g: " + str(x))
    print("Calling g now:")
    g()
    print("After calling g: " + str(x))
f()
print("x in main: " + str(x))


#  ----------NONLOCAL VARIABLE---------

def f():
    """this type of variable can only be used with nested function where
    nested function needs to access parent function's variable and change it.
    'nonlocal' specifier  specifies a variable to be nonlocal but not global
    but local to parent function"""
    x = 42
    def g():
        nonlocal x
        x = 43
    print("Before calling g: " + str(x))
    print("Calling g now:")
    g()
    print("After calling g: " + str(x))  # local variable of parent function changed
x = 3
f()
print("x in main: " + str(x))  # global variable dont get affected