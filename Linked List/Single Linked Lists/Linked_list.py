class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return "The list is empty." if self.head is None else "The list is not empty."

    def add(self, item):
        tmp = Node(item)
        tmp.set_next(self.head)
        self.head = tmp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        count = 0
        found = False
        while current is not None and not found:
            count += 1
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return "Item found at " + str(count) if found else "Item not found."

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found and current is not None:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if current is None:
            print("Item cannot be found")
        elif previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(Node(item))

    def pop(self):
        current = self.head
        previous = None
        while current.get_next() is not None:
            previous = current
            current = current.get_next()
        previous.set_next(None)

    def insert(self, item, position):
        current = self.head
        previous = None
        count = 0
        while current.get_next() is not None and count != position:
            count += 1
            previous = current
            current = current.get_next()

        temp = Node(item)
        previous.set_next(temp)
        temp.set_next(current)


my_list = UnorderedList()
my_list.add(20)
my_list.append(30)
my_list.add(10)
my_list.append(50)

print(my_list.size())
print(my_list.search(10))
print(my_list.search(20))
print(my_list.search(30))
print(my_list.search(50))

my_list.insert(40, 4)
print(my_list.search(40))
print(my_list.search(50))
