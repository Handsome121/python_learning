#  python多线程及线程同步方式

## 1、线程执行

- 1.子线程在主线程运行结束后，会继续执行完，如果给子线程设置为守护线程(setDaemon=True)，主线程运行结束子线程即结束；

- 2 .如果join()线程，那么主线程会等待子线程执行完再执行。

  ```python
  import threading
  import time
  
  
  def get_thread_a():
      print("get thread A started")
      time.sleep(3)
      print("get thread A end")
  
  
  def get_thread_b():
      print("get thread B started")
      time.sleep(5)
      print("get thread B end")
  
  
  if  __name__ == "__main__":
      thread_a = threading.Thread(target=get_thread_a)
      thread_b = threading.Thread(target=get_thread_b)
      start_time = time.time()
      thread_b.setDaemon(True)
      thread_a.start()
      thread_b.start()
      thread_a.join()   
  
      end_time = time.time()
      print("execution time: {}".format(end_time - start_time))
  ```

   thread_a是`join`，首先子线程thread_a执行，thread_b是守护线程，当主线程执行完后，thread_b不会再执行 

  ## 2.线程同步

 多线程间共享全局变量，多个线程对该变量执行不同的操作时，该变量最终的结果可能是不确定的(每次线程执行后的结果不同)，如：对count变量执行加减操作 ，count的值是不确定的，要想count的值是一个确定的需对线程执行的代码段加锁。 

## 3.线程同步的方式

### 3.1 锁机制

 ![img](图片/20190717093700554.png) 

 python对线程加锁主要有Lock和Rlock模块 

 **Lock：** 

```python
from threading import Lock
 
lock = Lock()
lock.acquire()
lock.release()
```

 **Lock有acquire()和release()方法，这两个方法必须是成对出现的，acquire()后面必须release()后才能再acquire()，否则会造成死锁** 

 **Rlock：** 

```python
from threading import RLock

lock = RLock()
lock.acquire()
lock.acquire()
lock.release()
lock.release()
```

 **鉴于Lock可能会造成死锁的情况，RLock(可重入锁)对Lock进行了改进，RLock可以在同一个线程里面连续调用多次acquire()，但必须再执行相同次数的release()** 

当一个线程调用锁的acquire()方法获得锁时，锁就进入“locked”状态。每次只有一个线程可以获得锁。如果此时另一个线程试图获得这个锁，该线程就会变为“blocked”状态，称为“同步阻塞”（参见多线程的基本概念）。

直到拥有锁的线程调用锁的release()方法释放锁之后，锁进入“unlocked”状态。线程调度程序从处于同步阻塞状态的线程中选择一个来获得锁，并使得该线程进入运行（running）状态

### 3.2 Semaphore(信号量)



信号量也提供acquire方法和release方法，每当调用acquire方法的时候，如果内部计数器大于0，则将其减1，如果内部计数器等于0，则会阻塞该线程，直到有线程调用了release方法将内部计数器更新到大于1位置。

Semaphore（信号量）是计算机科学史上最古老的同步指令之一。Semaphore管理一个内置的计数器，每当调用acquire()时-1，调用release() 时+1。计数器不能小于0；当计数器为0时，acquire()将阻塞线程至同步锁定状态，直到其他线程调用release()。

基于这个特点，Semaphore经常用来同步一些有“访客上限”的对象，比如连接池。

BoundedSemaphore 与Semaphore的唯一区别在于前者将在调用release()时检查计数器的值是否超过了计数器的初始值，如果超过了将抛出一个异常。

构造方法：
Semaphore(value=1): value是计数器的初始值。

```python
import time
import threading


def get_thread_a(semaphore,i):
    time.sleep(1)
    print("get thread : {}".format(i))
    semaphore.release()


def get_thread_b(semaphore):
    for i in range(10):
        semaphore.acquire()
        thread_a = threading.Thread(target=get_thread_a, args=(semaphore,i))
        thread_a.start()


if __name__ == "__main__":
    semaphore = threading.Semaphore(2)
    thread_b = threading.Thread(target=get_thread_b, args=(semaphore,))
    thread_b.start()
```

### 3.3 条件判断

 所谓条件变量，即这种机制是在满足了特定的条件后，线程才可以访问相关的数据。
  
它使用Condition类来完成，由于它也可以像锁机制那样用，所以它也有acquire方法和release方法，而且它还有wait，notify，notifyAll方法。 

 ![img](图片/20190717093630956.png) 

