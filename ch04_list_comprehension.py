""" new_list = [expression(i) for i in input_list if filter(i)] """

# Fill list
input_string = "Buy 1 get 2 free"
new_list = [c for c in input_string]
print(new_list)

# Only digits
only_digit = [c for c in input_string if c.isdigit()]
print(only_digit)

# Find right most digit
last_digit = [c for c in input_string if c.isdigit()][-1]
print(last_digit)

""" 
c for c 
price*3 for price - multiplies by 3
word[0] for word - first letter of each word
"""