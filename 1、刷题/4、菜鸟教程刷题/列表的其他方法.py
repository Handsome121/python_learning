# '''
# 列表的其他方法
# '''
# a = [21, 32, 43, 45]  # 创建一个列表
# a.reverse()  # 按照相反的顺序排列列表中的元素
# b = a.copy()  # 复制列表，浅复制 注：常规复制只是将另一个名称关联到列表
# a.clear()  # 清空列表的内容,相当于切片赋值语句list[:]=[]
# a.extend([1, 3, 4, 5, 6, 8])  # 可以使用另外一个列表来扩展这个列表
# a.pop()  # 从列表中删除一个元素，并返回这个元素，默认值为列表最后一个元素
# a.sort() #用于对列表就地排序，对原有的列表进行修改，使其元素按顺序排列，而不是返回排序后的列表的副本
# print(a)
# print(b)
# print(a)
# print(a.index(3))  # 在列表中查找指定值第一次出现的索引
# print(a.count(3))  # 计算指定的元素在列表中出现的次数


# a.sort() #用于对列表就地排序，对原有的列表进行修改，使其元素按顺序排列，而不是返回排序后的列表的副本
# 高级排序：
# x = ["aadddw", "ddwdwqdwq", "wdwdwddsdsdsd", "wdwdw"]
# x.sort(key=len)
# x.sort(reverse=True)
# print(x)

# 为了获取排序后列表的副本
# # 方法一： 可使用sorted()函数
# x = [4, 5, 3, 1, 7, 8, ]
# y = sorted(x)  # sorted()函数可用于任何序列，但总是返回一个列表
# print(x)
# print(y)
# # 方法二：
# x = [4, 5, 3, 1, 7, 8, ]
# y = x.copy()
# y.sort()
# print(x)
# print(y)

#使用切片赋值还可在不替换原有元素的情况下插入新元素
number=[1,5]
number[1:1]=[2,3,4]
print(number)
