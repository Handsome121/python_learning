def get_fibonacci_sequence(length):
    """
        获取斐波那契数列
    :param length:数量长度
    :return:list类型，斐波那契数列。
    """
    sequence = [1, 1]
    for i in range(length - 2):
        sequence.append(sequence[-2] + sequence[-1])
    return sequence


# 测试：
print(get_fibonacci_sequence(20))
