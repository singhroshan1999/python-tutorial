## itrable --> any object (like list tuple string) that can be iterated.
#           calling iter(obj) returns itrator object

## itrator --> actual object that is iterated in for loop
#           calling next(obj) returns next element

# s = "roshan" # iterable
# _s = iter(s)  # iterator
#
# print(_s)  # object
# print(next(_s))  # r
# print(next(_s))  # o
# print(next(_s))  # s
# print(next(_s))  # h
# print(next(_s))  # a
# print(next(_s))  # n
# print(next(_s))  # error


## class

class Reverse:
    """
    Creates Iterators for looping over a sequence backwards.
    """
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]*5


lst = [34, 978, 42]
lst_backwards = Reverse(lst)
for el in lst_backwards:
    print(el)
