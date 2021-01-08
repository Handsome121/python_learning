"""
python实现快速排序
"""
def quick(li):
    quick_sort(li, 0, len(li)-1)

def quick_sort(li, first, last):
    # 递归出口
    if first >= last:
        return

    split_pos = sort(li, first, last)
    # 递归思想
    quick_sort(li, first, split_pos-1)
    quick_sort(li, split_pos+1, last)

def sort(li, first, last):
    """first:基准值的下标索引"""
    mid = li[first]
    lcur = first + 1
    rcur = last

    while True:
        # 左游标右移
        while lcur <= rcur and li[lcur] <= mid:
            lcur += 1
        # 右游标左移
        while lcur <= rcur and li[rcur] >= mid:
            rcur -= 1

        # 要么左右游标互换位置,要么右游标和基准值互换位置
        if lcur > rcur:
            li[rcur],li[first] = li[first],li[rcur]
            return rcur
        else:
            li[lcur],li[rcur] = li[rcur], li[lcur]

if __name__ == '__main__':
    li = [6,5,3,1,8,666,8,222,6,7,2,4]
    quick(li)
    print(li)














