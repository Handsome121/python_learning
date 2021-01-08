# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution:
    def reversePrint(self, head) :
        li=[]
        cur=head
        while cur:
            li.append(cur.value)
            cur=cur.next
        for i in range(len(li)-1,-1,-1):
            return li[i]

if __name__ == '__main__':
    s=Solution()
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    print(s.reversePrint(head))

