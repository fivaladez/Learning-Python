# EJ23_P2    Lists comprehensions

# List comprehension:
# [expression for val in collection]

# ==========================================
# List of squares
squares = []
for i in range(1, 101):
    squares.append(i**2)
print "\n ", squares

squares2 = [i**2 for i in range(1, 101)]
print "\n ", squares2
# ==========================================
remainders5 = [x**2 % 5 for x in range(1, 101)]
print "\n ", remainders5
# ==========================================
movies = ["Star Wars", "Gandhi", "Casablanca"]

gmovies = []
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)
print "\n ", gmovies

gmovies = [title for title in movies if title.startswith("G")]
print "\n ", gmovies
# ==========================================
movies = [("Star Wars", 1950), ("Gandhi", 1960), ("Casablanca", 1970)]
pre2k = [title for (title, year) in movies if year < 2000]
print pre2k
