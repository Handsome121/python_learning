class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head, value):
        # 如果头结点为空，直接返回
        if not head:
            return head
        # 如果头结点值等于value,直接返回head.next
        if head.value == value:
            return head.next
        # 定义一个指针
        cur = head
        while cur.next:
            if cur.next.value == value:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head
    