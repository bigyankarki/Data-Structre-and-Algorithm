class HashTable:

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        hashvalue = self.hash_function(key, self.size)

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = value
        else:
            if self.slots[hashvalue] is key:
                self.data[hashvalue] = value
            else:
                next_slot = self.rehash(key, self.size)
                while self.slots[next_slot] is not None and self.slots[next_slot] is not key:
                    next_slot = self.rehash(next_slot, self.size)

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = value
                else:
                    self.data[next_slot] = value

    def hash_function(self, key, size):
        return key % size

    def rehash(self, key, size):
        return (key+1) % size

H = HashTable()

H.put(5, "bigyan")





