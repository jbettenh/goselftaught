""" Dictionaries are mutable. They don't store data in order, benefit is mapping of key and value pairing. Dictionary
keys must be immutable. Therefore Tuples can be keys but not lists. Can use keyword in for keys, but not values."""

my_dict = dict()
print(my_dict)

fruits ={"Apple": "Red", "Banana": "Yellow"}
print(fruits)

facts = dict()
facts["founded"] = 1776

print(facts["founded"])

del facts["founded"]
