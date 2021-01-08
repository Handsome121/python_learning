'''
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''


def combination_number(number):
    list01=[]
    for i in range(1,number):
        for j in range(1,number):
            for k in range(1,number):
                if (i != k) and (i != j) and (j != k):
                    result = i * 100 + j * 10 + k
                    list01.append(result)
    return list01
list01=combination_number(5)
print(list01)
