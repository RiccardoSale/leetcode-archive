# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = collections.defaultdict(list)
        # dic with count as key and values = list
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1  # ord necessary for conversion
            ans[tuple(count)].append(s)
            # transform into tuple for compatibility with dict
        return ans.values()  # we want to return all values inside the dictionary