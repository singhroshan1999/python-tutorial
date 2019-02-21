# # # Sets and FrozenSets

# simple demo
#
# s = set("hello, Python")  # only unique element stored
# print(s)
#
# s2 = set(['123', 'qwe', '!@!@'])  # using list
# print(s2)
#
# s3 = set((1,2,3,4,3,2,3,3,4,56,))  # using tuples
# print(s3)


# frozen() set --> immutable

#
# s = frozenset("hello, Python")  # only unique element stored
# print(s)
#
# s2 = frozenset(['123', 'qwe', '!@!@'])  # using list
# print(s2)
#
# s3 = frozenset((1,2,3,4,3,2,3,3,4,56,))  # using tuples
# print(s3)


#  using braces instead of built-in method

# s = {1,2,3,4,5,4,3,2,4,4,5,5}
#
# print(s)


# set operations

# s.add("this is added")  # add unique element or else do nothing
# print(s)
#
# s2 = s.copy()  # create shallow copy
# s.clear()  # removes all element of set
# print(s)
# print(s2)

x = {"a","b","c","d","e"}
y = {"b","c"}
z = {"c", "d"}
w = {1,2,3,4}
a = {'qaz','wsx','edc'}
#
# print(x.difference(y))  # removes common element
# print(x-y)  # same
#
# print(x.difference(y).difference(z))  # chaining
# print(x-y-z)  # same


# x.difference_update(y)  # remove common element from x same as x = x-y
# x=x-y
# print(x)

# removing element

# print(x)
# x.discard("a")  # removing any element
# x.discard("x")  # removing non-existing element
# print(x)
#
# x.remove("b")  # removing any element
# # x.remove("x")  # removing non-existing element  --> KeyError
# print(x)

# union / intersection

# print(x.union(w))  # union
# print(x.union(w).union(a))  # chaining
# print(x|w|a)  # using "|" notation
#
# print(x.intersection(y))  # intersection
# print(x.intersection(y).intersection(z))  # chaining
# print(x&y&z)  # uning "&" notation


# isdisjoint() / issubset() / issuperset()

# print(x.isdisjoint(y))
# print(x.isdisjoint(w))
#
#
# print(x.issubset(y))
# print(x<=y)
# print(y.issubset(x))
# print(y<=x)
#
# print(x.issuperset(y))
# print(x>=y)
# print(y.issuperset(x))
# print(y>=x)
#
# print(x<=x)  # subset
# print(x<x)  # proper subset
#
# print(x>=x)  # superset
# print(x>x)  # proper superset

print(x)
print(x.pop())
print(x)



