# Given an integer array nums, return all the triplets
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        for i, x in enumerate(nums):
            if i > 0 and x == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                triple = x + nums[l] + nums[r]
                if triple == 0:
                    res.append([x, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif triple < 0:
                    l += 1
                else:
                    r -= 1
        return res

#sort the array and then use two pointer + the "immovable" for pointer for create all the possbile solution
#Pay attention to dont use the same value two times so we have:
# if i > 0 and x == nums[i-1]: continue


