class Solution:
    def replaceSpace(self, s: str) -> str:
        # str_list = s.split(" ")
        # s = "%20".join(str_list)
        # return s
        return s.replace(" ","%20")

if __name__ == '__main__':
    a=Solution()
    s="we are happy"
    c=a.replaceSpace(s)
    print(c)

