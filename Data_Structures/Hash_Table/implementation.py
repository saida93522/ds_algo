
class HashTable(object):
    """ Implementing Custom HashTable. """
    
    def __init__(self,size):
        self.size = size
        self.bucket = [None] * self.size

    def __str__(self):
        return str(self.__dict__)
        

    def _hash(self,key):
        """ returns: Custom hash function to return hashed value of given key. """

        hash = 0
        for i,e in enumerate(key):
            # looping through key, get the unicode num of the char string
            hash = (hash + ord(e) * i) % self.size
        return hash

    def set(self,key,value):
        """ returns: sets key and value inside bucket[hash_index]. """
        hash_index = self._hash(key)
        if not self.bucket[hash_index]:
            self.bucket[hash_index] = [[key,value]]
        else:
            # if key already exists, update the value
            for items in self.bucket[hash_index]:
                if key == items[0]:
                    items[1] = value
                    return 
            # add new [key,value] to the bucket    
            self.bucket[hash_index].append([key,value])
        # return "You data has been stored!"
    
    def get(self,key):
        """ returns: gets the value of given key. """
        hash_index = self._hash(key)
        if hash_index:
            #if hash index exist loop through the arrays inside of it to find the array that contains our key.
            for hash_i,list_items in enumerate(self.bucket[hash_index]):
                if key == list_items[0]:
                    # if there is a matching value in list_items[key], return the second index = value
                    return list_items[1]
        else:
            return None

    def keys(self):
        """returns: A list containing all the keys. """
        key_items = []
        for i,bucket_items in enumerate(self.bucket):
            if bucket_items: # if items exist
                # loop through all the [key,value] list inside each bucket_items, and return its key
                # this return all the keys inside lists incase of collission
                for j in bucket_items:
                    key_items.append(j[0])
        return key_items

    def values(self):
        """returns: A list containing all the values. """
        value_items =[]
        for i,e in enumerate(self.bucket):
            if e:
                # in case of collision,return value of all the lists
               for j in e:
                   value_items.append(j[1])
        return value_items

my_table = HashTable(2)
set_grapes = my_table.set('grapes', 10)
set_grapes = my_table.set('grapess', 100)
set_cherries = my_table.set('cherries', 30)
set_apples = my_table.set('apples', 20)
set_oranges = my_table.set('oranges', 5)

# my_table.get('grapes')
# my_table.set('apples', 9)
# my_table.get('apples')
print(my_table.keys())
print(my_table.values())