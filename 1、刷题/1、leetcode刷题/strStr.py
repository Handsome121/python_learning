class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, N = len(needle), len(haystack)
        for start in range(N - L + 1):
            if haystack[start, start + L] == needle:
                return start
        return -1
   