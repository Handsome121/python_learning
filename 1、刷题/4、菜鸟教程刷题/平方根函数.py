'''平方根，又叫二次方根，表示为〔√￣〕，如：数学语言为：√￣16=4。语言描述为：根号下16=4。
以下实例为通过用户输入一个数字，并计算这个数字的平方根：
'''
# num=float(input("请输入一个数字："))
# num_sqrt=num**0.5
# print('%.3f的平方根为%.3f'%(num,num_sqrt))

# import cmath
# # num=float(input("请输入一个数字："))
# # num_sqrt=cmath.sqrt(num)
# # print('{0}的平方根为{1:0.3f}+{2:0.3f}'.format(num,num_sqrt.real,num_sqrt.imag))

import cmath

a = float(input("请输入一个实数字: "))
b = float(input("请输入一个虚数字: "))
num_sqrt = cmath.sqrt(complex(a, b))#复数complex()
print('{0:0.3f}+ {1:0.3f}j 8的平方根为 {2:0.3f}+{3:0.3f}j'.format(a, b, num_sqrt.real, num_sqrt.imag))
