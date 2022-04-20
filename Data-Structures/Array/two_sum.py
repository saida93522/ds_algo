"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)

solution #1 -- Double for loop however this will be a Brute force meaning it has a growth rate of n^2. run time is going to be O(n^2) i.e Quadratic time.g
If input size is 2, it will do four operations.
1. loop through list of numbers
2. loop through the list of numbers second time, So we can find every single combination of additions between numbers.

solution #2--O(N) Use dictionary to store indices and values we've already seen
and use those stored values to look up and see whether our current value plus anything thats stored will equal the target.

"""

#Solution 1 -- worst case O(n^2)
# nums = [2,7,11,15]
# nums = [3,2,4]
target = 9
# for i in range(len(nums)-1):
#     for j in range(i+1,len(nums)): 
#         if nums[i] + nums[j] == target:
#             print([i, j])
  
    
#Solution 2
dic = {} # keep track of values and indices that we want to see
# for i,num in enumerate(nums):
#     print('num is: ', num)
#     if target - num in dic:
#         print(dic[target - num], i)
#     elif num not in dic:
#         dic[num] = i
#         print('dic[num] is : ',dic[num])
# print(dic)



#STORES the value of  target - element as key and its index as value
# 
nums = [2,7,11,15]

storage = {} #val : index

for i,e in enumerate(nums):
    # check if the difference in hashmap
    difference = target - e
    if difference in storage:
        #return a pair of indices. the index of the value in the hashmap and index in array
        print(i)
        print([storage[difference], i])
    else: 
        print(i)
        storage[e] = i
print(storage)
    

""" Example #storing the value of  target - element as key and its index as value.
        num = [2,7,11,15]
    element = target - num --> 9-2 = 7 
    index = 0

    storage = {
        '7':0,
        '2':1,
        '2':2,
        '6':3
    }
    
"""






#Solution 3 O(N)
def twoSum(self, nums, target):
    """O(N)"""
    nums_sorted = sorted(nums) # returns sorted list
        
    l_pointer , r_pointer = 0, len(nums_sorted)-1

    while l_pointer < r_pointer:
        current_some = nums_sorted[l_pointer] + nums_sorted[r_pointer]
        if current_some > target:
            #decrease right pointer if some is > target
            r_pointer -=1
        elif current_some < target:
            #increase left pointer if some is < target
            l_pointer +=1
        else:
            # otherwise current_sum == target
            return [l_pointer,r_pointer]
        