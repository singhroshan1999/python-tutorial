"""Some important aspect of function"""

# 1. function names are just reference and can be more than one.

def one():
    print("roshan")
one_2 = one  # creating another reference
one()
one_2()
del one  # deleting one reference dont remove function till there is reference
one_2()

# 2. nested function

def two(n):
    def two_2(n):
        return n*n*n
    result = two_2(n)
    print(result)

two(4)

# 3. passing function as parameter.

def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")
def f(func):
    print("Hi, it's me 'f'")
    print(f"I will call '{func.__name__}' now")  # original function name
    func()
f(g)

# 4. function returning function

def f(x):
    def g(y):
        return y + x + 3
    return g
nf1 = f(1)
nf2 = f(3)
print(nf1(1))
print(nf2(1))