class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return  self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


aq = Queue()
print(aq.is_empty())

for i in range(11):
    aq.enqueue(i)

print(aq.items)

for i in range(aq.size()):
    print(i)