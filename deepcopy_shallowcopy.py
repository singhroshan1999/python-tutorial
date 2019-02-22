# # # DEEP_COPY SHALLOW_COPY

lst1 = [1, 2, 3, 4]  # dont copy but copy reference only
# lst2 = lst1
# lst2[0] = 123
# print(lst1)

# lst2 = lst1[:]  # make shallow copy of list
# lst2[0] = 123
# print(lst1)
#
lst1 = [1, 2, 3, ['a', 'b'], ['qaz', 'wsx']]  # dont do deep copy
lst2 = lst1[:]
lst2[3][0] = 'X'
print(lst1)

# # # this module create deepcopy
# from copy import deepcopy
#
# lst1 = [1, 2, 3, ['a', 'b'], ['qaz', 'wsx']]
# lst2 = deepcopy(lst1)
# lst2[3][0] = 'X'
# print(lst1)
