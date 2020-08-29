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

# Find Intersections
def intersection(current_winners, most_common):
    list3 = [value for value in current_winners if value in most_common]
    return list3
current_winners = [2, 43, 48, 62, 64, 28, 3]
most_common = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]
print(intersection(current_winners, most_common))

# Python built in function
set1 = set(current_winners)
set2 = set(most_common)
print(set1.intersection(set2))





