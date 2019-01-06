# EJ25_P2  Sorting

# x.sort(key=None, reverse=False)
# Sorting alphabetical
earth_methals = ["Beryllium","Magnesium","Calcium","Strotium","Barium","Radium"]

earth_methals.sort() # Alfabeticaly by default
print earth_methals

earth_methals.sort(reverse=True)
print earth_methals

planets = [
("Mercury", 2440, 5.43, 0.395),
("Venus", 6052, 5.24, 0.723),
("Earth", 6378, 5.52, 1.000),
]
size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)
print planets

# sorted(iterable, /, *,key=None, reverse=False )
# This is to create a copy os the sorted list
sorted_earth_methals = sorted(earth_methals)
print sorted_earth_methals

# To sort a Tuple
# The return value is a list and the original tuple is not modified
data = (7,2,5,6,9,2,6,3,8)
sorted_data = sorted(data)
print sorted_data

print sorted("Alphabetical")
