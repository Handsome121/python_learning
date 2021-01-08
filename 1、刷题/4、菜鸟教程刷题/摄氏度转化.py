'''
摄氏度和华氏度相互转换
'''
a=int(input("摄氏度转化为华氏度请按1\n华氏度转化为摄氏度请按2\n"))
while a!=1 and a!=2:
    print("你的输入不正确，请重新输入")
    a=int(input("摄氏度转化为华氏度请按1\n华氏度转化为摄氏度请按2\n"))
if a==1:
    celsius=float(input("输入摄氏度："))
    fahrenheit=(celsius*1.8)+32
    print("%.1f摄氏度转化为华氏度为：%(celsius,fahrenheit)")
else:
    fahrenheit = float(input('输入华氏度:'))
    celsius = (fahrenheit - 32) / 1.8  # 计算摄氏度
    print('%.1f华氏度转为摄氏度为%.1f' % (fahrenheit, celsius))

