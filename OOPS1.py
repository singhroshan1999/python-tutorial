# ## minimal class
class className:  # defining class
    pass  # when nothine is there put 'pass'

x = className()
y = className()
x1 = x
print(x == x1)
print(x == y)

className.attr = "roshan"  # assign class attribute
x.attr = "singh"  # assign instance attribute (overriding class attribute
print(className.__dict__,x.__dict__)  # get attribute:value dictionary
# getattr(inst,attr,def)

print(getattr(x,'bttr',100)) # safe way to get attribute
x.bttr = 200
print(getattr(x,'bttr',100))


# # attribute of functino

def f(x):
    f.counter = getattr(f, "counter", 0) + 1
    return "Monty Python"
for i in range(10):
    f(i)
print(f.counter)


# ## method

def hi(obj):
    print("Hi, I am " + obj.name)
class Robot:
    say_hi = hi  # simple and dirty way of creating method
x = Robot()
x.name = "Marvin"
Robot.say_hi(x)

# ## __int__() method

class initClass:
    def __init__(self):
        print("__init__ called inside robot line:45")
x = initClass()

# class with getter setter

class complete:
    def __init__(self,name = None,DOB = None):
        self.name = name
        self.DOB = DOB
    def get_name(self):
        return self.name
    def get_DOB(self):
        return self.DOB
    def get_id(self):
        return self.id
    def set_id(self,id):
        self.id = id
    def display(self):
        print("name:",self.name,"\nDOB:",self.DOB,"\nid:",self.id)

c = complete("roahan","02011999")
x = complete()
c.set_id(13123)
x.set_id(7867867)
c.display()
x.display()

# ## repr() and str()

class strr:
    def __init__(self,name = None,year = None):
        self.name = name
        self.year = year
    def __str__(self):
        return "Name:"+self.name+" Year:"+str(self.year)
    def __repr__(self):
        return "strr(\""+self.name+"\","+str(self.year)+")"
s = strr("roshan",1999)
s_str = str(s)
print(s_str)
s_repr = repr(s)
s2 = eval(s_repr)
print(type(s2))

# ## public protected private access modifier

class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"


# ## __del__() destructor

class destroyed:
    def __init__(self,num = None):
        self.num = num
        print("created",self.num)
    def __del__(self):
        print("destroyed",self.num)
d = destroyed(1)
d2 = destroyed(2)
d3 = d
del d
del d2
del d3

