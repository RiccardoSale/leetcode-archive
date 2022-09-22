
##Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
##You may assume that each input would have exactly one solution,
# and you may not use the same element twice.##
# You can return the answer in any order.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {} # value -> index

        for i,n in enumerate(nums):
            diff = target-n
            if diff in dic:
                return [dic[diff],i]
            dic[n] = i

#notes

#use hash map to instantly check for difference value,
# map will add index of last occurrence of a num, don’t use same element twice

#Recap for hashmap
# inizialiation name ={}
# we can store in a map of key tot a value n in this way dic[key]=value
#if we use dic[key] we can access the value
#we could check if the value exists with the keyword in








