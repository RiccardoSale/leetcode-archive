# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        res = 0
        for i in range(len(nums)):
            res = max(rob1, rob2 + nums[i])
            rob2 = rob1
            rob1 = res

        return res


#we can think that rob2 is the house one step far from us so we can add nums[i]

#rob1 is the house adiacent to us where we cant sum anything

#rob1 will become the result generated on the last max iteration

#rob2 will became rob1 the house that was " adiacent will now be far "

