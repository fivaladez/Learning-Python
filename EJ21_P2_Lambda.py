# EJ21_P2  Lambda expression - Anonymous functions

# Write function to compute 3x+1
def f(x):
    return 3*x + 1
print f(2)
# lambda input1, input2, ..., inputx: return expression in one line
print lambda x: 3*x + 1
# With the above declaration we still can not use the function,
# we need a name, so, we can do the next thing:
g = lambda x: 3*x + 1
print g(2)

full_name = lambda fn, ln: fn.strip().title()+" "+ ln.strip().title()
print full_name("Ivan   ", "Valadez ")

soccer_players = ["Leonel Messi", "Cristiano Ronaldo", "Ricardo Kaka"]
print soccer_players
# in sort method, take each of the spaces from a list (one by one)
soccer_players.sort(key=lambda name: name.split(" ")[-1].lower())
print soccer_players
# Function to create functions
def build_quadratic_function(a,b,c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x:a*x**2 + b*x + c
# Option 1
f = build_quadratic_function(2,3,-5)
print f(0), f(1), f(2)
# Option 2
print build_quadratic_function(2,3,-5)(2)
