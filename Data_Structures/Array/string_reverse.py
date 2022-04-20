""" reverse a string
"""

import time
import timeit
# create a function that reverses a string

# ****** Solution:-1*****
# To create an empty list. loop through the array starting from last index and append it to the new array.

def brute_force(string_arr):
    reverse_str = []
    for i in range(len(string_arr)-1,-1,-1): #start last element,step -1,stop first element
        reverse_str.append(string_arr[i]) #append to the new array
    return ''.join(reverse_str) #join char to return string instead of array

print('***Solution--1***')
t1 = timeit.default_timer()
brute_force('saida')
# result = brute_force('saida')
# print(result)
print(timeit.default_timer() - t1)


#NOTE: since we are looping through input once, the time complexity is O(n).Also we are creating a new array of the same size,the space complexity is O(n). as n get larger the more space the list would have to make



# ****** Solution:-2 *****
# reverse a string through slicing. since string are sequences, they are indexable,sliceable and iterable

def reverse_str(string_arr):
    if type(string_arr) is int:
        return 'Only strings'
    # [start:stop:step]
    return string_arr[::-1] #by default offset steps by 1. if we pass negative value to step,slicing runs backward. right to left

print('***Solution--2***')
time_sol2=timeit.default_timer()
reverse_str('Hi')
print(timeit.default_timer() - time_sol2)


# NOTE: Using built-in function, like slice() or slice technique O(1). Our time complexity reduces to O(1) since we are not looping though the array.

# ****** Solution:-3 *****
# reverse a string with .join() and reversed(). The most pythonic approach to reverse a string it to use these methods.The reversed() allows us to process the items in a sequence in reverse order. It accepts a sequence and returns an iterator. we know that string are sequences we can utilize this function.

def reverse_string(string_arr):
    # print(next(reversed(string_arr))) # we can retrieve each character from the right to end of string
    return "".join(reversed(string_arr))

print('***Solution--3***')
time_sol3=timeit.default_timer()
reverse_string('Hawo')
print(timeit.default_timer() - time_sol3)


#NOTE: Although Solution 3 is efficient in terms of space complexity(reversed(),iterator yields characters directly from the original string). we are not creating or returning new array but simply reading backward from the existing array. After timing we can estimate that Solution:2 is almost faster and more concise.



def swap(string,a,b):# swaps two chars of a string
    string = list(string)
    temp = string[a]
    string[a] = string[b]
    string[b] = temp
    return ''.join(string)

string = 'Hello'
# string_result = swap(string,1,len(string)-2)
# print(string_result)

def smart_reverse(string):
    # take two pairs from either end of a string and swap them until the middle of the string.
    for i in range(len(string)//2):
        string = swap(string,i,len(string)-i-1)
    return string

print('***Solution--4***')
time_sol4=timeit.default_timer()
smart_reverse(string)
print(timeit.default_timer() - time_sol4)
# print(smart_reverse(string))


# ****** Solution:-4 *****
#this approach is also a time complexity of O(n)
#  but it is efficient in terms of space complexcity since we are not creating a new array