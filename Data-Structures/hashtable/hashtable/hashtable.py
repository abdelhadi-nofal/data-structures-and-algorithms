from linkedlist import LinkedList


class HashTable:
    
    def __init__(self, size=1024):
        self.size = size
        self.map = [None] * size

    
    def hash(self, key):
        sum_of_asccii = 0
        for ch in key:
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp_value = sum_of_asccii * 19
        hashed_key = temp_value % self.size
        return hashed_key

        
    def add(self, key, value):

        hashed_key = self._hash(key)

        if not self.map[hashed_key]:
           self.map[hashed_key] = LinkedList()
        
        self.map[hashed_key].append([key, value])


    def get(self, key):
        hashed_key = self._hash(key)
        bucket = self.map[hashed_key]

        if bucket:
            current = bucket.head

            while current:
                if current.data[0] == key:
                    return current.data[1]
                current = current.next


    def contains(self, key):
        hashed_key = self._hash(key)

        if not self.map[hashed_key]:
            return False
        else:
            bucket = self.map[hashed_key]
            current = bucket.head

            while current:
                if current.data[0] == key:
                    return True
                current = current.next
   
