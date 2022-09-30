class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(s) < len(p):
            return []
        hashp = {}
        hashs = {}
        for i in range(len(p)):
            hashp[p[i]] = hashp.get(p[i], 0) + 1
            hashs[s[i]] = hashs.get(s[i], 0) + 1
        l = 0
        if hashs == hashp:
            res.append(l)
        for r in range(len(p), len(s)):
            print(r)
            hashs[s[r]] = 1 + hashs.get(s[r], 0)
            hashs[s[l]] -= 1

            if hashs[s[l]] == 0:
                hashs.pop(s[l])
            l += 1
            if hashs == hashp:
                res.append(l)
        return res

    #Solution use two hashmap that have always the same size of p and s
    # and try to find when the two hashmap its the same
    #same size always = to sliding windows with left and right pointer