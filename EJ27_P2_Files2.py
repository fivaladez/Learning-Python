# EJ27_P2 Files2
import os

print os.path.dirname(os.getcwd())
print os.getcwd()
print os.path.dirname(os.getcwd() + os.sep + "EJ27_P2_Files2.py")

# There are 2 kind of file: Text and Binary
f = open("guido_bio.txt")
text = f.read()
f.close()
print text, "\n ========================="

# This way, the file is close automatically
with open("guido_bio.txt") as fobj:
    bio = fobj.read()
print bio, "\n ========================="

# Better choice, you can handle if the file does not exist
try:
    with open("guido_bio.txt") as f:
        text2 = f.read()
except FileNotFoundError:
    text2 = None
print text2
# Write mode
oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Artic"]
with open("oceans.txt", "w") as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")
# Append mode
# with open("oceans.txt", "a") as f:
#    print 23*"=", file=f
#    print "These are the 5 oceans.", file=f
