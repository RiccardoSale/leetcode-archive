# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use set for know immediatly how much n that generate a start of sequence there are
        set_ = set(nums)
        res = 0

        for i in range(len(nums)):
            n = nums[i]
            if (n - 1) not in set_:  # so n is a start of a sequence
                count = 1
                while (n + count) in set_:
                    count += 1
                res = max(res, count)
        return res