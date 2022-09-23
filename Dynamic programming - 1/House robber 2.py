



#Same probelem as House robber 1 but the list is circular so we need to dont sum togheter
#the first and last element of the list
#How to do this? in the first iteration skip first element
#In the second iteration skip the last element 

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        rob1 = 0
        rob2 = 0
        res = 0

        for i in range(1, len(nums)):
            res = max(rob1, rob2 + nums[i])
            rob2 = rob1
            rob1 = res

        rob1, rob2, res_2 = 0, 0, 0

        for i in range(len(nums) - 1):
            res_2 = max(rob1, rob2 + nums[i])
            rob2 = rob1
            rob1 = res_2

        return max(res, res_2)