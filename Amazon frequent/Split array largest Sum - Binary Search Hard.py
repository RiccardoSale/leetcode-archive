class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # Binary Search solution
        # l=max(nums) = 18 #l and r are the range of solution
        # r=sum(nums) = 37

        # mid = 27 if we found 27 is the solution

        # start at the beginning 7 is less than 27
        # we continue to add until we are under than 27

        # if the entire subarray is less than 27
        # then we can split it and its sure is less

        # then we repeat the new binary search with 18 and 26
        # time complexity (n*log(s))

        l, r = max(nums), sum(nums)
        res = r

        def canSplit(largest):
            subarray = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:  # if cursum become > largest
                    subarray += 1
                    curSum = n  # we compute the new subarray starting from n we dont want n to be included if curSum broke the largest threshold

            return subarray + 1 <= m

        while l <= r:
            mid = (l + r) // 2
            if canSplit(mid):  # if we can split we can reach that result
                res = mid  # so we update res
                r = mid - 1  # look for smaller value
            else:
                l = mid + 1  # we search for bigger value
        return r + 1