#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Example:
#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]

def move_zeros(nums):
    # swap values in a list using syntax: x, y = y, x.
    zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            print(zero,i)
            nums[zero],nums[i] = nums[i],nums[zero]
            zero+=1
            print(nums[zero],nums[i])
            print('-----')
            
    return nums


result4 = move_zeros( [0,1,0,3,12])
print(result4)
# We use i to keep track of position of the first zero in the list (which changes as we go).
# We use j to keep track of the first non-zero value after the first zero (which is pointed by i).
# Each time we have i correctly points to a zero and j correctly points to the first non-zero after i, we swap the values that store at i and j.
# By doing this, we move zeros towards the end of the list gradually until j reaches the end.
# And when it does, we are done.