#Arrays consist of fixed-sized data records stored in contiguous memory locations and allow each element to be efficiently located based on its index.one of the data structures that are commonly used.



#Python dynamic array(list) operations and their complexities:

#Look-up/Access - O(1)*
my_array = [1,2,3,4,5,6,7,8,9]
look_up = my_array[1] 

#Push/Pop - O(1)*
my_array.append(7) #adds the element at the end of the array in O(1) time.
my_array.pop() #Pops/removes the element at the end of the array in O(1) time.



# NOTE: No matter how large the list is, index lookup and assignment take a constant amount of time and are thus O(1).Except when appending the last n which takes O(n) time to perform the size doubling operation
# 


#---------------#
#Insert - O(n)
my_array.insert(4,10) #inserts the specified value at the specified position.
# this would take O(n) because when item is inserted all the elements to the right shift and update their index location.


#Delete - O(n)
my_array.remove(6) #Removes the first matching value of the specified value.
#This would also have time complexity of O(n) because the elements to the right of the deleted element have to shift one space left, which requires looping over the entire array. 
# The same can be said for the pop and del method if an index is specified. Both take time complexity of O(n)
my_array.pop(4)

del my_array[5:] #deletes all element from position 5 
print(my_array)



# SUMMARY:
# Python includes several array-like data structures such as list,tuple,and  array module, 
# Dynamic arrays are arrays that do not have fixed size, and the data types don't have to be the same. You can store int,strings,floats,other lists,dict. In python its called list.

# python list use resizable vectors under the hood. whenever an element is added to the list that has reached its maximum space capacity, a new list is reallocated to hold twice as much as the previous list. dynamic array expands its size when it lacks space to append a new items.

# When looking up or accessing a dynamic array it takes a time complexity of O(1). 
# When appending in the end of a dynamic array it takes a time complexity of O(1) if it is less than the maximum capacity. 
# if the size of the dynamic array reaches maximum capacity then it takes O(n) to copy the old array into a new array. however the next n append takes O(1) because now there is more space.


#  when you create a new Array without specifying the size you need, it will create an Array of the default value. Until the default size gets filled, the push operation takes O(1) Complexity. But, if the default size is full, the compiler has to create a new Contiguous block of memory which is twice the size of the default memory, and copy the already existing elements to the newly allocated memory. So, it takes O(n) time to move the elements from one Contiguous block of memory to another Contiguous block of memory.




    