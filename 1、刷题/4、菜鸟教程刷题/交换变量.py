'''
以下实例通过用户输入两个变量，并相互交换：
'''
x = input("输入x值")
y = input("输入y值")
# 创建临时变量
temp = x
x = y
y = temp
print("交换后x的值为：{}".format(x))
print("交换后y的值为：{}".format(y))
