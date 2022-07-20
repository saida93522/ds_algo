# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Solution:  using two point solution we can keep track of the days when the price is the lowest to buy and the dat when the price is high to sell. left = buy right = sell. calculate the difference for max profit. 

def maxProfit(prices):
    left_pointer, right_pointer = 0, 1
    max_profit = 0

    #loop until right_pointer reaches end of array
    while right_pointer < len(prices):
        # check if left is pointing to the smallest price
        if prices[left_pointer] < prices[right_pointer]:
            calc_profit = prices[right_pointer] - prices[left_pointer]
            max_profit = max(max_profit, calc_profit)
        else:
            # since r is pointing at the smallest price, we update left pointer
            left_pointer = right_pointer
            
        right_pointer += 1
    return max_profit



result = maxProfit(prices = [7,1,5,3,6,4])
print(result)