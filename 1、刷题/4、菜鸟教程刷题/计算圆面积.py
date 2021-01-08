'''圆的面积公式为 ：
公式中 r 为圆的半径。
'''
def findArea(r):
    PI=3.142
    return PI*(r**2)
print("圆的面积为：%.3f"%findArea(5))