```python
"""
一个简单的生产消费者模型，通过条件变量的控制产品数量的增减，调用一次生产者产品就是+1，调用一次消费者产品就会-1.
"""

"""
使用 Condition 类来完成，由于它也可以像锁机制那样用，所以它也有 acquire 方法和 release 方法，而且它还有
wait， notify， notifyAll 方法。
"""

import threading
import queue,time,random

class Goods:#产品类
    def __init__(self):
        self.count = 0
    def add(self,num = 1):
        self.count += num
    def sub(self):
        if self.count>=0:
            self.count -= 1
    def empty(self):
        return self.count <= 0

class Producer(threading.Thread):#生产者类
    def __init__(self,condition,goods,sleeptime = 1):#sleeptime=1
        threading.Thread.__init__(self)
        self.cond = condition
        self.goods = goods
        self.sleeptime = sleeptime
    def run(self):
        cond = self.cond
        goods = self.goods
        while True:
            cond.acquire()#锁住资源
            goods.add()
            print("产品数量:",goods.count,"生产者线程")
            cond.notifyAll()#唤醒所有等待的线程--》其实就是唤醒消费者进程
            cond.release()#解锁资源
            time.sleep(self.sleeptime)

class Consumer(threading.Thread):#消费者类
    def __init__(self,condition,goods,sleeptime = 2):#sleeptime=2
        threading.Thread.__init__(self)
        self.cond = condition
        self.goods = goods
        self.sleeptime = sleeptime
    def run(self):
        cond = self.cond
        goods = self.goods
        while True:
            time.sleep(self.sleeptime)
            cond.acquire()#锁住资源
            while goods.empty():#如无产品则让线程等待
                cond.wait()
            goods.sub()
            print("产品数量:",goods.count,"消费者线程")
            cond.release()#解锁资源

g = Goods()
c = threading.Condition()

pro = Producer(c,g)
pro.start()

con = Consumer(c,g)
con.start()
```

Condition内部有一把锁，默认是RLock，在调用wait()和notify()之前必须先调用acquire()获取这个锁，才能继续执行；当wait()和notify()执行完后，需调用release()释放这个锁，在执行with condition时，会先执行acquire()，with结束时，执行了release()；所以condition有两层锁，最底层锁在调用wait()时会释放，同时会加一把锁到等待队列，等待notify()唤醒释放锁

wait() ：允许等待某个条件变量的通知，notify()可唤醒

notify()： 唤醒等待队列wait()

```python
# encoding: UTF-8
import threading
import time
 
# 商品
product = None
# 条件变量
con = threading.Condition()
 
# 生产者方法
def produce():
    global product
    
    if con.acquire():
        while True:
            if product is None:
                print 'produce...'
                product = 'anything'
                
                # 通知消费者，商品已经生产
                con.notify()
            
            # 等待通知
            con.wait()
            time.sleep(2)
 
# 消费者方法
def consume():
    global product
    
    if con.acquire():
        while True:
            if product is not None:
                print 'consume...'
                product = None
                
                # 通知生产者，商品已经没了
                con.notify()
            
            # 等待通知
            con.wait()
            time.sleep(2)
 
t1 = threading.Thread(target=produce)
t2 = threading.Thread(target=consume)
t2.start()
t1.start()
```

### 3.4 同步队列

put方法和task_done方法，queue有一个未完成任务数量num，put依次num+1，task依次num-1.任务都完成时任务结束。

 ![img](图片/2019071709360292.png) 

```python
import threading
import queue
import time
import random

'''
1.创建一个 Queue.Queue() 的实例，然后使用数据对它进行填充。
2.将经过填充数据的实例传递给线程类，后者是通过继承 threading.Thread 的方式创建的。
3.每次从队列中取出一个项目，并使用该线程中的数据和 run 方法以执行相应的工作。
4.在完成这项工作之后，使用 queue.task_done() 函数向任务已经完成的队列发送一个信号。
5.对队列执行 join 操作，实际上意味着等到队列为空，再退出主程序。
'''

class jdThread(threading.Thread):
    def __init__(self,index,queue):
        threading.Thread.__init__(self)
        self.index = index
        self.queue = queue

    def run(self):
        while True:
            time.sleep(1)
            item = self.queue.get()
            if item is None:
                break
            print("序号：",self.index,"任务",item,"完成")
            self.queue.task_done()#task_done方法使得未完成的任务数量-1

q = queue.Queue(0)
'''
初始化函数接受一个数字来作为该队列的容量，如果传递的是
一个小于等于0的数，那么默认会认为该队列的容量是无限的.
'''
for i in range(2):
    jdThread(i,q).start()#两个线程同时完成任务

for i in range(10):
    q.put(i)#put方法使得未完成的任务数量+1
```

### 3.5 Event对象

 Event对象是一种简单的线程同步通信技术，一个线程设置Event对象，另一个线程等待Event对象。 

 ![img](图片/20190717093352922.png) 

```python
import threading


# 自定义线程类
class MyThread(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self, name=thread_name)

    # 重写线程代码
    def run(self):
        global my_event
        if my_event.isSet():
            my_event.clear()
            # 等待通知
            my_event.wait()
            print(self.getName())
        else:
            print(self.getName())
            my_event.set()


# 创建锁
my_event = threading.Event()
my_event.set()
t1 = []

for i in range(10):
    t = MyThread(str(i))
    t1.append(t)

for t in t1:
    t.start()
```

