class Solution:
    def __init__(self):
        """先初始化两个空栈"""
        self.stack_a=[]
        self.stack_b=[]
    def push(self,item):
        """入队操作：相当于在栈stack_a中添加一个元素"""
        self.stack_a.append(item)
    def pop(self):
        """出队操作：相当于在stack_b中弹出一个元素"""
        # 先从栈stack_b中pop()出栈
        if self.stack_b:
            return self.stack_b.pop()
        # 栈stack_b为空时，把栈stack_a中所有的元素再添加到栈stack_b中
        while self.stack_a:
            self.stack_b.append(self.stack_a.pop())
        # 循环结束后，把stack_a中所有元素添加到了stack_b中
        if self.stack_b:
            return self.stack_b.pop()
if __name__ == '__main__':
    s = Solution()
    # 入队: 100 200 300
    s.push(100)
    s.push(200)
    s.push(300)
    # 出队: 100 200 300
    print(s.pop())
    print(s.pop())
    print(s.pop())