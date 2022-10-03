class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        if len(nums) == 1:
            return nums[0]

        res = float("inf")
        while l <= r:
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[l] < nums[r]:
                return min(nums[l], res)
                # we need to check because we could arrive from the left
            # and already seen the min value so min beetwen l and res

            if nums[mid] >= nums[l]:
                # we know for sure that left is greater then the value to ou right so we search right
                l = mid + 1
            else:
                r = mid - 1
        return res
