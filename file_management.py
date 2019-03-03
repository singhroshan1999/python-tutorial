# fptr = open("out.txt")  # open() opens a file pointer which is 'itrator' object, bydefault open(fileName) ~ open(file,"r")
# # for i in fptr:
# #     print(i)  # prints unstripped line
#
# for i in fptr:  # itrated over line by line
#     print(i.rstrip())  # right strip whitespaces and newline
#
# fptr.close()  # closes file

# ## Writing to file

# fptr = open("out.txt")
# fptr2 = open("out2.txt","w")
# lineno = 1
# for line in fptr:
#     fptr2.write("{0:2d}. ".format(lineno)+line.rstrip()+"\n")
#     lineno+=1
# fptr2.close()

# ## using with operator --> closes file pointer automatically

# reading example

# with open("out.txt") as fptr:  # closes fptr automatically
#     for i in fptr:
#         print(i.rstrip())

# write eample
# lineno = 1
# with open("out.txt") as fptr:
#     with open("out2.txt","a") as fptr2:  # nesting with statment to open multiple file pointer
#         for line in fptr:                # instead of using "w" used "a" to append file
#             fptr2.write("{0:2d}. ".format(lineno)+line.rstrip()+"\n")
#             lineno+=1

# ## Reading files in one go readlines() read()
# open().readlines() --> list of all lines of file
# open().read() --> single string containing whole file

# fptr = open("out.txt")
# poem = fptr.readlines()  # read whole file into list
# print(poem)
# fptr.close()
#
# strr = open("out.txt").read()  # read whole file into single string
# print(strr)


# ## Resetting file pointer's current position

# fptr = open("out.txt")
# print(fptr.read(10))  # read 7 character
# print(fptr.tell())  # returns current position
# fptr.seek(fptr.tell()-5)  # seeks current position - 5 character position
# print(fptr.read(10))
# print(fptr.tell())
# fptr.close()

# ## Read-write same file


fh = open('out.txt', 'w+')  # this openns file for reading and wriring both
fh.write('The colour brown')
# Go to the 12th byte in the file, counting starts with 0
fh.seek(11)
print(fh.read(5))
print(fh.tell())
fh.seek(11)
fh.write('green')
fh.seek(0)
content = fh.read()
print(content)