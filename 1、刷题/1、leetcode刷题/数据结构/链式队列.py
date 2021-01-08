class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkListQueue:
    def __init__(self):
        """初始化一个空队列"""
        self.head = None
    def is_empty(self):
        """判断队列是否为空"""
        return self.head==None
    def enqueue(self,item):
        node=Node(item)
        # 空队列情况
        if self.is_empty():
            self.head=node
            return
        # 非空队列
        cur=self.head
        while cur.next:
            cur=cur.next
        # 循环结束后，cur一定是指向了元链表尾节点
        cur.next=node
        node.next=None
    def dequeue(self):
        """队头出队：相当于删除链表头结点"""
        if self.is_empty():
            raise Exception('dequeue from empty LinkListQueue')
        cur=self.head
        # 删除头结点
        self.head=self.head.next
        return cur.value
if __name__ == '__main__':
    q = LinkListQueue()
    # 队列: 100 200 300
    q.enqueue(100)
    q.enqueue(200)
    q.enqueue(300)
    # 终端1: 100
    print(q.dequeue())
    # 终端2: False
    print(q.is_empty())
