#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
#and return its sum.
#Example:
#Input: [-2,1,-3,4,-1,2,1,-5,4],
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.


#Solution: 1 "Sliding window". remove all negatives unless it comes after a positive nums. time complexity of O(n)
def max_sub_array(nums):
    max_sub = nums[0] #assume first index is max sub
    cur_sum = 0
    for i in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += i
        max_sub = max(max_sub,cur_sum)
    return max_sub


result = max_sub_array([-2,1,-3,4,-1,2,1,-5,4])
print(result)