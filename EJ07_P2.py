#EJ07_P2    if statement

thing = "Animal";
animal = "Fish";
print "  What is? ";

#The operator "is" es equal to ==
#The operator "is not" es equal to !=

if thing is "Animal":
    print "  An animal";
    if animal == "Fish":
        print " That is a fish";
        #The operator "in" look for something
        #The operator "not in" look for something that is not there
        if "F" in animal:
            print "  There is a letter F"
    elif animal == "Cat":
        print "  That is a cat";
else:
    print "  Nothing";

a = 10;
b = 15;

# Operator "and" is equal to && in C
if a > b and a < 100:
    print a;
# Operator "or" is equal to || in C
elif a < b or a != a:
    print b;
