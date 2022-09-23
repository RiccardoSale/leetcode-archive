#iven an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

#You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        pre = [0]*len(nums)
        sum_ = 1
        for i,x in enumerate(nums):
            pre[i] = sum_
            sum_ *= x
        sum_ = 1
        for i in range(len(nums)-1,-1,-1):
            #we can compute the result directly making the product with the prefix array
            res[i] = sum_ * pre[i]
            sum_ *= nums[i]
        return res