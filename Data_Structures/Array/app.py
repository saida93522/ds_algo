import timeit
from heapq import merge

# def merge_arr(arr1,arr2):
#     if len(arr1) == 0 or len(arr2) == 0:
#         return list(merge(arr1, arr2))

#     my_list = []
#     i = j = 0
#     flag = 0

#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] <= arr2[j]:
#             my_list.append(arr1[i])
#             i+=1
#         elif arr2[j] < arr1[i]:
#             my_list.append(arr2[j])
#             j+=1

#         if i == len(arr1):
#             flag = 1

#     if flag:
#         for item in arr2[j:]:
#             my_list.append(item)
#     else:
#         for item in arr1[i:]:
#             my_list.append(item)
            
#     return my_list


# def merge_data(arr2,arr1):
#     if len(arr1) == 0 or len(arr2) == 0:
#         return arr1 + arr2

#     my_list = []
#     while arr1 and arr2:
#         if arr1[0] <= arr2[0]:
#             my_list.append(arr1.pop(0))
#         else:
#             my_list.append(arr2.pop(0))
#     my_list+=arr1
#     my_list+=arr2

#     return my_list
            
            
def check_for_duplicates(arr):
    unique = set()
    for i in arr:
        if i in unique:
            return True
        else:
            unique.add(i)
    return False 



# result = check_for_duplicates([1,2,3,4])
# array1 = [1,2,3,4]
# array2 = [5,6,7,8,9,10]
# t1 = timeit.default_timer()
# result =  merge_data(array2,array1)
# print(result)
# print(timeit.default_timer()-t1)
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