import time


def sum_to_n(n):
    """calculates the sum of the first n numbers

    Args:
        n ([int]): [number]

    Returns:
        [total]: [the sum of n]
        [time]: [how long it to calculate]
    """
    # record start time
    start = time.time()
    total = 0
    for i in range(n +1):
        total += i
    # record end time
    end = time.time()
    time_stamp = end - start
    return total, time_stamp

result1 = sum_to_n(1000) # O(n)
print(result1)


def arithmic_sum(n):
    # record start time
    start = time.time()
    total = n * (n +1) // 2
    # record end time
    end = time.time()
    time_stamp = end - start
    return total, time_stamp

# calc = 16*(16+1) / 2
# print(calc)

for i in range(1,10):
    result2 = arithmic_sum(i * 10000) #O(1)
print(result2)
