#You are given an integer array coins representing coins of
# different denominations and an integer amount representing a total amount of money.
#Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
#You may assume that you have an infinite number of each kind of coin.


#This problem can be seen as a 2Dimensional DP problem where all cases = matrix
#row = coins
#amount = columns
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount+1] * amount+1
        dp[0] = 0 #for reach amount 0 "we need a minimum of 0 coin "

        for i in range(1,amount):
            for c in coins:
                if i-c >= 0: #if the amount minus the value of coint dont make a negative number
                    dp[i] = min(dp[i] , 1 + dp[i-c])
                    #we want the minimum between the actual dp stored or
                    #the dp calculated from the prec dp that is amount-coin
        return dp[amount] if dp[amount]!=dp[amount+1] else -1