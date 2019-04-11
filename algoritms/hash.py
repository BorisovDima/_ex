
class Hash:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def put(self, key, val):
        hash_ = self.do_hash(key)
        if self.slots[hash_] is None:
            self.slots[hash_] = key
            self.data[hash_] = val
        elif self.slots[hash_] == key:
            self.data[hash_] = val
        else:
            while True:
                hash_ = (hash_ + 1) % self.size
                if self.slots[hash_] is not None or self.slots[hash_] != key:
                    self.slots[hash_] = key
                    self.data[hash_] = val
                    return


    def get(self, key):
        hash_ = self.do_hash(key)
        if self.slots[hash_] == key:
            return self.data[hash_]
        count = 0
        while True:
            hash_ = (hash_ + 1) % self.size
            if self.slots[hash_] == key:
                return self.data[hash_]
            count += 1
            if count > self.size:
                raise ValueError('NOT')

    def __str__(self):
        return str((self.data, self.slots))


    def do_hash(self, key):
        return key % self.size



d = Hash(11)

d.put(11277, 'CAT')

d.put(44, 'DOG')
print(d.get(44))

d.put(99, 'SOM')

print(d.get(99))

print(d)

d.put(22, 'DDDD')

print(d.get(22))

print(d)