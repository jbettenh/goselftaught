class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)


stack = Stack()
print(stack.is_empty())

stack.push(1)
print(stack.is_empty())

for i in range(1, 11):
    stack.push(i)

print(stack.items)
print(stack.size())

print(stack.pop())

print(stack.items)


# Reverse String
reverso = Stack()

for c in "yesterday":
    reverso.push(c)

reversed_String = ""
for s in range(len(reverso.items)):
    reversed_String += reverso.pop()

print(reversed_String)

# Reverse List, Use a stack to create a new list with the items in the following list reversed: [1, 2, 3, 4, 5].
dirty_dishes = [1, 2, 3, 4, 5]
clean_dishes = []

dishes = Stack()

for item in dirty_dishes:
    dishes.push(item)

print(dishes.items)

for item in range(len(dishes.items)):
    clean_dishes.append(dishes.pop())

print(clean_dishes)





