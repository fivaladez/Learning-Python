# EJ15_P2    JSON

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

# Import module for working with JSON data
import json

# Convert from JSON to Python
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print "\n  This is an element of the JSON string: ", y["age"]

# Convert from Python to JSON
# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print "\n  This is the dictionary in a JSON format: ", y
print "\n  This is the dictionary in a Python format: ", x

# Convert Python objects into JSON strings,
print json.dumps({"name": "John", "age": 30})  # Dictionary
print json.dumps(["apple", "bananas"])  # List
print json.dumps(("apple", "bananas"))  # Tuple
print json.dumps("hello")  # String
print json.dumps(42)  # Int
print json.dumps(31.76)  # Float
print json.dumps(True)  # Boolean
print json.dumps(False)  # Boolean
print json.dumps(None)  # Boolean

z = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
# Use the indent parameter to define the numbers of indents
# Use the separators parameter change the default separator:
print json.dumps(z, indent=4, separators=(". ", " = "))
print json.dumps(z, indent=4, sort_keys=True)
