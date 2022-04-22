#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Example:
#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]


#Solution: we can modify and reverse the question by moving non-zero elements to the left side of the array thus resulting 0 elements to be at the end of the array. 
# time complexity is O(n)
# We use right_pointer to keep track of position of the first non-zero in the list (which increments as we go).
# We use left_pointer variable to keep track of the first zero value after the first non-zero (which is pointed by right_pointer).
# and each time we have right_pointer correctly pointing to a non_zero value and left_pointer correctly pointing to the zero value , we swap the values that is stored at left_pointer and right_pointer.
# By doing this, we move non-zeros towards the left of the list gradually until right_pointer reaches the end.
# We are looping though the array once and the swapping is done in constant time, so overall time complexity is O(n)




def move_zeros(arr):
    left_pointer = 0
    for right_pointer in range(len(arr)):
        if arr[right_pointer]:
            # swap values in a list using syntax: x, y = y, x.
            arr[left_pointer], arr[right_pointer] = arr[right_pointer],arr[left_pointer]
            left_pointer+=1
    return arr





#Solution:2 since zero is a falsy value we can sort the array on the basis of boolean values.The zeros are moved to the beginning of the array and the rest of the elements which are considered 1 are moved to the end. resulting in --> [0, 0, 1, 3, 12], then we pass reverse parameter to maintain the relative order.However the complexity for this would be O(nlog n) as the complexity of Python's built-in sort method is O(nlog n) 

def move_zeros_sort(arr):
    arr.sort(key=bool,reverse=True)
    return arr

result = move_zeros_sort([0,1,0,3,12])
print(result)


    