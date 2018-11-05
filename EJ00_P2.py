#EJ00_P2    Numbers, Math, Variables and Casting

# The use of ";" is not neccessary but I will use it for clarity

# If you want decimals in Python 2, any number in the operation
# must have a "." -> a = 5. or 5.0

#function "input" is for getting a value from the user and return that value
a = input("Enter a number a here: ");
b = input("Enter a number b here: ");

print "\n  a =", a, "and b =", b, "\n";
c = a + b;
print "  a + b =", c;
c = a - b;
print "  a - b =", c;
c = a * b;
print "  a * b =", c;
c = a / b;
print "  a / b =", c;
c = a % b;
print "  a % b =", c;
# Operator "^" in Python 2 is  equal to "**"
c = a ** b;
print "  a ^ b =", c;
c = a // b;
print "  a // b =", c;

#To verify the type of any object in Python, use the type() function:
print "The type of var a is: ", type(a);
print "The type of var b is: ", type(b);
print "The type of var c is: ", type(c);
# Complex number
e = 5 + 3j;
print "The type of var e is: ", type(e);

# Will be only 3.0
f = int(3.4);
# Will be 3.4
f = float(3.4);
# Will be "3.4"
f = str(3.4);
