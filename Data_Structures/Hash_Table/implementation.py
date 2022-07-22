# Implement own hash table

class HashTable(object):
    def __init__(self,size):
        self.size = size
        self.data = [None]*self.size

    def __str__(self):
        return str(self.__dict__)
        

    def _hash(self,key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % self.size
        return hash

    def set(self,key,value): #set key and value in 
        memory_loc = self._hash(key) # using hash function calculate hash value.
        if not self.data[memory_loc]:
            self.data[memory_loc] = [[key,value]]
        else:
            self.data[memory_loc].append([key,value])
        return self.data

    def get(self,key):
        pass


my_table = HashTable(50)
# print(my_table._hash('grapes'))
my_table.set('grapes', 10000)
# my_table.get('grapes')
# my_table.set('apples', 9)
# my_table.get('apples')
# key = 'grapes'
# has = 0
# print(has)
# for i in range(len(key)):
#     has = (has + ord(key[i]) * i) % 50
# print(has)


