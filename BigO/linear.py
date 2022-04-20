""" O(n) or Linear time is an operation whose runtime or the growth rate scale is direct proportion to the size of the input. 

for n inputs, an algorithm might perform n operations
"""
import time

def add_up(n): #Always 3 operations O(1)
    t1 =time.time()
    total = n *(n + 1) / 2
    t2 =time.time()
    
    return f'Total: {total} Time:{t1 - t2}'



def add_up_to(n): #Number of operations is (eventually) bounded by a multiple of n (say, 10n)
    total = 0
    t1 =time.time()
    for i in range(n+1):
        total += i
    t2 =time.time()
    return f'Total: {total} Time:{t1 - t2}'
       
       


# result1 = add_up(7)
# print(result1)

# result2 = add_up_to(7)
# print(result2)





def find_nemo1(i):
    print('**** find_nemo1!****')
    t1 = time.time()
    if i == 'nemo': 
        print('Found NEMO!')
    t2 =time.time()
    print(f'Time: {t1 - t2}')

# filter_list = list(filter(find_nemo1,['jake','nemo']))

# print(filter_list)



def find_nemo2(arr):
    print('**** find_nemo2!****')
    t1 = time.time()
    for i in arr:
        if i == 'nemo':
            print('Found NEMO!')
            break
    t2 =time.time()
    print(f'Time: {t1 - t2}')

# print(find_nemo2(['jake','nemo']))



def challenge1(input):
    a = 10 #O(1)
    a = 50 + 3 # O(1)
    for i in input:#O(n)
        # some_func() # * unknown .O(n)calling func for every n elements
        stranger = True #O(n)
        a+=1 # O(n)time. performing operation for every n elements
    return a #O(1)



#NOTE for the challenge1 function we can conclude that the worst-case scenario will be O(n).
# O(1 + 1 + n + n + n + n + 1) = O(3 +4n) ---> O(n)
# We are looping through N (input.length) times and for each n we are doing other operation such as calling function. O(N*(O(some_func))) -- droping the constants it evaluates to O(n) --- linear time complexity

def challenge2(input):
    a = 5 #O(1)
    b = 10 #O(1)
    c = 50 # O(1)
    for i in input:#O(n)
        x = i + 1 # O(n + 1)
        y = i + 2 # O(n + 2)
        z = i + 3 # O(n + 3)
        
    for j in input:#O(n)
        p = j * 2 # O(n * 1)
        q = j * 2 # O(n * 2)

    whoAmI = "I don't know" #O(1)

#NOTE for the challenge2 function we can conclude that the worst-case  will be O(n).   
#BIG O(4 + 7n) ----> O(n)