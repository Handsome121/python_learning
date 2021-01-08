# class Solution:
#     def findRepeatNumber(self, nums):
#         nums.sort()#数组排序
#         for i in range(len(nums)-1):
#             if nums[i]==nums[i+1]:
#                 yield nums[i]
#
#
#
# a1=Solution()
# result_lst=a1.findRepeatNumber([5,2,2,1,1,3,5,6,8,9,2])
# for i in result_lst:
#     print(i)
# 复杂度分析
#     时间复杂度：O(NlogN),sort排序。
#     空间复杂度：O(1)。

# from typing import List
#
#
# class Solution:
#     def findRepeatNumber(self, nums: List[int]) -> int:
#         s = set()
#         for num in nums:
#             if num in s:
#                 yield num
#             else:
#                 s.add(num)
#
#
# a1 = Solution()
# result_lst = a1.findRepeatNumber([5, 2, 2, 1, 1, 3, 5, 6, 8, 9, 2])
# for i in result_lst:
#     print(i)
# 复杂度分析
#     时间复杂度：O(N)。在最坏条件下，我们会遍历整个数组。
#     空间复杂度：O(N)。使用了哈希set作为辅助空间。

