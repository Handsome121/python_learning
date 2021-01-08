class Solution(object):
    def addDigits(self,num):
        str_num=str(num)
        sum=0
        for i in str_num:
            sum+=int(i)
        while sum>9:
            str_num=str(sum)
            sum=0
            for j in str_num:
                sum+=int(j)

        return sum
a=Solution()
print(a.addDigits(121))






