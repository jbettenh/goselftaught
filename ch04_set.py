# Set can't contain duplicate items

def return_duplicates(a_list):
    dups = []
    a_set = set()

    for item in a_list:
        length_one = len(a_set)
        a_set.add(item)
        length_two = len(a_set)
        if length_one == length_two:
            dups.append(item)

    return dups


a_list = ['Susan Adams', 'Kwame Goodall', 'Jill Hampton', 'Susan Adams']
dups = return_duplicates(a_list)
print(dups)