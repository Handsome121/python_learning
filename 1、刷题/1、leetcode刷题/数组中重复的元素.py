class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        repeatDict = {}
        for num in nums:
            if num not in repeateDict:
                repeateDict[num] = 1
            else:
                return num
