#判断输入字符串中每个字符出现的次数
str_input=input("请输入一个字符串：")
dict01={}
for i in str_input:
    if i not in dict01:
        dict01[i]=1
    else:
        dict01[i] += 1
for k,v in dict01.items():
    print("字符%s,%d次"%(k,v))
