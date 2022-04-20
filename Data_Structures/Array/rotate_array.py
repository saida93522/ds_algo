#Given an array, rotate the array to the right by k steps, where k is non-negative.
#Example 1:
#nput: nums = [1,2,3,4,5,6,7], k = 3
#Output: [5,6,7,1,2,3,4]

#Solution: #1
# class Rotate(object):
#     def rotate(self,nums,k):
#         k %= len(nums)
#         nums[:] = nums[len(nums)-k:] + nums[:len(nums) -k]
#         return nums

    

# my_list = Rotate()
# result = my_list.rotate([1,2,3,4,5,6,7],3)
# print(result)


k = 3
nums = [1,2,3,4,5,6,7]

mid = len(nums) - (k % len(nums))
nums[:] = nums[mid:] + nums[:mid]
del mid
print(nums)
