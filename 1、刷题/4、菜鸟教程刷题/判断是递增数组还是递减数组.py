"""
如果数组是单调递增或单调递减的，那么它是单调的
当给定的数组 A 是单调数组时返回 true，否则返回 false
"""
class Solution(object):
    def isMonotonic(self, A):
        for i in range(len(A)-1):
            if A[i]<A[i+1]:
                return True
            elif A[i]>A[i+1]:
                return True
            else:
                return False
a=Solution()
print(a.isMonotonic([1,3,4,5,6]))
