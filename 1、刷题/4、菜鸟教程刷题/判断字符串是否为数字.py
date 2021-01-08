'''
以下实例通过创建自定义函数 is_number() 方法来判断字符串是否为数字：
'''
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)#把一个表示数字的字符串转换为浮点数返回。比如可以把‘8’，‘四’转换数值输出。
        # 与digit（）不一样的地方是它可以任意表示数值的字符都可以，不仅仅限于0到9的字符。
        # 如果不是合法字符，会抛出异常ValueError。
        return True
    except(TypeError,ValueError):
        pass
    return False
