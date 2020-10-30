# Carlos Perez
# Student ID: 000819792
class HashTable:
    # Hashtable made to a capacity of 99 to avoid any collisions
    def __init__(self, capacity = 99):
        self.table = []
        for i in range(capacity):
            self.table.append([])

    # put() that allows the packages to be placed into buckets
    def put(self, package):
        key = package.package_id
        index = hash(key) % len(self.table)
        self.table[index].append(package)

# Hashtable initiated for later retrieval
table = HashTable()


