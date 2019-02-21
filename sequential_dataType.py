# s = "python is great"
# print(s[0:6])
# print(s[-8:-6])
#
# s1 = "roshan"
# s2 = "singh"
# s = s1 + ' ' + s2
# print(s)
#
# l1 = ["ros", 'han']
# l2 = [' ', '']

# # extend
lst = [1, 2, 3, 4, 3, 5, 6, 3]
# st = 'hello'
# tup = 12, 23, 34, 45,
# lst.extend(st)
# lst.extend(tup)
# print(lst)

# # using (+) as alternative to 'append' and 'extend'
#
# lst = lst + [12]  # ~1268 times slower
# lst += [12]  # good
# lst.append(12)  # best

# # Removing elements
# print(lst)
# lst.remove(12)
# lst.remove(12)
# lst.remove(12)
# lst.remove(12)  # valueError if element dont exist
print(lst)

# # finding position using index(element[,start[,end]])

print(lst.index(3))
print(lst.index(3, 2))
print(lst.index(3, 5))
print(lst.index(3, 3, 6))


# # inserting element at arbitrary position using insert(pos,obj)

print(lst)
lst.insert(0,12)
lst.insert(5,90)
lst.insert(-1,121) # not inserted at last
# [12,1,2,3,4,90,3,5,6,3,121]
lst.insert(len(lst),1211)
print(lst)



