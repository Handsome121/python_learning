class Node:
    """节点类"""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkListStack:
    def __init__(self):
        """初始化空栈"""
        self.head = None

    def is_empty(self):
        """判断是否为空栈"""
        return self.head == None

    def push(self, item):
        """入栈操作：相当于在链表的头部添加一个节点"""
        node = Node(item)
        node.next = self.head
        self.head=node
    def pop(self):
        """出栈操作：相当于删除链表头结点"""
        if self.is_empty():
            raise Exception('pop from empty LinkListStack')
        item = self.head.value
        self.head=self.head.next
        return item

