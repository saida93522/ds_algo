""" during each iteration you'll select the smallest item from the unsorted partion and move it to the sorted partion.

    keep track of current minimum value which is always set to the first element, and swapping it with current element if it is less than

pseudo code

repeat/loop (numberOfElements -1) times
    assume/set the first unsorted element as the minimum
    for each of the rest of unsorted element
        if element < currentMinimum
            set this element as the new minimum
    swap minimum with first unsorted position

    time complexity: O(n2) -- scanning through array to find the smallest for n times.
    space complexity: O(1) -- does not rely on any extra arrays
 """

def sort_sel(arr):
    for i in range(len(arr)):
        current_min = i
        for j in range (i +1,len(arr)):
            if arr[j] < arr[current_min]:
                current_min = j
        # take the initial value  with and swap that with the position of the lowest item
        # arr[i], arr[current_min] = arr[current_min], arr[i]
        swap(arr,i,current_min)
        # print(arr)
        # print('*****')
    return arr

def swap(arr,index1,index2):
    arr[index1],arr[index2] = arr[index2],arr[index1]
    return arr


# result2 = sort_sel([4,9,3,6,2]) #2,9,3,6,4
# print(result2)



def sort_array(arr):
    print(arr)
    for i in range(len(arr)):
        min_num = i
        for j in range(i + 1,len(arr)):
            if arr[j] < arr[min_num]:
                min_num = j

        
        arr[i], arr[min_num] = arr[min_num], arr[i]
        print(arr) 
    return arr



result = sort_array([30,60,20,50,40,10])
print(result)