class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, string: str):
        tot = 0
        for char in string:
            tot += ord(char)
        return tot
    
    def add(self, key, value):
        hash_key = self.hash(key)
        if hash_key not in self.collection.keys():
            self.collection[hash_key] = {key: value}
        else:
            self.collection[hash_key][key] = value
    
    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection.keys():
            if len(self.collection[hash_key]) > 1:
                self.collection[hash_key].pop(key, None)
            else:
                self.collection.pop(hash_key, None)
        else:
            return None
    
    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection.keys():
            return self.collection[hash_key][key]
        else:
            return None
