# # # Dictionary

# # using dict
d = {'key1': 1, 'key2': 2, 'key3': 3}
# print(d)
# print(d['key1'])
# print(d['key2'])
# print(d['key3'])
#
# # print(d['key4'])  # # keyError --> if key not exist
#
# # adding element to dict
#
# d['key4'] = 4
# print(d['key4'])
#
#
# # incrementing empty dict
# d2 = {}
# d2['A'] = 'a'
# d2['B'] = 'b'
# print(d2)
#

# only immutable types can be key
#
# d3 = {(1, 2, 3): 123}  # immutable works
# print(d3)
# d4 = {[1, 2, 3]: 123} # mutable dont work --> TypeError: unhashable type: 'dict'
# print(d4)
# d5 = {{123: 'a'}: 123} # mutable dont work
# print(d5)

# operations on dictionary

# print(len(d))  # --> no of key value pair
# del d['key1']  # --> delete key1
# print('key1' in d)
# print('key2' in d)
# print('key3' not in d)


# pop() and popitems()

# print(d.pop('key2'))  # --> remove and returns value associated with key
# print(d)
# print(d.popitem())  # --> remove and return arbitrary (key,value) tupple
# print(d)


# accessing non existing key

# if 'key2' in d:
#     print(d['key2'])


#  copy --> creates shallow copy of dictionary

# dx = d.copy()
# print(dx)

#  clear() --> removes all key,value pair
# print(d)
# d.clear()
# print(d)

#  merging dictionary
#
# da = {1:12,2:23,3:34}
# db = {3:123,4:45,5:56}
# da.update(db)
# print(da)


# Iterating over dictionary
#
# di = {"a":123, "b":34, "c":304, "d":99}
# print(di)

# for key in di:  # get key
#     print(key)
#
# for key in di.keys():  # get key
#     print(key)
#
# for key in di:  # get value ~~slow
#     print(di[key])
#
# for value in di.values():  # get value ~~fast
#     print(value)


# List From Dictionary

# items() --> list of tuples of key,value pair
# keys() --> list of key
# values() --> list of values
#
# print(di.items())
# print(di.keys())
# print(di.values())


# Creating Dictionary From List

dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]

iterator = zip(dishes, countries)  # create iterator object
print(iterator)

iterator_list = list(iterator)  # casts iterator object to list of tuples of key,value
print(iterator_list)

dl = dict(iterator_list)  # cast list of tuples to dictionary
print(dl)

dl2 = dict(zip(dishes, countries))  # casting iterator directly to dict  ~~more efficient
print(dl2)
