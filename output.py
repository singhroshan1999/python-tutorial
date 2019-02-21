## general format of print()
# print(value1, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

# print("a","b")  # default sep = " ", end = "\n", file = sya.stdout
# print("a","b",sep=".")
# print("a","b",end="#")
# fp = open("out.txt","w")
# print("a","b",file=fp)
#
# print("roshan","singh",sep="|",end="?",file=fp)

# import sys
# print("roshan",file=sys.stderr)  # output in standard error

## formated output --> %[flags][width][.precision]type

# print("amount: %d"%(50))  # simple
#
# print("amount: %3d"%(50))
# print("amount: %3d"%(500))
# print("amount: %3d"%(500))
#
# print("amount: %2.5f"%(50))
# print("amount: %2.5f"%(5.6565))
# print("amount: %2.5f"%(10.12345))

# print("%o"%(50))
# print("%x:%X"%(500,500))

# print("%e"%(1000))
# print("%E"%(1000))
# print("%g"%(100000))
# print("%g"%(1000000))
# print("%G"%(0.00001))


# print("%-5d"%(1))
# print("%-5d"%(10))
# print("%-5d"%(1000))
# print("%-5d"%(10000))
# print("%-5d"%(100000))
# print("%5d"%(1))
# print("%5d"%(10))
# print("%5d"%(1000))
# print("%5d"%(10000))
# print("%5d"%(100000))
# print("%+5d"%(1))  # didnt understand +
# print("%+5d"%(10))
# print("%+5d"%(1000))
# print("%+5d"%(10000))
# print("%+5d"%(100000))


## using template.format(...)

# print ("id: {0:d} age: {1:d}".format(1231,21))  # simple
#
# print("n={0:d}  s={1:2.5f}  s/n = {1:2.5f}/{0:d} = {2:2.5f}".format(5,35,6))  # repeated argument
#
# print("artNo: {a:5d}  price: {b:5.5f}".format(b=123.24234554,a=53421))  # using keyword parameter

# options
#-> <>^0
# print("id: |{0:8.2f}|".format(532.2))  # default left-align
# print("id: |{0:<8.2f}|".format(532.2))  # < --> right-align
# print("id: |{0:>8.2f}|".format(532.2))  # > --> left-align
# print("id: |{0:^8.2f}|".format(532.2))  # ^ centered-align
# print("id: |{0:08.2f}|".format(532.2))  # 0 --> zero-padding

# print("prince: {0:d}".format(10000000000000000))
# print("prince: {0:,d}".format(10000000000000000))  # , --> adds comma after every thousand

# print("prince: |{0:6d}|".format(-100))
# print("prince: |{0:=6d}|".format(-100))  # = --> puts sign before padding eg. '-  100'
# print("prince: |{0:+6d}|".format(100))  # + --> show + and minus sign
# print("prince: |{0:+6d}|".format(-100))
# print("prince: |{0:-6d}|".format(100))  # - --> show only minus sign
# print("prince: |{0:-6d}|".format(-100))
# print("prince: |{0: 6d}|".format(-100))  # didnt get it
# print("prince: |{0: 6d}|".format(100))

## using dictionary
# name = {"f_name":"roshan","l_name":"singh"}
# print("First Name: {f_name}  Last Name: {l_name}".format(**name))


# using local variable locals()

# a="roshan"
# b="singh"
# l = [1,2,3,4]
# d=locals()
#
# print("a={b}  b={b}  l={l}".format(**d))

## using string class to format using rjust(),ljust(),zfill(),center()

# rjust,ljust,center --> (width[, fillchar])
# zfill --> (width)

# s = "hello";
#
# print(s.ljust(10))  # left justify
# print(s.ljust(10,"_"))  # '_' as filler
# print(s.rjust(10))  # right justify
# print(s.rjust(10,"_"))
# print(s.center(10))  # center justify
# print(s.center(10,"_"))
# print(s.zfill(10))  # pad '0' to left

## formatted string literal

# it is same as calling template.format(...) but syntax is different
# f"<string template>" here only variable should be used in {...}
# expression in {...} is evaluated  ex "{5*8}"  --> "40"

price = 5.2
print(f"interest = Rs.|{price*(5/100):^10.5}|")


