# EJ02_P2    Strings
# For strings you can use "" or ''
# In a string, if you use \, the next value will not be interpreted
# just printed
print "  Ivan said: \"Hello\" to me"

Name = raw_input("  Enter your name: ")
lastName = raw_input("  Enter your last name: ")

# To join a string with other string use "+"
CompleteName = Name + " " + lastName
print "  Welcome", CompleteName
# Times to add the same string
print "  Welcome", CompleteName * 3
# Look for a value "in"
print "  Is an v in your name? ", "v" in Name

# To use the function "str()" to add a numeric value to a string
age = str(22)  # Casting
age2 = 23
print "  Your age is " + age
print "  Your age is " + `age2`

# "%s" is going to be replaced
varA = "  Hello %s, how is your %s?"
varB = ("Ivan", "head")
# Works only with tuples() and not with Lists[]
print varA % varB

varC = "  Hello! How are you?"
print varC
# Same expression .find = .index
print varC.find("are")
print varC.index("are")

large_string = """I'm going to tell you what happend to me last week:
                  I was driving to my job and then...
                  end of the story"""
print large_string
