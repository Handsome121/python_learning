from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        hashmap = Counter(nums)
        for k in hashmap.keys():
            if hashmap[k]==1:
                return k

