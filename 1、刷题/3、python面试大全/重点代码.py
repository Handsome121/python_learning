# 1. 斐波那契数列：从第3项开始，每一项都等于前两项之和。
#    1, 1, 2, 3, 5, 8, 13, 21..
# 定义函数，根据长度获取斐波那契数列。
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


# 2. 定义函数，删除列表中所有重复的元素(重复元素只保留一个)。
# 输入：[4,35,7,64,7,35]
# 输出：[4, 35, 7, 64]

def delete_duplicates(target):
    """
        删除重复元素
    :param target: list类型，表示具有重复元素的数据
    """
    # 方法3：
    for r in range(len(target) - 1, -1, -1):
        for c in range(r):
            if target[r] == target[c]:
                del target[r]
                break


# 测试
list01 = [4, 35, 7, 64, 7, 35]
delete_duplicates(list01)
print(list01)

# 3. 定义函数，判断二维数字列表中是否存在某个数字
# 输入：二维列表、11
# 输出：True

list01 =[
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]


def is_exists(double_list, target):
    """
        判断二维列表中是否存在指定元素
    :param double_list:list类型，表示二维列表
    :param target:需要判断的元素
    :return:bool类型，是否存在。
    """
    for line in double_list:
        if target in line:
            return True
    return False


print(is_exists(list01, 18))

# 4. 定义函数，返回字符串中第一个不重复的字符。
# 输入：ABCACDBEFD
# 输出：E

"""
    定义函数，返回字符串中第一个不重复的字符。
    输入：ABCACDBEFD
    输出：E
"""


def first_not_repeating_char(target):
    dict_info = get_repeating_info(target)
    return get_key_for_value(dict_info, 1)


def get_repeating_info(target):
    dict_repeat_info = {}
    for char in target:
        dict_repeat_info[char] = target.count(char)
    # if char not in dict_repeat_info:
    #     dict_repeat_info[char] = 1
    # else:
    #     dict_repeat_info[char] += 1
    return dict_repeat_info


def get_key_for_value(target, value):
    for k, v in target.items():
        if v == value:
            return k


print(first_not_repeating_char("ABCACDBEFD"))

# 5.质数：大于1的整数，除了1和它本身以外不能再被其他数字整除。
#     定义函数，获取指定范围内的所有质数。
# 输入：2,20
# 输出：[2, 3, 5, 7, 11, 13, 17, 19]

"""
    质数：大于1的整数，除了1和它本身以外不能再被其他数字整除。
    定义函数，获取指定范围内的所有质数。
    输入：2,20
    输出：[2, 3, 5, 7, 11, 13, 17, 19]
"""


def is_prime(number):
    for item in range(2, number):
        if number % item == 0:
            return False
    return True


def get_prime(begin, end):
    # list_result = []
    # for num in range(begin, end):
    #     if is_prime(num):
    #         list_result.append(num)
    # return list_result
    return [num for num in range(begin, end) if is_prime(num)]


print(get_prime(2, 20))
