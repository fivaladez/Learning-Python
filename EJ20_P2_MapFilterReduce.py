# #EJ20_P2  Map, Filter and Reduce functions
# Map
# NOTES:
#       -Data: a1, a2, ..., an
#       -Function f
#       -map(f, data):
#           Returns iterator over
#           f(a1), f(a2), ..., f(an)
temps = [("Berlin", 29),("Cairo", 36),("Buenos Aires", 19)]
c_to_f = lambda data: (data[0], (9/5) * data[1] + 32)
print list(map(c_to_f, temps))
# =================================================
# Filter
# NOTES:
#       -Data: a1, a2, ..., an
#       -Function f
#       -map(f, data):
#           Returns iterator over
#           f(a1), f(a2), ..., f(an)
#           where the result of f was true
data = [1.3,2.7,0.8,4.1,4.3,-0.1]
avg = 2.0
print list(filter(lambda x: x > avg, data))

countries = ["Brazil", "", "Argentina", "", "Mexico"]
print list(filter(None, countries))
# In Python, False = "", 0, 0.0, 0j, (), [], {}, False, None

# =================================================
# Reduce
# NOTES:
#       -Data: a1, a2, ..., an
#       -Function f(x, y)
#       -reduce(f, data):
#           Step 1: val1 = f(a1, a2)
#           Step 2: val2 = f(val1, a3)
#           Step 3: val3 = f(val2, a4)
#           ...
#           Step n-1: valn-1 = f(valn-2, an)
#           Return valn-1
from functools import reduce
data = [2,3,5,7,11,13,17,19,23,29]
multiplier = lambda x, y: x*y
print reduce(multiplier, data)

product = 1
for x in data:
    product = product * x
print product
