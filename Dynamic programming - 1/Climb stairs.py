# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Basically is Fibonacci
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        start_one = 1
        start_two = 2
        for i in range(n - 2):
            temp = start_one
            start_one = start_two
            start_two = temp + start_two
        return start_two