""" Binary search is search algorithm. It takes in a sorted list of elements. Start the search with the middle element and eliminate half of the remaining elements every time. this process repeats until the desired value is found or all elements have been eliminated.

if the element your are searching for is in the list it will return the index, or the position it is located in. otherwise it returns NULL.

it takes log n element in the worst case.
"""

def binary_search(arr,item):
    low = 0
    high = len(arr) -1
    mid = (low + high) // 2 #check middle element. rounded down by python if (low + high) == even number.
    while low <= high:
        guess = arr[mid] # middle element of the array

        if guess == item:
            #if the middle element == item return the index
            return mid 
        elif guess > item:
            #if the mid el is greater than the item, start searching all elements less than mid el.
            high = mid - 1

        else:
            #if the mid el is less than the item, start searching all elements greater than mid el.           
            low = mid + 1
    return None



# result = binary_search([1,3,5,7,9],3)
# print(result)



