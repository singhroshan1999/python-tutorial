# ## try - except block

# try:
#     n = input("Enter integer:")
#     n = int(n)
#     print(n)
# except ValueError:
#     print("Enter Valid number")


# ## multiple except clause

try:  # multiple except clause
    fptr = open('out.txt')
    str = fptr.readline()
    n = int(str.strip())
    print(n)
except IOError as e:  # specifing additional variable
    errno,stderror = e.args  # instance.args to access variable. Error on and standard error message
    print("enter valid file",errno,stderror)
except ValueError as xyz:
    print("file dont have integer",xyz)

# ## multiple Exception in tuple (Exception1,Exception2)
print("---------------------------------------")
try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
except (IOError, ValueError) as e:  # tuple of errors
    print("An I/O error or a ValueError occurred",e)
except:
    print("An unexpected error occurred")


# ## exception in function within try block
print("---------------------------------------")
def f():
    x = int("four")
try:
    f()  # exception will be caught here!
except ValueError as e:
    print("got it :-) ", e)
print("Let's get on")

# ## exception inside function()'s try block within try block
print("---------------------------------------")

def f():
    try:
        x = int("four")  # Exception will be caught here
    except ValueError as e:
        print("got it in the function :-) ", e)
try:
    f()  # not here
except ValueError as e:
    print("got it :-) ", e)
print("Let's get on")

# ## using raise to again raise Exception
print("---------------------------------------")

def f():
    try:
        x = int("four")  # Exception will be caught here
    except ValueError as e:
        print("got it in the function :-) ", e)
        raise
try:
    f()  # here also
except ValueError as e:
    print("got it :-) ", e)
print("Let's get on")

# ## try ... finally block
print("---------------------------------------")

def err(n):
    try:
        print(int(n))
    finally:
        print("there may or may not be any error")
err(1233)
err("121212")
# err("1212 12")  # error here

# try ... except ... finally --> exectued always
print("---------------------------------------")

try:
    x = float("13123 23")
    inverse = 1.0 / x
except ValueError:
    print("You should have given either an int or a float")
except ZeroDivisionError:
    print("Infinity")
finally:
    print("There may or may not have been an exception.")

# try ... except ... else --> executed when there is no Exception
print("---------------------------------------")
try:
    x = float("1312323")
    inverse = 1.0 / x
except ValueError:
    print("You should have given either an int or a float")
except ZeroDivisionError:
    print("Infinity")
else:
    print("There may not have been an exception.")