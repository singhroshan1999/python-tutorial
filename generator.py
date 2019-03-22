# ## iter(seq) --> itrator
# use next(itrator) to get next element
# StopIteration thrown when no element left

countries = ['India','USA','Canada','Russia','China','Sri Lanka']
iterator = iter(countries)  # creating iterator
# print(next(iterator))
# print(next(iterator))  # itrating iterator
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

other_cities = ["Strasbourg", "Freiburg", "Stuttgart",
"Vienna / Wien", "Hannover", "Berlin",
"Zurich"]
city_iterator = iter(other_cities)  # for loop equivalent while loop
# while city_iterator:
#     try:
#         city = next(city_iterator)
#         print(city)
#     except StopIteration:  # catching exception
#         break

# ## yield() and generators

def gen():  # generator function
    yield("India")
    yield("USA")
    yield ("Canada")
    yield("Russia")
    yield("China")

# print(gen())
# print(next(gen()))  # each time new generator is created hence every time India will be returned
# print(next(gen()))
# print(next(gen()))
# print(next(gen()))
# print(next(gen()))
# print(next(gen()))

g = gen()  # creating generator

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# ## using return in generator

def even3(n1,n2):
    for i in range(n1,n2+1):
        if(i%3 == 0):
            raise StopIteration(i)
        yield(i*2)
def even32(n1,n2):
    for i in range(n1,n2+1):
        if(i%3 == 0):
            return i  # better
        yield(i*2)

g = even32(10,20)  # creating generator

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# ## sent() method and coroutine

def count():
    status = ''
    i=0
    while status != 'STOP':
        status = yield i
        i+=1
        if status == 'RESET':
            i=0
    return

c = count()
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(c.send('RESET'))
# print(next(c))
# print(next(c))
# print(next(c))
# c.send('STOP')


# ## throw() method

def count2(n):
    count = 0
    while True:
        try:
            yield n*count
        except Exception :
            print(count)
        count+=1

c = count2(5)
# print(next(c))
# print(next(c))
# print(next(c))
# c.throw(Exception)  # generator was paused at 2
# print(next(c))
# print(next(c))
# print(next(c))
# c.throw(Exception)


# ## decorating generator

from functools import wraps
def get_ready(gen):
    """
Decorator: gets a generator gen ready
by advancing to first yield statement
    """
    @wraps(gen)
    def generator(*args,**kwargs):
        g = gen(*args,**kwargs)
        next(g)
        return g
    return generator
@get_ready
def infinite_looper(objects):
    count = -1
    message = yield None
    while True:
        count += 1
        if message != None:
            count = 0 if message < 0 else message
        if count >= len(objects):
            count = 0
        message = yield objects[count]
x = infinite_looper("abcdef")
# print(next(x))
# print(x.send(4))
# print(next(x))
# print(next(x))
# print(x.send(5))
# print(next(x))


# ## yield from

def yld():
    yield from "roshan" # ###

# for x in yld():
#     print(x)

# ## recursive generator

def permutations(items):
    n = len(items)
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i]+items[i+1:]):
                yield [items[i]]+cc
# for p in permutations(['r','e','d']): print(''.join(p))
# for p in permutations(list("game")): print(''.join(p) + ", ", end="")

# ## generator of generators

def fibonacci():
    """Ein Fibonacci-Zahlen-Generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
def firstn(g, n):
    for i in range(n):
        yield next(g)
print(list(firstn(fibonacci(), 10)))