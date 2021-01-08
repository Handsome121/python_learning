class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        odd = {}

        for ch in s:
            if ch in odd.keys():
                del odd[ch]
            else:
                odd[ch] = 0
        if len(odd.keys()) > 1:
            return False
        else:
            return True


a = Solution()
b = a.canPermutePalindrome("asdv")
print(b)
