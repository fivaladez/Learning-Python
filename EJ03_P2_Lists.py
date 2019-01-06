#EJ03_P2    Lists[]

myList = ["  Ivan", "Valadez", "is" , 22];
print "  Hello", myList;
print "  Hello", myList[:];
#From position 0 until position 2 because the 3 count as 1,2,3 = 0,1,2
print "  Hello", myList[0:3];#Slicing
print "  Hello", myList[:3];
print "  Hello", myList[0:];
#[Begining position:End position:Increment of count]
print "  Hello", myList[1:4:2];
print "  Hello", myList[::-2];
#Start the count as 0, 1, 2, ..., n
print "  Hello", myList[3];
#Also, it is allowed to refer to negative positions. Starts from the end
print "  Hello", myList[-2];

#Change the value in a list
myList[3] = 23;
print "  Now the list contains", myList[:];
del myList[3];
print "  I just delete the position 3, see: ", myList[:];
#You also can delete usisng :
myList[1:3] = [];
print "  The new list is: ", myList[:];

FamilyList = ["Mom", "Dad", "Son", "Daughter"];
print "  Is \"Son\" in the family list? ", "Son" in FamilyList;
# "len() return the length of the list"
print "  Whats the length of my family? ", len(FamilyList);
# Look for the bigest value in the list, but just check, in case that is a text,
# the fist character in the ""
print "  Whats larger value of my family? ", max(FamilyList);
# Look for the lowest value in the list, but just check, in case that is a text,
# the fist character in the ""
print "  Whats larger value of my family? ", min(FamilyList);

#For convert into a list
varString = "Hola";
print "  This is a string: ", varString;
print "  This is a list: ", list(varString);#Casting
