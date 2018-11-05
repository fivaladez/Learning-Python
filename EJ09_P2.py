#EJ09_P2    Functions

def myFunction(x):
    return "What up " + x;

print myFunction("Ivan");

def plusTen(y):
    return y+10;

print plusTen(34);

def nameFunction(firstName = "Ivan",lastName = "Valadez"):
    print "Hello %s %s" % (firstName, lastName);

# Calls the function with default parameters
nameFunction();
# Call the function and pass the parameters
nameFunction("Francisco", "Morales");

# "*" when you do not know how many parameters you will need
# converts the variable in a tuple ()
# The first parameter can be just an element and all the others
# will be part of a tuple()
def foodFunction(foodParameter, *foodTuple):
    print "  ", foodParameter , foodTuple;

foodFunction("Apples");
foodFunction("Beef", "Oranges", "Straberry");

# converts the variable in a dictionary {}
def food2Function(**foodDictionary):
    print "  ", foodDictionary;
# Arguments MUST not be strings
food2Function(Apples = 3, Oranges = 4, Beef = 5);

def food3Function(first, *ages, **items):
    print "  ", first;
    print "  ", ages;
    print "  ", items;

food3Function("Ivan",  12,14,16,18,20,  Futbol = 100);

def example (a,b,c):
    print "  ", a+b*c;
myTuple = (1,2,3);
# To pass a tuple as argument
example(*myTuple);

def example2 (**myDictionary):
    print "  ", myDictionary;
myDictionary = {"mom": 40, "dad":45};
# To pass a dictionary as argument
example2(**myDictionary);
