class Node:
    """节点类"""

    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkList:
    """单链表类"""

    def __init__(self, node):
        self.head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.head == None

    def length(self):
        """获取链表长度"""
        # 游标：从头节点开始，一直往后移动，移动一次，+1
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.head
        while cur:
            print(cur.value, end=" ")
            cur = cur.next
        print()

    def add(self, item):
        """在链表头部增加一个节点"""
        node = Node(item)
        # 1、把新添加的节点指针指向原来头结点
        node.next = self.head
        # 2、添加的节点设置为新的头
        self.head = node

    def append(self, item):
        """在链表尾部添加一个节点，考虑空链表特殊情况"""
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            # 循环结束后，cur指向尾结点
            cur.next = node
            node.next = None

    def search(self, item):
        """查看链表中是否存在"""
        cur = self.head
        while cur:
            if cur.value == item:
                return True
            else:
                cur = cur.next
        return False

    def insert(self, pos, item):
        """在指定索引添加一个节点，索引值从0开始"""
        if pos < 0:
            self.add(item)
        elif pos>self.length()-1:
            self.append(item)
        else:
            pre=self.head
            count=0
            while count<(pos-1):
                count+=1
                pre=pre.next
                # 循环结束后，pos指向pos-1位置
                node=Node(item)
                node.next=pre.next
                pre.next=node
if __name__ == '__main__':
    s = SingleLinkList()
    # 终端1：True
    print(s.is_empty())
    # 链表：Node(100) -> Node(200) -> Node(300)
    s.add(200)
    s.add(100)
    s.append(300)
    # 终端2：3
    print(s.lengh())
    # 终端3：100 200 300
    s.travel()
    # 100 666 200 300
    s.insert(1, 666)
    # 终端4: 100 666 200 300
    s.travel()
    # 终端5: True
    print(s.search(666))