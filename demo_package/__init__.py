# import demo_package.submod1  # importing subpackage inside __init__.py itself
# import demo_package.submod2
# import demo_package.submod3

# from . import submod1  # importing subpackages with relative path
# from . import submod2
# from . import submod3

import demo_package.submod1  # import tree submod1-->submod2-->submod3
print("demo_package is imported")