class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def reverse_link_list(self, head):
        # 空链表情况
        if head == None:
            return
        # 非空链表
        pre = None
        cur = head
        while cur:
            # 记录下一个要操作反转的节点
            next_node=cur.next
            # 反转节点cur,并移动两个游标
            cur.next=pre
            pre=cur
            cur=next_node
        return pre.value
    
