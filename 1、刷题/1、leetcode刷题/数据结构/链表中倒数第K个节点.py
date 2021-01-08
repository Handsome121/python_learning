class Node:
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head, k) :
       # 把链表中的节点数据添加到列表中
        li=[]
        cur=head
        while cur:
            li.append(cur.value)
            cur=cur.next
        # 利用列表的索引取出对应值
        if k>len(li):
            raise IndexError('list index out of range')
        return li[-k]

if __name__ == '__main__':
    s = Solution()
    # 创建链表: 100 -> 200 -> 300 -> None
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    # 终端1: 200
    print(s.getKthFromEnd(head, 2))
    # 终端2: list index out of range
    print(s.getKthFromEnd(head, 8))