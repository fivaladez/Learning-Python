#EJ14_P2    Dates

#You MUST import the moduel "datetime"
import datetime
#help(datetime.date)

gvr = datetime.date(1956, 1, 31)
print gvr
print gvr.year
print gvr.month
print gvr.day

mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)
print "\n ", mill + dt
print "\n ", gvr.strftime("%A, %B %d, %Y")

message = "GVR was born on {:%A, %B %d, %Y}."
print "\n ", message.format(gvr)

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
print launch_date
print launch_time
print launch_datetime

moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print "\n=== ",moon_landing_datetime, " ===\n"

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
