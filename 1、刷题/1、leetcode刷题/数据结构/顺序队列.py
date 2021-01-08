class SQueue:
    def __init__(self):
        self.elems = []
    # 判断队列是否为空
    def is_empty(self):
        return self.elems == []

    # 入队
    def enqueue(self,val):
        self.elems.append(val)

    # 出队
    def dequeue(self):
        if not self._elems:
            raise Exception("Queue is empty")
        return self.elems.pop(0) # 弹出第一个数据
if __name__ == '__main__':
    sq = SQueue()
    sq.enqueue(10)
    sq.enqueue(20)
    sq.enqueue(30)
    while not sq.is_empty():
        print(sq.dequeue())