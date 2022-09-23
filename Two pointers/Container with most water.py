# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.
# Return the maximum amount of water a container can store.

class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1

        res = 0
        while l < r:
            res = max(res, (r - l) * min(height[l], height[r]))

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res

#two pointers we compute all "possible max cases" with the "home made" formula and we shift to the
#left or right making a comparision beetween the height of the two pointers