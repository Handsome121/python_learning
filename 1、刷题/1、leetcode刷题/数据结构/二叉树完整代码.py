"""python实现二叉树"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, node=None):
        """创建了一棵空树或者只有树根的树"""
        self.root = node

    def add(self, value):
        """在树中添加一个节点"""
        node = Node(value)
        # 空树情况
        if self.root == None:
            self.root = node
            return
            # 不是空树的情况
        node_list = [self.root]
        while node_list:
            cur = node_list.pop(0)
            # 判断左孩子
            if cur.left is None:
                cur.left = node
                return
            else:
                node_list.append(cur.left)
                # 判断右孩子
            if cur.right is None:
                cur.right = node
                return
            else:
                node_list.append(cur.right)

    def breadth_travel(self):
        """广度遍历-队列思想（即：列表的append方法和pop(0)方法）"""
        # 空树的情况
        if self.root == None:
            return
            # 非空树的情况
        node_list = [self.root]
        while node_list:
            cur = node_list.pop(0)
            print(cur.value, end='')
            # 添加左孩子
            if cur.left is not None:
                node_list.append(cur.left)
            # 添加右孩子
            if cur.right is not None:
                node_list.append(cur.right)

        print()

    def pre_travel(self, node):
        """根左右"""
        if node is None:
            return
        print(node.value, end=" ")
        self.pre_travel(node.left)
        self.pre_travel(node.right)

    def mid_travel(self, node):
        """中序遍历-左根右"""
        self.mid_travel(node.left)
        print(node.value, end=" ")
        self.mid_travel(node.right)

    def last_travel(self, node):
        """后序遍历-左右根"""
        self.last_travel(node.left)
        self.last_travel(node.right)
        print(node.value, end=" ")


if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.add(10)
    # 广度遍历：1 2 3 4 5 6 7 8 9 10
    tree.breadth_travel()
    # 前序遍历：1 2 4 8 9 5 10 3 6 7
    tree.pre_travel(tree.root)
    print()
    # 中序遍历:8 4 9 2 10 5 1 6 3 7
    tree.mid_travel(tree.root)
    print()
    # 后序遍历：8 9 4 10 5 2 6 7 3 1
    tree.last_travel(tree.root)
