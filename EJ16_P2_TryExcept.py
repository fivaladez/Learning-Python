# EJ16_P2    PIP and try Except

# PIP is a package manager for Python packages, or modules if you like.
# A package contains all the files you need for a module.
# Modules are Python code libraries you can include in your project.
import camelcase
c = camelcase.CamelCase()
txt = "hello world"
# Writes a capital letter at the begining of each word
print c.hump(txt)

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code,
# regardless of the result of the try- and except blocks.

try:
    # This statement will raise an error, because x is not defined:
    print x
except NameError:
    print " Variable x is not defined"
except:
    print " Something else went wrong"


# You can use the else keyword to define a block of code
# to be executed if no errors were raised:
try:
    print "Hello"
except:
    print "Something went wrong"
else:
    print "Nothing went wrong"

# The finally block, if specified, will be executed regardless
# if the try block raises an error or not.
try:
    print x
except:
    print "Something went wrong"
finally:
    print "The 'try except' is finished"
