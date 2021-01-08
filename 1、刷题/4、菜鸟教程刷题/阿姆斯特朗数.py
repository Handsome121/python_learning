"""
如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153
"""


def get_Armstrong(num):
    str_num = str(num)
    n = len(str_num)
    sum_value = 0
    for i in range(n):
        sum_value += int(str_num[i]) ** n
    if sum_value == num:
        print(num, "是阿姆斯特朗数")
    else:
        print(num, "不是阿姆斯特朗数")
get_Armstrong(153)