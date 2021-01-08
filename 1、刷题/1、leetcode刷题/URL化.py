class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(" ","20%")
        return "20%".join(S[:length].split(" "))
a=Solution()
b=a.replaceSpaces("er st 320 fef",10)
print(b)
