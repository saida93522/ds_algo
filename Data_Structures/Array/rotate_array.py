from collections import deque
#Given an array, rotate the array to the right by k steps, where k is non-negative.
#Example 1:
#input: nums = [1,2,3,4,5,6,7], k = 3
#Output: [5,6,7,1,2,3,4]

#Solution: #1 using slice method , Time-complexity is 0(n) and space complexity is 0(n)

def rotate_right(nums,k):
    #  rotate a list in place
    k %= len(nums) #avoid overflow
    nums[:] = nums[len(nums)-k:] + nums[:len(nums) -k] #store elements -k to len and len(num) to k and concatenate arrays   
    return nums

def rotate_left(nums,k):
    k %= len(nums)
    nums[:] = nums[k:] + nums[:k]
    return nums

#Solution: 2 using deque

def rotate_nums(nums,k):
    nums = deque(nums)
    nums.rotate(k)
    return nums

rotate_nums([1,2,3,4,5,6,7],3)

