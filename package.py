# import demo_package  # importing package

# import demo_package.submod1  # importing subpackages
# import demo_package.submod2
# import demo_package.submod3


from demo_package import *  # trying to import all submodule and subpackage
from demo_package.submod1 import *  # import submodule


mod11.func()  # calling a function

print(dir()) # --> ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
