# EJ04_P2    Methods
# Method = An action of what you want to do

# My object
myList = [21, 21, "Hello", "Bye"]
print "\n  Your list", myList[:]
# What a want to do
# Add an element in the list
myList.append(45)
myList.append("Hey")
print "  Your new list", myList[:]
print "  There are", myList.count(21), "\"21\" in the list"
print "  There are", myList.count(60), "\"60\" in the list"
# Add elements in the list
myList2 = [66, 77, 88]
myList.extend(myList2)
print "  Your new list", myList[:]

# Returns the position in a list if there is any
print "  \"Hello\" is in the position ", myList.index("Hello")
# Add a value in your list
myList.insert(2, "Ivan")
print "  \"Ivan\" is now in the position 2: ", myList[:]
# Remove elements
myList.pop(2)  # Also return the value that removes
print "  Second position was deleted: ", myList[:]

myList.remove("Hello")
print "  \"Hello\" was removed: ", myList[:]

myList.sort()
print "  The new list is: ", myList[:]

myList3 = ["  Hello", " all", " you"]
myStringToJoin = " Mexico is great "
# This returns the list with the string pasted each one word
# But the real list is not modified
print myStringToJoin.join(myList3)
# Returns all letters lower in a single string
print myStringToJoin.lower()
# Returns the message and its replacement in a single string
print myStringToJoin.replace("great", "awesome")
# NOTE: Just return the string, the string is not modified
