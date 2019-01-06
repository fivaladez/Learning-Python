#EJ01_P2    Modules and Functions

#Get access to module "math"
import math;

a = input("  Enter a number a here: ");
b = input("  Enter a number b here: ");

print "  a ^ b =", pow(a, b);

c = input("  Enter a number c here: ");
print "  absolute of c is:", abs(c);

print "  The function floor used for c returns:", math.floor(c);
print "  The function sqrt used c returns:", math.sqrt(c);

#Assign function "sqtr" to variable d
d = math.sqrt
#Assign value of sqtr(9) to e
e = d(9);
print "  The variable e has:", e;

# "raw_input" is for getting a string of characters
f = raw_input("  Enter your name here: ");
print "  Welcome", f;

#Line for wait for an enter from the user
raw_input("  Press<enter>");
