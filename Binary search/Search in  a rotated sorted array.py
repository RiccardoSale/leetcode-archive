class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[l] <= nums[mid]:  # left portion
                if target > nums[mid]:  # right because from l to mid order and target >mid
                    l = mid + 1
                else:  # target < mid
                    if target < nums[l]:
                        # we could write only target > nums[mid] or target< nums[l]
                        l = mid + 1  # right again
                    else:
                        r = mid - 1  # else left
            else:
                if target < nums[mid]:  # so che da mid a r e ordinato
                    r = mid - 1  # vado a sx non puo essere nella porzione dx
                else:
                    if target > nums[r]:
                        # so che e fuori dalla porzione destra ugualemente perche r e piu piccolo
                        r = mid - 1
                    else:
                        l = mid + 1
        return -1
