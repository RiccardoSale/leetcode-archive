

#Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:  # if the character is present in the set
                charSet.remove(s[l])  # remove the most left char
                l += 1  # move the sliding window
            charSet.add(s[r])  # then when we finish add the rightmost one
            res = max(res, r - l + 1)  # formula +1 because of index
        return res

# we can think a set as a simpler hasmap without the "value"
# abcabcbb
# in this example we can see the algorithm will go forward and evaluate the max
# at every iteration without change the left pointer while we dont find any repetition
# we we find a single repetition we can move the left pointer and eliminate every #character that can cause a repetition