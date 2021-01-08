class Node:
    """链表节点类"""
    def __init__(self,x):
        self.value = x
        self.next = None

class Solution:
    # 返回从尾部到头部的序列，node为头结点
    def get_list_from_tail_to_head(self,node):
        array_list=[]
        while node:
            array_list.insert(0,node.value)
            node=node.next

        return array_list

if __name__ == '__main__':
	s = Solution()
	head = Node(100)
	head.next = Node(200)
	head.next.next = Node(300)
	print(s.get_list_from_tail_to_head(head))