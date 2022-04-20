""" O(1) or constant time is an operation whose runtime or the growth rate scale is NOT direct proportion to the size of the input. 

a function will stay "constant" as input(s) get arbitrarily large.

The size of the input does not affect the number of operations performed
"""
import time
#Order of function
def lower_list(arr):
    if len(arr) == 0: # O(1)
        return 'No data'
    else:#O(n)
        return list(map(lambda i:i.lower(),arr))


# result = lower_list(['EGG','Strawberry','APPLE'])
# print(result)


ten_arr = ['nemo' for i in range(10)]
hundred_arr = ['nemo' for i in range(100)]
thousand_arr = ['nemo' for i in range(1000)]

def find_nemo(arr):
    #The size of the input does not affect the number of operations performed. it will always return specified value of index
    t1 = time.time()
    print(arr[0]) # O(1)
    print(arr[1]) # O(1)

    t2 = time.time()
    print(f'Time: {t1-t2}')  
    
find_nemo(ten_arr)
print('**')
find_nemo(hundred_arr)
print('**')
find_nemo(thousand_arr)

#NOTE 
# Not looping though the entire array rather returning the first and second elements. Time taken for the 3 cases would be 0.0 or same seconds.Therefore we can conclude that this function(find_nemo) takes constant time complexity i.e it is of O(1)



