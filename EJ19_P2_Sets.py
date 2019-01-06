#EJ19_P2    Sets
# Storage info but the order doesn't matter
# Also, sets can not contain duplicated values
# If you try to remove a value that is not in the set, you will receive a keyerror
# You can try using discard, which does nothing if the value is not in the set

example = set()
#help(set)
example.add(42)
example.add(False)
example.add(3.1416)
example.add("Hello")

#It is not goint to be saved
example.add(42)
print example
print len(example)

example.remove(42)
print example
print len(example)

example.discard(50)
print example
print len(example)
