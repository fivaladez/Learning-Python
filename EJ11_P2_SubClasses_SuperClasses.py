#EJ11_P2    Object Oriented - subClasses and superClasses

# SuperClass
class parentClasss:
    var1 = "This is var1"
    var2 = "This is var2 in parentClass"

# SubClass
class childClass(parentClasss):
    # Overwrite this var in this class
    var2 = "This is var2 in childClass"

myObject1 = parentClasss();
print "  ", myObject1.var1;
# You can acces to upper layer class "parentClasss"
myObject2 = childClass();
print "  ", myObject2.var1;

print "  ", myObject1.var2;
print "  ", myObject2.var2;
#==================================================
# Multiple inhertance
class mom:
    mom = "Im mom"

class dad:
    dad = "Im dad"

# child class inherit/hereda the elements of classes mom and dad
class son(mom,dad):
    son = "Im son"

myObject3 = son();
print "  ", myObject3.mom;
print "  ", myObject3.dad;
print "  ", myObject3.son;
#==================================================
# Constructor

class new:
    def __init__(self):
        print "  This is the contructor of class new: "
# Automatically calls the constructor
myObject4 = new();
