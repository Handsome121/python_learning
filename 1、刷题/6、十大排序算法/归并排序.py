"""归并排序"""


def merge_sort(li):
    # 递归出口:当切出来的列表长度为1时,返回
    if len(li) == 1:
        # print(li)
        return li
    # 1.分
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]
    # 递归思想
    left_li = merge_sort(left)
    right_li = merge_sort(right)
    # 2.合
    return merge(left_li, right_li)


def merge(left_li, right_li):
    """合并函数：将两个有序的列表合并成一个大列表"""
    result = []
    while left_li and right_li:
        if left_li[0] >= right_li[0]:
            result.append(right_li.pop(0))
        else:
            result.append(left_li.pop(0))
    # 循环结束后，一定有一个列表为空
    if left_li:
        result += right_li
    else:
        result += left_li
    return result

if __name__ == '__main__':
    result=merge_sort([6,3,4,5,6,7,0])
    print(result)


