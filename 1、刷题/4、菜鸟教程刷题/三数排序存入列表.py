"""
输入三个整数x,y,z，请把这三个数由小到大输出
"""
def sort_min_to_max(number):
    l=[]
    for i in range(number):
        x=int(input("请输入一个整数："))
        l.append(x)
    return l
l=sort_min_to_max(5)
print(l)


