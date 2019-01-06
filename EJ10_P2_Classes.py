#EJ10_P2    Object Oriented - Classes

# Create a class
class exampleClass:
    eyes = "Blue";
    age = 22;
    # The first parameter MUST be self to refers to the object using this class
    def thisMethod(self):
        return "Hey this method worked"

# This is called an Object
# Assign the class to an a variable to the class
exampleObject = exampleClass();

# Calling methods from our Object
# Members from our class
print "  ", exampleObject.eyes;
print "  ", exampleObject.age;
print "  ", exampleObject.thisMethod();

class className:
    def createName(self, name):
        # Create a var called name and assign the parameter name
        # This is because the variable is inside a function
        self.name = name;
    def displayName(self):
        return self.name;
    def saying(self):
        print "  Hello %s" % self.name;

first = className();
second = className();

first.createName("Ivan");
print "  ", first.displayName();
first.saying();
print "  ", first.name;
