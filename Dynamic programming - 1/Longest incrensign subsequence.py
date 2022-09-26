class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    #i is always before j so if we see that i < j then we can
                    # add the value of the subsequence that we already know
                    #in this way we could find the max

                    LIS[i] = max(LIS[i], 1 + LIS[j])

        # print(LIS)
        return max(LIS) #max of LIS