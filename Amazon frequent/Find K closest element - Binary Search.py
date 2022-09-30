class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l = 0
        r = len(arr) - k  # because we can arrive maximum at r and see the other with m+k
        # we cant do an usually binary search on target because we are not sure
        # if the value is inside our array so we have to try search for the closest one
        # moving with window
        while l < r:
            m = (l + r) // 2  # calculate mid
            # arr m+k is the most right element of the window
            # arr [m] is for sure <  than arr [m+k]
            # so x - arr [m] or  arr[m+k] - x
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                # we dont know if value to the left are closer so but we cant go further than mid
                r = m
        return arr[l:l + k]  # we return the window l+k is not inclusive