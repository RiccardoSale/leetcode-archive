"""""
You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.
"""

class Solution:
    def minFlips(self, s: str) -> int:

        n = len(s)  # size of window
        s = s + s  # we do this concatenation because we want check every possible sliding window
        # like we used the remove and append operation how we can do this "more cleaver" ?
        # for example if we have 0100  s+s=01000100
        # now all the sliding window can be 0100 1000 0001 0010 0100
        alt1, alt2 = "", ""
        for i in range(len(s)):
            # we can have have two target and for make easier to code it up we
            # they will have the same lenght of s+s
            alt1 = "0" if i % 2 else "1"
            alt2 = "1" if i % 2 else "0"

        res = len(s)
        diff1, diff2 = 0, 0
        l = 0
        for r in range(len(s)):
            # now we can compute the minum amount of diff for every sliding window and each target
            if s[r] != alt1[r]
                diff1 += 1
            if s[r] != alt2[r]
                diff2 += 1
            if (r - l + 1) > n:
                # we move the window if we reach > len and decrement the diff if we found before
                if s[l] != alt1[l]:
                    diff1 -= 1
                if s[l] != alt2[l]:
                    diff2 -= 1
                l += 1  # increanse left
            if (r - l + 1) == n:  # Compute best result
                res = min(res, diff1, diff2)
        return res