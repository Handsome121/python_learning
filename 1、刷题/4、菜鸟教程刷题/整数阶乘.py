'''
整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n。
'''
number=int(input("请输入一个数字："))
factorial=1
if number<0:
    print("负数没有阶乘")
elif number==0:
    print("0的阶乘是1")
else:
    for i in range(1,number+1):
        factorial*=i
    print("%d的阶乘是%d"%(number,factorial))
