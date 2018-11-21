class HashTable:
    def __init__(self,maxsize=10):
        self.size = maxsize
        self.keys = [None] * maxsize
        self.vals = [None] * maxsize

    def _hashFunc(self, key):
        return(key % self.size)

    def insert(self, key, val):
        bucket = self._hashFunc(key)
        if self.keys[bucket] is None:
            self.keys[bucket] = key
            self.vals[bucket] = val
            print('assigned in bucket ',bucket)
            return(0)
        else:
            for i in range (self.size-1):
                if (bucket+i) < (self.size-1):
                    if self.keys[bucket + i] is None:
                        self.keys[bucket+i] = key
                        self.vals[bucket+i] = val
                        print('assigned in bucket ',bucket+i)
                        return(0)
                else:
                    if self.keys[(bucket + i) % self.size] is None:
                        self.keys[(bucket + i) % self.size] = key
                        self.vals[(bucket + i) % self.size] = val
                        print('assigned in bucket ', (bucket + i) % self.size)
                        return(0)
        print("hash table full :(")
        return(1)

    def find(self, key):
        pass

    def delete(self, key):
        pass


if __name__ == "__main__":
    test_hash = HashTable()
    print(test_hash, test_hash.size, test_hash.keys, test_hash.vals)
    test_hash.insert(1,'a')
    test_hash.insert(2,'b')
    test_hash.insert(3,'c')
    test_hash.insert(4,'d')
    test_hash.insert(5,'e')
    test_hash.insert(6,'f')
    test_hash.insert(7,'g')
    test_hash.insert(8,'h')
    test_hash.insert(9,'i')
    test_hash.insert(10,'j')
    test_hash.insert(11,'k')
