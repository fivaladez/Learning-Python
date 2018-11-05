#EJ12_P2    Import Modules
# Look for another file.py and execute what it has
import EJ09_P2
import math

def testModule():
    print "This is a test"
# First execute what the file.py has and then you can use its elements
# For example the function "myFunction()"
print EJ09_P2.myFunction("Aaron");
mF = EJ09_P2.myFunction;
print mF("Omar");

# To UPDATE the module you are using
reload(EJ09_P2)
print math.sqrt(4);
# Functions of the module
dir(math)
# Complete Information of functions in a module
help(math);
# Documentation about the module
math.__doc__
