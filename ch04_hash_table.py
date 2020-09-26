""" Hash Table - stores data in slots/buckets.
A hash takes a number or characters and performs a arithmetic or logical transformation to produce a value.
A simple hash is modulo division.
 Hash tables should be the length of prime numbers. Python Dictionaries use Hash Tables."""

# makeup list of IP addresses
sockets = {'T1R': '10.0.0.142:5002', 'TR2': '192.168.3.55:5002'}
print(sockets)
sockets['TR3'] = '10.250.6.23:5002'
sockets['TR4'] = '10.250.7.24:5002'
sockets['CL3'] = '10.250.6.30:5002'
print(sockets)
sockets['TR4'] = '10.250.6.24:5002'
print(sockets)
del sockets['CL3']
print(sockets)
