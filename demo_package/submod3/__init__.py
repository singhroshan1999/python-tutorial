# from .. import submod1  # creating import cycle  DONT WORK

# from . import mod31,mod32,mod33  # import all module

__all__ = ['mod31','mod32','mod33']  # this import submodule

print("submod3 is imported")