
myList = ["Hola ", "mundo", "espero", "todo", "verde"]
myList2 = []

for i in myList:
    print "This is from myList ", i
    myList2 = i
    print "\n ", myList2
print myList2

myDictionary = {"x":1, "y":2}
for key in myDictionary.keys():
    value = myDictionary[key]
    print key, "=", value
for key, value in myDictionary.items():
    print key, "=", value

x, y = 1, 1
print "\n ============= \n"
for i in range(3):
    i = i + 1
    print " ", i
    x = x * i
    y = y * i
    print " ", x
    print " ", y
