# 输入数组，求和等于指定数的元素下标

class Solution():

    def __init__(self, *nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target

    def sum_two(self):
        list01 = []
        for i in range(len(self.nums) - 1):
            for j in range(i + 1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    list01[:] = i, j
        print(list01)


a = Solution(1, 2, 3, 4, 5, target=5)
a.sum_two()
