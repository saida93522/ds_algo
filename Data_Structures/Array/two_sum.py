"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)

solution #1 --Brute force, to loop through twice until can find every single combination of additions between numbers resulting in a growth rate of n^2. run time is going to be O(n^2) i.e Quadratic time.g

solution #2--O(N) Use dictionary to store indices and values we've already seen
and use those stored values to look up and see whether our current value plus anything thats stored will equal the target.

"""

#Solution: 1 -- worst case O(n^2)
# nums = [2,7,11,15]
# nums = [3,2,4]
target = 9
# for i in range(len(nums)-1):
#     for j in range(i+1,len(nums)): 
#         if nums[i] + nums[j] == target:
#             print([i, j])
  
    
#Solution: 2
#STORES the value of  target - element as key and its index as value
# 
# numbers = [2,7,11,15]

def two_sum1(nums,target):
    storage = {} #val : index
    for i,e in enumerate(nums):
        # check if the difference in hashmap
        difference = target - e
        
        if difference in storage:
            #return a pair of indices. the index of the value in the hashmap and index in array
            return [storage[difference], i]
        else:
            storage[e] = i
        
    

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






#Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.
def two_sum_sorted(nums, target):
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
            return [l_pointer+1,r_pointer+1]
        