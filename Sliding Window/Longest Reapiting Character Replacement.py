# You are given a string s and an integer k.
# You can choose any character of the #string and change it to any other uppercase English character.
# You can perform this #operation at most k times.
#return the most longest substring without repetition
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        l = 0
        res = 0
        maxrep = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxrep = max(maxrep, count[s[r]])
            # we use the hasmap to save the maxrep of the same char

            if (r - l + 1) - maxrep > k:
                # we compute the distance we have reached and subract the maxrep
                count[s[l]] -= 1
                l += 1
            else:
                res = max(res, r - l + 1)
        return res