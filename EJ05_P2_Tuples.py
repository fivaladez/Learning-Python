# EJ05_P2    Tuples ()
# Tuples are like Lists but they can not be changed
# Are more efficient that lists in terms of performance (speed)
# NOTE: This document uses the same examples that "EJ03_P2 List[]"

myTuple = ("  Ivan", "Valadez", "is", 22)
print "  Hello", myTuple
print "  Hello", myTuple[:]
# From position 0 until position 2 because the 3 count as 1,2,3 = 0,1,2
print "  Hello", myTuple[0:3]  # Slicing
print "  Hello", myTuple[:3]
print "  Hello", myTuple[0:]
# [Begining position:End position:Increment of count]
print "  Hello", myTuple[1:4:2]
print "  Hello", myTuple[::-2]
# Start the count as 0, 1, 2, ..., n
print "  Hello", myTuple[3]
# Also, it is allowed to refer to negative positions. Starts from the end
print "  Hello", myTuple[-2]

# NOTE: Change and delete the value in a tuple is not possible

FamilyTuple = ("Mom", "Dad", "Son", "Daughter")
print "  Is \"Son\" in the family tuple? ", "Son" in FamilyTuple
# "len() return the length of the list"
print "  Whats the length of my family? ", len(FamilyTuple)
# Look for the bigest value in the list, but just check, in case that is a text,
# the fist character in the ""
print "  Whats larger value of my family? ", max(FamilyTuple)
# Look for the lowest value in the list, but just check, in case that is a text,
# the fist character in the ""
print "  Whats larger value of my family? ", min(FamilyTuple)

# For convert into a tuple
varString = "Hola"
print "  This is a string: ", varString
print "  This is a tupla: ", tuple(varString)  # Casting

empty_tuple = ()
# This line is just a string, to make it a tuple you have to add a ,
#test1 = ("a")
# This is a tuple with only one member
test1 = ("a",)
test2 = ("a", "b")
test3 = ("a", "b", "c")

print empty_tuple
print test1
print test2
print test3
