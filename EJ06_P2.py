#EJ06_P2    Dictionaries {}
# Keys:Value
#Key or value can be anything(a list, a tuple, a string, a number, a doctionary)
myDiccionary = {"Berlin" : "Germany", "Spain" : "Madrid"};

print "\n  This is my complete dictionary: ", myDiccionary;
# Use the key intead of the position to have access to its members
print "  This is a member of my dictionary: ", myDiccionary["Berlin"];

myDiccionary2 = myDiccionary.copy();
print "  This is a copy of my first dictionary: ", myDiccionary2;

#Returns True or False
print "  Does the dictionary have the key \"Spain\"? ", myDiccionary.has_key("Spain");
print "  Does the dictionary have the key \"Mexico\"? ", myDiccionary.has_key("Mexico");

print "  The keys of my dictionary are: ", myDiccionary.keys();
print "  The values of my dictionary are: ", myDiccionary.values();


# Clear all members of the dictionary
myDiccionary.clear();
print "  This is my dictionary cleared: ", myDiccionary;
