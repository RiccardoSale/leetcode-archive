# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False

    # idea of the solution, we could start from the end and see if we can reach the first element
    # how we can reach the first element ??
    # if we are in the i position and i + the value of that position could reach the actual_goal (>=)
    # in that case we need to upgrade the goal to i and continue go to the left