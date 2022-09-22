# Given two strings s and t of lengths m and n respectively,
# return the minimum window substring of s such that every character in
# t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        dic_t = {}
        for i in range(len(t)):
            dic_t[t[i]] = 1 + dic_t.get(t[i], 0)
        # first we save in an hasmap the char/occurence we need for the minimum substring window

        l = 0
        window = {}
        have = 0
        need = len(dic_t)
        reslen = float('inf')
        res = [-1, -1]

        for r in range(len(s)):  # then we start iterate on the second string
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in dic_t and window[s[r]] == dic_t[s[r]]:
                have += 1
                # if we found that we have the same character and occurence in the string we update have to +1 we have the minimum occ of that character

            while have == need:
                # now we can start remove char from the left and see if have remains equal to need
                if r - l + 1 < reslen:  # we update our result
                    reslen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1  # we pop the most left char
                if s[l] in dic_t and window[s[l]] < dic_t[
                    s[l]]:  # if the minum occurence of that char is not equal or bigger we decrease have
                    have -= 1
                l += 1  # we always move left pointer

        return s[res[0]: res[1] + 1] if reslen != float("inf") else ""
        # slice from pointer l to r +1 because r is not included