# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
#(bucket sort)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():  # analyze each element of dictionar
            # n = key c = value
            freq[c].append(n)  # we append at frequency c the value that occur c time
        print(freq)
        res = []
        # from len(freq)-1 last element
        for i in range(len(freq) - 1, 0, -1):  # 0 in not necessary to check but we could go to -1  for stop
            for n in freq[i]:
                res.append(n)
                if len(res) == k:  # we start from the end that is equal to the max frequency number so when we reach k element we have completed the problem
                    return res