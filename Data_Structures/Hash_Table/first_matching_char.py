# Given an array return the first recurring character
# Example 1
# input: array = [2,5,1,2,3,5,1,2,4]
# output: 2

# Example 2
# input: array = [2,1,1,2,3,5,1,2,4]
# output: 1

# Example 3
# input: array = [2,3,4,5]
# output: None

# Solution: #1 Brute force approach where we use nested loops and compare every element. Time complexity of O(n^2) because of the nested loop. Space complexity of O(1) since we are not allocating new memory.


def find_duplicate_naive(arr):
    last = arr[-1]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return arr[j]
            if arr[j] == arr[j+1]:
                return arr[j]
    return None if len(arr) < 2 else None 


            

find_duplicate_naive([2,5,1,2,3,5,1,2,4]) # 2
find_duplicate_naive([2,1,1,2,3,5,1,2,4]) # 1
find_duplicate_naive([2]) # None

# Solution: #2 Create a dictionary and keep track of elements that we already seen.
# Time complexity of O(n) since we are looping through the array once. Space complexity of O(n) since we are storing all the elements that are unique inside the dictionary.

def find_duplicate(arr):
    if len(arr) < 2:
        return None
    
    storage = dict()
    for i in arr:
        if i in storage:
            return i
        else:
            storage[i] = 1
    return None



find_duplicate([2,5,1,2,3,5,1,2,4]) # 2 
find_duplicate([2,1,1,2,3,5,1,2,4]) # 1
find_duplicate([2,3,4,5]) # None
find_duplicate([2]) # None

