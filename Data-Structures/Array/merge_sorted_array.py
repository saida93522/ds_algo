""" Given two sorted arrays, merge the two arrays into one array that still sorted
"""
import timeit
from heapq import merge

def sort_array(array1, array2):
    # merged_arr = array1 + array2
    return sorted(array1 + array2)
    # for i in range(len(merged_arr)):
    #     min_val = i
    #     for j in range(i+1,len(merged_arr)):
    #         if merged_arr[j] < merged_arr[min_val]:
    #             min_val = j
    #     merged_arr[i],merged_arr[min_val] =merged_arr[min_val], merged_arr[i]
    # return merged_arr

# print('Timer 1')
# start = timeit.default_timer()
# sort_array([0,3,4,31],[4,6,30])
# print(timeit.default_timer() - start)



def mergesortedarr(a,b):
  if len(a)==0 or len(b)==0:
    return list(merge(a, b))
  mylist=[]
  i=0
  j=0
  while i<len(a) and j<len(b):

    if a[i]<=b[j]:
      mylist.append(a[i])
      i+=1

    elif b[j]<a[i]:
      mylist.append(b[j])
      j+=1

  return mylist+a[i:]+b[j:]



# print('Timer 2')
start1 = timeit.default_timer()
result1=mergesortedarr([0,3,4,31],[4,6,30])
print(result1)
# print(timeit.default_timer() - start1)


def sorted_array(arr1,arr2):
    if not arr1 or not arr2:
        print('provide valid array')
    else:
        array_sum=arr1+arr2
    return (sorted(array_sum))


# print('Timer 3')
# start2 = timeit.default_timer()
# sorted_array([0,3,4,31],[4,6,30])
# print(timeit.default_timer() - start2)


def merge_sorted_array(arr1,arr2):
  # check input
  if len(arr1) == 0 or len(arr2) == 0:
    return arr1+arr2
  
  merged_array = []
  arr1_item=arr2_item = 0
  while arr1_item<len(arr1) and arr2_item<len(arr2):
    
    if arr1[arr1_item] <= arr2[arr2_item]:
      merged_array.append(arr1[arr1_item])
      arr1_item+=1
      
    elif arr2[arr2_item] <= arr1[arr1_item]:
      merged_array.append(arr2[arr2_item])
      arr2_item+=1
  return merged_array + arr1[arr1_item:]+arr2[arr2_item:]
# mylist+a[i:]+b[j:]

result = merge_sorted_array([4,6,30],[])
print(result)





#Using Stack method
def merge_arrays(array1,array2):
    "using stack, pop smaller elements from the top of the stack and append the popped item to the list. continue this until the stack is empty"
    my_list = []
    while array1 and array2:
        if array1[0] < array2[0]:
            my_list.append(array1.pop(0))
        else:
            my_list.append(array2.pop(0))
    my_list += array1
    my_list += array2
    return my_list

t2 = timeit.default_timer()
merge_arrays([0,3,4,31],[4,6,30])

print(timeit.default_timer()-t2)