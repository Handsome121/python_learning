# 倒序输入字符
# 写法一
msg = input("请输入一个字符串：")
list01 = []
for i in range(len(msg)):
    list01.append(msg[i])
for x in range(len(list01)//2):
    list01[x], list01[len(list01) - 1 - x] = list01[len(list01) - 1 - x], list01[x]
result = "".join(list01)
print(result)
#写法二
msg = input("请输入一个字符串：")
# list02=[msg[i] for i in range(len(msg))]
list02=list(msg)
result="".join(list02[::-1])
print(result)
#写法三
msg=input("请输入一句英文：")
list03=msg.split(" ")
result=" ".join(list03[::-1])
print(result)

