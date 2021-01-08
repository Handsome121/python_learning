class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_list = s.split(" ")
        word_length = len(str_list[-1])
        return word_length


if __name__ == '__main__':
    a = Solution()
    s = "hello world hello xiaomage"
    word_length=a.lengthOfLastWord(s)
    print(word_length)

