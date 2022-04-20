""" Implementing implement list."""

class MyList(object):
    def __init__(self):
        self.length = 0 
        self.data = {} #initialize the data of the array using an empty dictionary. The keys will correspond to the index and the values to the data

    def __str__(self):
        return str(self.__dict__)

    def get(self,index):
        """ :param This method takes in the index of the element
            :returns the value element in O(1) time. 
        """
        return self.data[index]
    
    def push(self,item):
        """ :param This method adds item to the end of the array 
        """
        self.length += 1
        self.data[self.length - 1] = item
        
    def pop(self):
        """ :param This method removes last item of the array 
            :returns the popped item in O(1)
        """
        last_item = self.data[self.length -1] # store data before del
        del self.data[self.length -1] #del last item
        self.length -= 1 #decrement array
        return last_item 
       
    def insert(self,index,item):
        """ :param This method adds item at the specified position 
        """
        self.length += 1 #create space for new item
        for i in range(self.length-1, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = item

    def delete(self,index):
        deleted_item = self.data[index]
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length -1]
        self.length -= 1
        return deleted_item



arr = MyList()
my_lists = [1,2,3,4,5]

for i in my_lists:
    arr.push(i) # {'length': 5, 'data': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}}
    
arr.push(6) # {'length': 6, 'data': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6}}
arr.push(7) # {'length': 6, 'data': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6}}

arr.pop() #{'length': 5, 'data': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}}
print(arr.get(2)) # 3



print(arr.delete(2)) # 3

arr.insert(4,5)




print(arr)

