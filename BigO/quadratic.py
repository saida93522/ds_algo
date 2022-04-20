""" O(n^2) or Quadratic time is an operation whose runtime is directly proportional to the squared size of the input data set. 

for n inputs, an algorithm might perform n operations for n times.
running a linear operation within another linear operation(n*n=n2)
"""


# Log all pairs of array

def log_all_pair_of_arrays(boxes):
    for i in range(len(boxes)):
        for j in range(i+1,len(boxes)):
           boxes[i] = boxes[i] + boxes[j]
    return boxes


result = log_all_pair_of_arrays([1,2,3,4,5])
print(result)
#NOTE 
# Loop through the array and select first element of the pair
# for each element selected tr
# time complexity: O(n^2) -- scanning through array to find the n times.


def log_pair_arrays(boxes):
    for i in range(len(boxes)):
        for j in range(i+1,len(boxes)):
           boxes[i] = boxes[i] + boxes[j]
    return boxes