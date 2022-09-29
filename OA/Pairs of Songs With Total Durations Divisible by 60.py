
"""""
You are given a list of songs where the ith song has a duration of time[i] seconds.
Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
"""""




class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        dic = {}
        res = 0

        # the plus %60 is needed because we need to accept 60 for example
        # 60 - 60%60 is equal to 60 but we dont need a 60 in the hasmap we only need a "0"
        # so 60- 0 %60 is equal to 0  as we do for add value to the map
        for x in time:
            if ((60 - x % 60) % 60) in dic:
                res += dic[((60 - x % 60) % 60)]
            dic[x % 60] = dic.get(x % 60, 0) + 1
        return res

    # similar to two sum but with a particular request