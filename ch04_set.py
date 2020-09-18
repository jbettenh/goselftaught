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


# LeetCode Remove Duplicates from Sorted Array
def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1

    pointer1 = 0

    for pointer2 in range(1, len(nums)):
        if nums[pointer1] != nums[pointer2]:
            print(f'Pointer 1 ({pointer1} value: {nums[pointer1]}) != to Pointer 2 ({pointer2} value: {nums[pointer2]})')
            pointer1 += 1
            nums[pointer1] = nums[pointer2]
            print(f'update: {num_list}')
        else:
            print(f'Pointer 1 ({pointer1} value: {nums[pointer1]}) = to Pointer 2 ({pointer2} value: {nums[pointer2]})')

    return pointer1 + 1


num_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(f'original: {num_list}')
print(f' The length of unqiue values: {removeDuplicates(num_list)}')
print(f'modified: {num_list}')

