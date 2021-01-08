class Solution:
    def removeElement(self, nums, val):
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)


if __name__ == '__main__':
    a = Solution()
    nums = [0, 1, 1, 2, 2, 1, 2, 1, 3, 0]
    c = a.removeElement(nums, 0)
    print(c)
