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


# ## more on class instance

class C:
    count = 0
    def __init__(self):
        C.count+=1
        print("Instance created",C.count)
    def __del__(self):
        C.count -=1
        print("Instance removed",C.count)
c1 = C()
c2 = C()
c3 = c1
del c1
del c2
del c3

# ## @staticmethod to create static method

class static:
    def __init__(self):
        print("Created static instance")
    @staticmethod
    def thisMethodIsStatic():
        print("This is static method")
    def thisIsNotStaticMethod():
        print("Created non static method")
static.thisMethodIsStatic()  # accessing from class
x = static()  # accessing from instance of class
x.thisMethodIsStatic()
static.thisIsNotStaticMethod()  # only accessed using class
# x.thisIsNotStaticMethod()  # error while accessing because self is passed by default

# ## @classmethod to define class method

class Robot:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1
    @classmethod
    def RobotInstances(cls):
        return cls, Robot.__counter
r = Robot()

print(r.RobotInstances())

# more practical example  using inheritance

class Pets:
    name = "pet animals"
    @classmethod
    def about(cls):
        print("This class is about {}!".format(cls.name))
class Dogs(Pets):
    name = "'man's best friends' (Frederick II)"
class Cats(Pets):
    name = "cats"
p = Pets()
p.about()
d = Dogs()
d.about()
c = Cats()
c.about()


# ## getter and setter

#1 JAVA way of creating getter setter

class JAVA:
    def __init__(self,x):
        self.__x = x
        # self.set_x(x)  # alternatively
    def get_x(self):
        print(self.__x)
    def set_x(self,x):
        self.__x = x
j1 = JAVA(12)
j1.get_x()
j1.set_x(23)
j1.get_x()

#2 pythonic way (without encapsulation)

class PYTHON:
    def __init__(self,x):
        self.x = x
p1 = PYTHON(12)
print(p1.x)
p1.x = 23
print(p1.x)

#3 more pythonic way (using @property @f.setter )

class MOREP:
    def __init__(self,x):
        self.x = x
    @property
    def x(self):
        print(self.__x)
    @x.setter
    def x(self,x):
        self.__x = x
m1 = MOREP(12)
m1.x
m1.x = 23
m1.x

#4 similar code without decorator with property(getter,setter)

class MOREP2:
    def __init__(self,x):
        self.x = x
    def __x_get(self):  # we can now make them private also
        print(self.__x)
    def __x_set(self,x):
        self.__x = x
    x = property(__x_get,__x_set)
m12 = MOREP2(112)
m12.x
m12.x = 231
m12.x