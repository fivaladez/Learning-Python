#EJ08_P2    Loops

b = 1;

while b <= 10:
    print "  ", b;
    b += 1;

myList = ["Guadalajara", "DF", "Monterrey"];

for i in myList:
# Traditionaly you will do this in C -> print "You are in ", myList[i];
# But in Python, the variable i gets the value of list and it increments
# So, this is what you do
    print "  You are in ", i;

myDictionary = {"Mexico":10, "Germany":12 , "France":15};
for s in myDictionary:
    # "s" will print the key and "myDictionary[s]" will print the value
    print "  ", s, myDictionary[s];

while 1:
    name = raw_input("  Enter the password: ");
    if name == "123":
        print "  Password correct"
        # We use break to end the loop
        break;
        # We can use "continue" to skip the current iteration
        # and go to the next one
    else:
        print "  Password incorrect"
