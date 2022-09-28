#Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#A subarray is a contiguous part of an array.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a_sum = 0
        res = float("-inf")

        for r in range(len(nums)):
            a_sum += nums[r]
            res = max(res, a_sum)
            if a_sum < 0:
                a_sum = 0
        return res

        # idea of the solution we need to remove the prefix is it is negative, other than that we add            number
        # we could think this as a sliding windows exercise "we move left " when we put actual sum equal             to 0