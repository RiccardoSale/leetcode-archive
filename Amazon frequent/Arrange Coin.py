#You have n coins and you want to build a staircase with these coins. The staircase consists
# of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
#Given the integer n, return the number of complete rows of the staircase you will build.


class Solution:
    def arrangeCoins(self, n: int) -> int:

        def ric(n, i):
            if (n - i) >= 0:
                return 1 + ric(n - i, i + 1)
            else:
                return 0

        return ric(n, 1)
#O(i)

#but we can do 0(log(n)) binary search
#We need to know Gauss formula
#number 1 to 100 how add them faster
#we need gauss formula
#1+100 = 101
#2+ 99 = 101
#only exception are the two central one
#if we split 100 in two array
#we now know the pairs ....50 the pair sum to 101

#(n/2)*(n+1)
#calculate series of value
#n is the upper bound for the rows (sure less but still upper bound)

#l = 1
#r = n
#we calculate mid can we make "mid" row
#for make mid row we need tot coin
#tot coin can be found with gaus formula
    l, r = 1 , n
    res = 0
    while l<=r:
        mid = (l+r)//2 #row
        coins = (mid/2)*(mid+1) #coins needed for that row
        if coins > n: #i cant create mid row if coins are > than n 
            r = mid -1
        else:
            l= mid + 1
            res = max(mid,res)
    return res


#or O(1) r/2(r+1) = n














