class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, word):
        hashed_value = 0
        for letter in word:
            hashed_value += ord(letter)
        return hashed_value
    
    def add(self, key, value):
        computed_hash = self.hash(key)
        new_dict = self.collection.get(computed_hash, {})
        new_dict[key] = value
        self.collection[computed_hash] = new_dict

    def remove(self, key):
        computed_hash = self.hash(key)
        if self.collection.get(computed_hash, False):
            self.collection[computed_hash].pop(key, None)

    def lookup(self, key):
        computed_hash = self.hash(key)
        return (self.collection.get(computed_hash, {})).get(key, None)


