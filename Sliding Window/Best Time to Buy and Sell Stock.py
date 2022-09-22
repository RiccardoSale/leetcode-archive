#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a
# different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        res = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res


    #We need to use a sliding window with two pointers for save the local minimum and
    # then find the max after that local minimum