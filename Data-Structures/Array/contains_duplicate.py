import time

#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#Example 1:
#Input: [1,2,3,1]
#Output: true
#Example 2:
#Input: [1,2,3,4]
#Output: false

#Solution:0 naive approach.The runtime is directly proportional to the squared size of the input data set.

def brute_force(arr):
    if len(arr) < 2:
        return False
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] == arr[i]:
                return True  
    return False

#Time Complexity - O(n^2)

# result = brute_force( [3,2,3,1])
# print(result)


#Solution:1 # check if a list contains duplicate by adding the list content in set. set contains only unique elements, so duplicate will be accepted

def check_duplicate(arr):
    
    if len(arr) != len(set(arr)):
        return True
    else:
        return False

# result1 = check_duplicate( [4,2,3,1])
# print(result1)



#Solution:2 # check if a list contains duplicate by counting it reoccurrence 
def check_duplicate2(arr):
    for i in arr:
        if arr.count(i) >= 1:
            return True
    return False

# result2 = check_duplicate2( [4,2,3,1])
# print(result2)



#Solution:3 sort the array, that way if there are duplicates then they would be adjacent. therefore we can iterate though the array once and check if any consecutive elements are same

def check_duplicate3(arr):
    arr.sort() #O(nlogn)
    for i in range(len(arr)):
        if arr[i] == arr[i-1]:
            return True
    return False
#Time Complexity - O(nlogn)
#Space Complexity - O(1)

# result3 = check_duplicate3( [4,2,4,3,1])
# print(result3)


def smart_duplicate_search(array):
    dictionary = dict()
    if len(array)<2:
        return False
    else:
        for i in range(len(array)):
            if array[i] in dictionary:
                return True
            else:
                dictionary[array[i]] = True
    return False

# ta = time.time()
# smart_duplicate_search([4,2,4,3,1])
# tb = time.time()
# print(ta - tb)


#Solution:4 sets hold a collection of unique keys.we can loop through the array once, and the check if the current item is in the set. if true then we have duplicate elements if not true add the item to set.
#


def check_duplicate4(arr):

    
    if len(arr) < 2:
        return False
    unique_arr = dict()
 
    for i in arr:
        if unique_arr.get(i):
            return True
        else:
            unique_arr[i] = 1
    return False

# t4a = time.time()
# check_duplicate4([4,2,4,3,1])
# result4 = check_duplicate4( [2,4,3,1])
# print(result4)
# t4b = time.time()
# print(t4a - t4b)


# def dup(nums):
#     return len(nums) != len(set(nums))
        

# t6a = time.time()
# dup([4,2,4,3,1])
# t6b = time.time()
# print(t6a - t6b)
