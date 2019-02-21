# ## while loop
# i = input("enter")
# j=0
# while j<len(i):
#     print(i[j])
#     j+=1
#

# import sys
#
# text = ""
# while 1:
#     c = sys.stdin.read(1)
#     text += c
#     if c == '\n':
#         break
# print(text)

# while j<len(i):
#     print(i[j])
#     if(i[j] == 'd'):
#         break
#     j+=1
# else:
#     print("else executed")


## For loop

# for i in ["roshan","singh","asdasd"]:
#     print(i)
# else:
#     print("else block")

# range() function

# print(range(10))  #--> outputs 'range(0,10)'
# print(list(range(10))) #--> [0,1,2,3,4,5,6,7,8,9]
# print(list(range(-5,5))) #--> [-5,-4,-2,-1,0,1,2,3,4]
# print(list(range(-20,0,4))) #--> [-20,-16,-12,-8,-4]

# for-list sideeffects

l = [1]
for i in l: # with side effect
    if i == 1:
        l.append(2)
    if i == 2:
        l.append(3)
print(l)
l=[1]
for i in l[:]: # without side effect
    if i == 1:
        l.append(2)
    if i == 2:
        l.append(3)
print(l)




