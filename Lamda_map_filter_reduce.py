# ## Lambda function

sum = lambda x,y : x+y  # lambda syntax
# print(sum(5,4))

# ## map(func,seq)  -->  iterator

l = [1,2,3,4,5,6,7,8,9]

def sqr(n):
    return n*n
lsqr = map(sqr,l)  # iterator  - using normal function
lsqr = map(lambda x : x*x,l)  # iterator - using lambda
l2 = list(lsqr)
# print(l,"\n",lsqr,"\n",l2)

# map() in more than one list

l1 = [1,2,3,4,5,6,7,8,9]
l2 = [12,23,23,34,45,56,67,78,89]
l3 = [123,234,345,456,567,678,789,890,901]

lsum = list(map(lambda x,y,z : x*y+z,l1,l2,l3))
# print(l1)
# print(l2)
# print(l3)
# print(lsum)

# with unequal elements


l1 = [1,2,3,4,5,6,7,8,9]
l2 = [12,23,23,34,45,56,67,78,89]
l3 = [123,234,345,456,567,678,789]

lsum = list(map(lambda x,y,z : x*y+z,l1,l2,l3))
# print(l1)
# print(l2)
# print(l3)
# print(lsum)  # map() executes upto length of smallest sequence

# ## filter(func,seq) --> iterator of filtered elements

l1 = list(range(0,100))

lresult = list(filter(lambda x : x%3 == 0,l1))  # number divisible by 3
print(lresult)


# ## reduce(func,sequence) --> single value
from functools import reduce
l = [1,2,3,4,5,6,7,8,9]
def func(x,y):
    if x>y:
        return x-y
    else:
        return y-x

s = reduce(func,l)
print(s)

