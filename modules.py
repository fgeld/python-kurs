#!/usr/bin/env python3
# Modules
# Modules files .py
# 
# Import the whole module
# import module_name
# module_name.method_name()
#
# Import a specific method of the module
# from module_name import method_name
# method_name()
# 
# Import multiple methods from the module
# from module_name import method_name1, method_nameN
#
# https://docs.python.org/3/library

import time
print(time.asctime())


from time import asctime
print(asctime())

from time import asctime, sleep
print(asctime())
sleep(3)
print(asctime())

import sys
for path in sys.path:
    print(path)

