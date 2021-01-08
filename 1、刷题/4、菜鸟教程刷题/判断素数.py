'''
一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），\
换句话说就是该数除了1和它本身以外不再有其他的因数。
'''
number = input("请输入一个数:")
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("不是质数")
            break
        else:
            print("是质数")
else:
    print("不是质数")

#输出指定范围内素数
# lower = int(input("输入区间最小值: "))
# upper = int(input("输入区间最大值: "))
#
# for num in range(lower, upper + 1):
#     # 素数大于 1
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)
