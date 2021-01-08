#统计词频
# colors=['1','2','2','1','3']
# result={}
# for color in colors:
#     if result.get(color)==None:
#         result[color]=1
#     else:
#         result[color]+=1
# print(result)
# ========================================================
# 计数器（Counter）：统计元素的个数，并以字典形式返回{元素：元素个数}
from collections import Counter
from collections import OrderedDict
str1='aaabbbccssddffff'
c=Counter(str1)
print(c)
# 将元素出现的次数按照从高到低进行排序，并返回前N个元素，若多个元素统计数相同，按照字母顺序排列，N若未指定，则返回所有元素
d=c.most_common(3)
print(d)
# 返回一个迭代器，元素被重复多少次，在迭代器中就包含多少个此元素，所有元素按字母序排列，个数<1的不罗列
c1=Counter(a=2,b=1,c=3,d=-1)
d1=c1.elements()
print(list(d1))
# 增加元素的重复次数
c.update('f')
print(c)
# 减少元素重复次数
c.subtract('abc')
print(c)
# 有序字典（orderedDict）：继承了dict的所有功能，dict是无序的，orderedDict刚好对dict作了补充，记录了键值对插入的顺序，是有序字典
dic=OrderedDict({'name': 'tom', 'age': 18, 'sex': 'man'})
print(dic)
# clear：清空字典
dic.clear()
print(dic)
# popitem：有序删除，类似于栈，按照后进先出的顺序依次删除
