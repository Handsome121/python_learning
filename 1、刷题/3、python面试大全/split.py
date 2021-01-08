#将"k:1|k1:2|k3:3|k4:4"处理成字典
str1="k:1|k1:2|k3:3|k4:4"
def StrDict(str1):
    dict={}
    for item in str1.split("|"):
        key,value=item.split(":")
        dict[key]=int(value)
    return dict
print(StrDict(str1))