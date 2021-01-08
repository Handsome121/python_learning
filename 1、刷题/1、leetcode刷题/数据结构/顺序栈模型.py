class Stack:
    def __init__(self):
        # 开辟一个顺序存储的模型空间
        # 列表的尾部表示栈顶
        self.elems = []

    def is_empty(self):
        """判断栈是否为空"""
        return self.elems == []
    def push(self,value):
        """入栈"""
        self.elems.append(value)
    def pop(self):
        """出栈"""
        if self.is_empty():
            raise StackError('pop from empty stack')
        # 弹出一个值并返回
        return self.elems.pop()
    def top(self):
        """查看栈顶元素"""
        if self.is_empty():
            raise StackError('pop from empty stack')
        return self.elems[-1]
if __name__ == '__main__':
    st = Stack()
    st.push(1)
    st.push(3)
    st.push(5)
    print(st.top())
    while not st.is_empty():
        print(st.pop())

