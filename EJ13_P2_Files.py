#EJ13_P2    Files

# The open() function takes two parameters; filename, and mode.
# "r" - Read - Default value
# "a" - Append
# "w" - Write
# "x" - Create
# "t" - Text - Default value.
# "b" - Binary

# To read all the file
fileObject = open("C:\Users\ivaldez\Documents\OwnProjects\Python\Python_2/new.txt","r" );
print fileObject.read();
fileObject.close();
# To read just some bytes
fileObject = open("C:\Users\ivaldez\Documents\OwnProjects\Python\Python_2/new.txt","r" );
print "Just a part of the file: ", fileObject.read(5);
fileObject.close();
# To read a line
fileObject = open("C:\Users\ivaldez\Documents\OwnProjects\Python\Python_2/new.txt","r" );
print "Just a line of the file: ", fileObject.readline();
fileObject.close();
#NOTE: When you read a file, there is a kind of pointer that knows
#      where you are and if you keep using functions of read, the Functions
#      start where the last finished
#      This is why you MUST close and open the same file each time

#Also, you can use for reading:
fileObject = open("C:\Users\ivaldez\Documents\OwnProjects\Python\Python_2/new.txt","r" );
for i in fileObject:
    print i
fileObject.close();

#Write in a file
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content
fileObject = open("C:\Users\ivaldez\Documents\OwnProjects\Python\Python_2/new.txt","a" );
fileObject.write("Now the file has another line");
fileObject.close();

fileObject = open("C:\Users\ivaldez\Documents\OwnProjects\Python\Python_2/new.txt","r" );
print fileObject.read();
fileObject.close();

# Create a file
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist
fileObject = open("C:\Users\ivaldez\Documents\OwnProjects\Python\Python_2/new2.txt","w" );
fileObject.close();

# Delete a file
import os
if os.path.exists("C:\Users\ivaldez\Documents\OwnProjects\Python\Python_2/new2.txt"):
    os.remove("C:\Users\ivaldez\Documents\OwnProjects\Python\Python_2/new2.txt");
    print "The file was deleted"
else:
    print "The file does not exist"
# Use os.rmdir("myfolder") to delete a Folder


print "Ends here"

#fileObject = open("C:\Users\ivaldez\Documents\OwnProjects\Python\Python_2/new.txt","r" );
# Bytes to read (characters)
