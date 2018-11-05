#EJ14_P2    Dates

#You MUST import the moduel "datetime"
import datetime

x = datetime.datetime.now();

print x;
print x.year;
# ".strftime()" take as paremeter the fromat to return the string
print x.strftime("%A");
# "%A" = Name of week day
# "%B" = Name of Month
# "%a" = Name of week day abreviation
# "%b" = Name of Month abreviation
# For more information: "https://www.w3schools.com/python/python_datetime.asp"

#Create a date object
y = datetime.datetime(2020, 5, 17);
print y;
