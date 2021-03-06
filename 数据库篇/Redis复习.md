## Redis（Remote Dictionary Server）为什么快呢？

```
redis的速度非常的快，单机的redis就可以支撑每秒10几万的并发，相对于mysql来说，性能是mysql的几十倍。速度快的原因主要有几点：
1. 完全基于内存操作
2. C语言实现，优化过的数据结构，基于几种基础的数据结构，redis做了大量的优化，性能极高
3. 使用单线程，无上下文的切换成本
4. 基于非阻塞的IO多路复用机制
```

![](C:\Users\未来我来\AppData\Roaming\Typora\typora-user-images\image-20201205151419168.png)

**高效的数据结构**

![image-20201215103522399](C:/Users/未来我来/AppData/Roaming/Typora/typora-user-images/image-20201215103522399.png)

**1、简单动态字符串**

这个名词可能你不熟悉，换成 **SDS** 肯定就知道了。这是用来处理字符串的。了解 C 语言的都知道，它是有处理字符串方法的。而 Redis 就是 C 语言实现的，那为什么还要重复造轮子？我们从以下几点来看：

**（1）字符串长度处理**

![image-20201215103754845](C:/Users/未来我来/AppData/Roaming/Typora/typora-user-images/image-20201215103754845.png)

这个图是字符串在 C 语言中的存储方式，想要获取 「Redis」的长度，需要从头开始遍历，直到遇到 '\0' 为止。

![image-20201215103809955](C:/Users/未来我来/AppData/Roaming/Typora/typora-user-images/image-20201215103809955.png)

Redis 中怎么操作呢？用一个 len 字段记录当前字符串的长度。想要获取长度只需要获取 len 字段即可。你看，差距不言自明。前者遍历的时间复杂度为 O(n)，Redis 中 O(1) 就能拿到，速度明显提升。

**（2）内存重新分配**

C 语言中涉及到修改字符串的时候会重新分配内存。修改地越频繁，内存分配也就越频繁。而内存分配是会消耗性能的，那么性能下降在所难免。

而 Redis 中会涉及到字符串频繁的修改操作，这种内存分配方式显然就不适合了。于是 SDS 实现了两种优化策略：

- **空间预分配**

对 SDS 修改及空间扩充时，除了分配所必须的空间外，还会额外分配未使用的空间。

具体分配规则是这样的：SDS 修改后，len 长度小于 1M，那么将会额外分配与 len 相同长度的未使用空间。如果修改后长度大于 1M，那么将分配1M的使用空间。

- **惰性空间释放**

当然，有空间分配对应的就有空间释放。

SDS 缩短时，并不会回收多余的内存空间，而是使用 free 字段将多出来的空间记录下来。如果后续有变更操作，直接使用 free 中记录的空间，减少了内存的分配。

**（3）二进制安全**

你已经知道了 Redis 可以存储各种数据类型，那么二进制数据肯定也不例外。但二进制数据并不是规则的字符串格式，可能会包含一些特殊的字符，比如 '\0' 等。

前面我们提到过，C 中字符串遇到 '\0' 会结束，那 '\0' 之后的数据就读取不上了。但在 SDS 中，是根据 len 长度来判断字符串结束的。

看，二进制安全的问题就解决了。

**2、双端链表**

列表 List 更多是被当作队列或栈来使用的。队列和栈的特性一个先进先出，一个先进后出。双端链表很好的支持了这些特性。

![image-20201215104243372](C:/Users/未来我来/AppData/Roaming/Typora/typora-user-images/image-20201215104243372.png)

**（1）前后节点**

![image-20201215104330508](C:/Users/未来我来/AppData/Roaming/Typora/typora-user-images/image-20201215104330508.png)

链表里每个节点都带有两个指针，prev 指向前节点，next 指向后节点。这样在时间复杂度为 O(1) 内就能获取到前后节点。

**（2）头尾节点**

![image-20201215104352227](C:/Users/未来我来/AppData/Roaming/Typora/typora-user-images/image-20201215104352227.png)你可能注意到了，头节点里有 head 和 tail 两个参数，分别指向头节点和尾节点。这样的设计能够对双端节点的处理时间复杂度降至 O(1) ，对于队列和栈来说再适合不过。同时链表迭代时从两端都可以进行。

**（3）链表长度**

头节点里同时还有一个参数 len，和上边提到的 SDS 里类似，这里是用来记录链表长度的。因此获取链表长度时不用再遍历整个链表，直接拿到 len 值就可以了，这个时间复杂度是 O(1)。

你看，这些特性都降低了 List 使用时的时间开销。

**3、压缩列表**

双端链表我们已经熟悉了。不知道你有没有注意到一个问题：如果在一个链表节点中存储一个小数据，比如一个字节。那么对应的就要保存头节点，前后指针等额外的数据。

这样就浪费了空间，同时由于反复申请与释放也容易导致内存碎片化。这样内存的使用效率就太低了。

于是，压缩列表上场了！

![image-20201215104512814](C:/Users/未来我来/AppData/Roaming/Typora/typora-user-images/image-20201215104512814.png)它是经过特殊编码，专门为了提升内存使用效率设计的。所有的操作都是通过指针与解码出来的偏移量进行的。

并且压缩列表的内存是连续分配的，遍历的速度很快。

**4、字典**

Redis 作为 K-V 型数据库，所有的键值都是用字典来存储的。

日常学习中使用的字典你应该不会陌生，想查找某个词通过某个字就可以直接定位到，速度非常快。这里所说的字典原理上是一样的，通过某个 key 可以直接获取到对应的value。

字典又称为哈希表，这点没什么可说的。哈希表的特性大家都很清楚，能够在 O(1) 时间复杂度内取出和插入关联的值。

**5、跳跃表**

作为 Redis 中特有的数据结构-跳跃表，其在链表的基础上增加了多级索引来提升查找效率。

![image-20201215104621734](C:/Users/未来我来/AppData/Roaming/Typora/typora-user-images/image-20201215104621734.png)



这是跳跃表的简单原理图，每一层都有一条有序的链表，最底层的链表包含了所有的元素。这样跳跃表就可以支持在 O(logN) 的时间复杂度里查找到对应的节点。

下面这张是跳表真实的存储结构，和其它数据结构一样，都在头节点里记录了相应的信息，减少了一些不必要的系统开销。

**合理的数据编码**

对于每一种数据类型来说，底层的支持可能是多种数据结构，什么时候使用哪种数据结构，这就涉及到了编码转化的问题。

那我们就来看看，不同的数据类型是如何进行编码转化的：

**String**：存储数字的话，采用int类型的编码，如果是非数字的话，采用 raw 编码；

**List**：字符串长度及元素个数小于一定范围使用 ziplist 编码，任意条件不满足，则转化为 linkedlist 编码；

**Hash**：hash 对象保存的键值对内的键和值字符串长度小于一定值及键值对；

**Set**：保存元素为整数及元素个数小于一定范围使用 intset 编码，任意条件不满足，则使用 hashtable 编码；

**Zset**：zset 对象中保存的元素个数小于及成员长度小于一定值使用 ziplist 编码，任意条件不满足，则使用 skiplist 编码。



## 那为什么Redis6.0之后又改用多线程呢?

```
redis使用多线程并非是完全摒弃单线程，redis还是使用单线程模型来处理客户端的请求，只是使用多线程来处理数据的读写和协议解析，执行命令还是使用单线程。
这样做的目的是因为redis的性能瓶颈在于网络IO而非CPU，使用多线程能提升IO读写的效率，从而整体提高redis的性能。
```

## 知道什么是热key吗？热key问题怎么解决？

```
所谓热key问题就是，突然有几十万的请求去访问redis上的某个特定key，那么这样会造成流量过于集中，达到物理网卡上限，从而导致这台redis的服务器宕机引发雪崩。
针对热key的解决方案：
1、提前把热key打散到不同的服务器，降低压力
2、加入二级缓存，提前加载热key数据到内存中，如果redis宕机，走内存查询
```

## 什么是缓存击穿、缓存穿透、缓存雪崩？

**缓存击穿[单个key并发访问过高，过期时导致所有请求打到db上]**

```
	缓存击穿的概念就是单个key并发访问过高，过期时导致所有请求直接打到db上，这个和热key的问题比较类似，只是说的点在于过期导致请求全部打到DB上而已。
解决方案：
1、加锁更新，比如请求查询A，发现缓存中没有，对A这个key加锁，同时去数据库查询数据，写入缓存，再返回给用户，这样后面的请求就可以从缓存中拿到数据了。
2、将过期时间组合写在value中，通过异步的方式不断的刷新过期时间，防止此类现象。
```

**缓存穿透[查询不存在缓存中的数据]**

缓存穿透的概念很简单，用户想要查询一个数据，发现redis内存数据库没有，也就是缓存没有命中，于是向持久层数据库查询。发现也没有，于是本次查询失败。当用户很多的时候，缓存都没有命中，于是都去请求了持久层数据库。这会给持久层数据库造成很大的压力，这时候就相当于出现了缓存穿透。



这里需要注意和缓存击穿的区别，缓存击穿，是指一个key非常热点，在不停的扛着大并发，大并发集中对这一个点进行访问，当这个key在失效的瞬间，持续的大并发就穿破缓存，直接请求数据库，就像在一个屏障上凿开了一个洞。

```
针对这个问题，加一层布隆过滤器。布隆过滤器的原理是在你存入数据的时候，会通过散列函数将它映射为一个位数组中的K个点，同时把他们置为1。
这样当用户再次来查询A，而A在布隆过滤器值为0，直接返回，就不会产生击穿请求打到DB了。
显然，使用布隆过滤器之后会有一个问题就是误判，因为它本身是一个数组，可能会有多个值落到同一个位置，那么理论上来说只要我们的数组长度够长，误判的概率就会越低，这种问题就根据实际情况来就好了。
```

**缓存雪崩[大规模缓存失效]**

```
当某一时刻发生大规模的缓存失效的情况，比如你的缓存服务宕机了，会有大量的请求进来直接打到DB上，这样可能导致整个系统的崩溃，称为雪崩。雪崩和击穿、热key的问题不太一样的是，他是指大规模的缓存都过期失效了。
针对雪崩几个解决方案：
1、针对不同key设置不同的过期时间，避免同时过期
2、限流，如果redis宕机，可以限流，避免同时刻大量请求打崩DB
3、二级缓存，同热key的方案。
```

## Redis的过期策略有哪些？

**惰性删除**

```
惰性删除指的是当我们查询key的时候才对key进行检测，如果已经达到过期时间，则删除。显然，他有一个缺点就是如果这些过期的key没有被访问，那么他就一直无法被删除，而且一直占用内存。
```

 **定期删除**

```
定期删除指的是redis每隔一段时间对数据库做一次检查，删除里面的过期key。由于不可能对所有key去做轮询来删除，所以redis会每次随机取一些key去做检查和删除。
```

#### 那么定期+惰性都没有删除过期的key怎么办？

```
假设redis每次定期随机查询key的时候没有删掉，这些key也没有做查询的话，就会导致这些key一直保存在redis里面无法被删除，这时候就会走到redis的内存淘汰机制。
1、volatile-lru：从已设置过期时间的key中，移出最近最少使用的key进行淘汰
2、volatile-ttl：从已设置过期时间的key中，移出将要过期的key
3、volatile-random：从已设置过期时间的key中随机选择key淘汰
4、allkeys-lru：从key中选择最近最少使用的进行淘汰
5、allkeys-random：从key中随机选择key进行淘汰
6、noeviction：当内存达到阈值的时候，新写入操作报错
```

## 持久化方式有哪些？有什么区别？

**RDB**[保存数据]

```
RDB持久化可以手动执行也可以根据配置定期执行，它的作用是将某个时间点上的数据库状态保存到RDB文件中，RDB文件是一个压缩的二进制文件，通过它可以还原某个时刻数据库的状态。由于RDB文件是保存在硬盘上的，所以即使redis崩溃或者退出，只要RDB文件存在，就可以用它来恢复还原数据库的状态。
可以通过SAVE或者BGSAVE来生成RDB文件。
SAVE命令会阻塞redis进程，直到RDB文件生成完毕，在进程阻塞期间，redis不能处理任何命令请求，这显然是不合适的。
BGSAVE则是会fork出一个子进程，然后由子进程去负责生成RDB文件，父进程还可以继续处理命令请求，不会阻塞进程。
```

**AOF**[保存命令]

```
AOF和RDB不同，AOF是通过保存redis服务器所执行的写命令来记录数据库状态的。
AOF通过追加、写入、同步三个步骤来实现持久化机制。
当AOF持久化处于激活状态，服务器执行完写命令之后，写命令将会被追加append到aof_buf缓冲区的末尾
在服务器每结束一个事件循环之前，将会调用flushAppendOnlyFile函数决定是否要将aof_buf的内容保存到AOF文件中，可以通过配置appendfsync来决定。
    always ##aof_buf内容写入并同步到AOF文件
    everysec ##将aof_buf中内容写入到AOF文件，如果上次同步AOF文件时间距离现在超过1秒，则再次对AOF文件进行同步
    no ##将aof_buf内容写入AOF文件，但是并不对AOF文件进行同步，同步时间由操作系统决定
如果不设置，默认选项将会是everysec，因为always来说虽然最安全（只会丢失一次事件循环的写命令），但是性能较差，而everysec模式只不过会可能丢失1秒钟的数据，而no模式的效率和everysec相仿，但是会丢失上次同步AOF文件之后的所有写命令数据。
```

**RDB和AOF持久化对比**【重点】

| RDB持久化                                                    | AOF持久化                                     |
| ------------------------------------------------------------ | --------------------------------------------- |
| 全量备份，一次保存整个数据库                                 | 增量备份，一次保存一个修改数据库的命令        |
| 保存的间隔较长                                               | 保存的间隔默认为一秒钟                        |
| 数据还原速度快                                               | 数据还原速度一般，冗余命令多，还原速度慢      |
| 执行SAVE命令时会阻塞服务器，但手动或者自动触发的BGSAVE不会阻塞服务器 | 无论是平时还是进行AOF重写时，都不会阻塞服务器 |

## 怎么实现Redis的高可用？

**主从架构**

```
主从模式是最简单的实现高可用的方案，核心就是主从同步。主从同步的原理如下：
1、slave发送sync命令到master
2、master收到sync之后，执行bgsave，生成RDB全量文件
3、master把slave的写命令记录到缓存
4、bgsave执行完毕之后，发送RDB文件到slave，slave执行
5、master发送缓存中的写命令到slave，slave执行
```

**哨兵**

```
基于主从方案的缺点还是很明显的，假设master宕机，那么就不能写入数据，那么slave也就失去了作用，整个架构就不可用了，除非你手动切换，主要原因就是因为没有自动故障转移机制。而哨兵(sentinel)的功能比单纯的主从架构全面的多了，它具备自动故障转移、集群监控、消息通知等功能。
```

```
哨兵可以同时监视多个主从服务器，并且在被监视的master下线时，自动将某个slave提升为master，然后由新的master继续接收命令。整个过程如下：
初始化sentinel，将普通的redis代码替换成sentinel专用代码
初始化masters字典和服务器信息，服务器信息主要保存ip:port，并记录实例的地址和ID
创建和master的两个连接，命令连接和订阅连接，并且订阅sentinel:hello频道
每隔10秒向master发送info命令，获取master和它下面所有slave的当前信息
当发现master有新的slave之后，sentinel和新的slave同样建立两个连接，同时每个10秒发送info命令，更新master信息
sentinel每隔1秒向所有服务器发送ping命令，如果某台服务器在配置的响应时间内连续返回无效回复，将会被标记为下线状态
选举出领头sentinel，领头sentinel需要半数以上的sentinel同意
领头sentinel从已下线的的master所有slave中挑选一个，将其转换为master
让所有的slave改为从新的master复制数据
将原来的master设置为新的master的从服务器，当原来master重新回复连接时，就变成了新master的从服务器
```

```
sentinel会每隔1秒向所有实例（包括主从服务器和其他sentinel）发送ping命令，并且根据回复判断是否已经下线，这种方式叫做主观下线。当判断为主观下线时，就会向其他监视的sentinel询问，如果超过半数的投票认为已经是下线状态，则会标记为客观下线状态，同时触发故障转移。
```

## 能说说redis集群的原理吗？

```
如果说依靠哨兵可以实现redis的高可用，如果还想在支持高并发同时容纳海量的数据，那就需要redis集群。redis集群是redis提供的分布式数据存储方案，集群通过数据分片sharding来进行数据的共享，同时提供复制和故障转移的功能。
```

**节点**

```
一个redis集群由多个节点node组成，而多个node之间通过cluster meet命令来进行连接，节点的握手过程：
节点A收到客户端的cluster meet命令
A根据收到的IP地址和端口号，向B发送一条meet消息
节点B收到meet消息返回pong
A知道B收到了meet消息，返回一条ping消息，握手成功
最后，节点A将会通过gossip协议把节点B的信息传播给集群中的其他节点，其他节点也将和B进行握手
```

**槽slot**

```
redis通过集群分片的形式来保存数据，整个集群数据库被分为16384个slot，集群中的每个节点可以处理0-16384个slot，当数据库16384个slot都有节点在处理时，集群处于上线状态，反之只要有一个slot没有得到处理都会处理下线状态。通过cluster addslots命令可以将slot指派给对应节点处理。
slot是一个位数组，数组的长度是16384/8=2048，而数组的每一位用1表示被节点处理，0表示不处理，如图所示的话表示A节点处理0-7的slot。
当客户端向节点发送命令，如果刚好找到slot属于当前节点，那么节点就执行命令，反之，则会返回一个MOVED命令到客户端指引客户端转向正确的节点。（MOVED过程是自动的）
如果增加或者移出节点，对于slot的重新分配也是非常方便的，redis提供了工具帮助实现slot的迁移，整个过程是完全在线的，不需要停止服务。
```

**故障转移**

```
如果节点A向节点B发送ping消息，节点B没有在规定的时间内响应pong，那么节点A会标记节点B为pfail疑似下线状态，同时把B的状态通过消息的形式发送给其他节点，如果超过半数以上的节点都标记B为pfail状态，B就会被标记为fail下线状态，此时将会发生故障转移，优先从复制数据较多的从节点选择一个成为主节点，并且接管下线节点的slot，整个过程和哨兵非常类似，都是基于Raft协议做选举。
```

## 了解Redis事务机制吗？

```
redis通过MULTI、EXEC、WATCH等命令来实现事务机制，事务执行过程将一系列多个命令按照顺序一次性执行，并且在执行期间，事务不会被中断，也不会去执行客户端的其他请求，直到所有命令执行完毕。事务的执行过程如下：
服务端收到客户端请求，事务以MULTI开始
如果客户端正处于事务状态，则会把事务放入队列同时返回给客户端QUEUED，反之则直接执行这个命令
当收到客户端EXEC命令时，WATCH命令监视整个事务中的key是否有被修改，如果有则返回空回复到客户端表示失败，否则redis会遍历整个事务队列，执行队列中保存的所有命令，最后返回结果给客户端
WATCH的机制本身是一个CAS的机制，被监视的key会被保存到一个链表中，如果某个key被修改，那么REDIS_DIRTY_CAS标志将会被打开，这时服务器会拒绝执行事务。
```

## Redis 和数据库双写一致性问题

```
一致性问题是分布式常见问题，还可以再分为最终一致性和强一致性。数据库和缓存双写，就必然会存在不一致的问题。

答这个问题，先明白一个前提。就是如果对数据有强一致性要求，不能放缓存。我们所做的一切，只能保证最终一致性。

另外，我们所做的方案从根本上来说，只能说降低不一致发生的概率，无法完全避免。因此，有强一致性要求的数据，不能放缓存。

回答：首先，采取正确更新策略，先更新数据库，再删缓存。其次，因为可能存在删除缓存失败的问题，提供一个补偿措施即可，例如利用消息队列。
```

## 缓存更新策略（即如何让缓存和mysql保持一致性）？

##### key过期清除（超时剔除）策略

```
惰性过期（类比懒加载，这是懒过期）：只有当访问一个key时，才会判断该key是否已过期，过期则清除。该策略可以最大化地节省CPU资源，却对内存非常不友好。极端情况可能出现大量的过期key没有再次被访问，从而不会被清除，占用大量内存。
定期过期：每隔一定的时间，会扫描一定数量的数据库的expires字典中一定数量的key，并清除其中已过期的key。该策略是前两者的一个折中方案。通过调整定时扫描的时间间隔和每次扫描的限定耗时，可以在不同情况下使得CPU和内存资源达到最优的平衡效果。
```

(expires字典会保存所有设置了过期时间的key的过期时间数据，其中，key是指向键空间中的某个键的指针，value是该键的毫秒精度的UNIX时间戳表示的过期时间。键空间是指该Redis集群中保存的所有键。)
问：比如这么个场景，我设计了很多key，过期时间是5分钟，当前内存占用率是50%。但是5分钟到了，内存占用率还是很高，请问为什么？
Redis中同时使用了惰性过期和定期过期两种过期策略，即使过期时间到了，但是有部分并没有真正删除，等待惰性删除。
为什么有定期还要有惰性呢？其实很简单，比如10万个key就要过期了，Redis默认是100ms检查一波。如果他检查出10万个即将要清除，那他接下来的时间基本都是在干这些清空内存的事了，那肯定影响性能，所以他只会部分删除，剩下的等惰性。



## 如何解决 Redis 的并发竞争 Key 问题

**如果对这个 Key 操作，不要求顺序**

```
这种情况下，准备一个分布式锁，大家去抢锁，抢到锁就做 set 操作即可，比较简单。
```

**如果对这个 Key 操作，要求顺序**

```
假设有一个 key1，系统 A 需要将 key1 设置为 valueA，系统 B 需要将 key1 设置为 valueB，系统 C 需要将 key1 设置为 valueC。

期望按照 key1 的 value 值按照 valueA > valueB > valueC 的顺序变化。这种时候我们在数据写入数据库的时候，需要保存一个时间戳。
那么，假设这会系统 B 先抢到锁，将 key1 设置为{valueB 3:05}。接下来系统 A 抢到锁，发现自己的 valueA 的时间戳早于缓存中的时间戳，那就不做 set 操作了，以此类推。

其他方法，比如利用队列，将 set 方法变成串行访问也可以。总之，灵活变通。
```

## 为什么Redis 需要把所有数据放到内存中？

```
Redis 为了达到最快的读写速度将数据都读到内存中，并通过异步的方式将数据写入磁盘。所以Redis 具有快速和数据持久化的特征。如果不将数据放在内存中，磁盘I/O 速度为严重影响Redis 的性能。在内存越来越便宜的今天，Redis 将会越来越受欢迎。如果设置了最大使用的内存，则数据已有记录数达到内存限值后不能继续插入新值。
```

## MySQL 里有2000w 数据，Redis 中只存20w 的数据，如何保证Redis 中的数据都是热点数据？、

```
Redis 内存数据集大小上升到一定大小的时候，就会施行数据淘汰策略。
```

## Redis 集群的主从复制模型是怎样的？

```
为了使在部分节点失败或者大部分节点无法通信的情况下集群仍然可用，所以集群使用了主从复制模型,每个节点都会有N-1 个复制品.
```

## Redis 集群会有写操作丢失吗？为什么？

```
Redis 并不能保证数据的强一致性，这意味这在实际中集群在特定的条件下可能会丢失写操作。
```

## Redis 集群之间是如何复制的？

```
异步复制
```

## Redis 集群最大节点个数是多少？

```
16384 个。
```

## Redis的内存淘汰策略

```
Redis的内存淘汰策略是指在Redis的用于缓存的内存不足时，怎么处理需要新写入且需要申请额外空间的数据
1、noeviction：当内存不足以容纳新写入数据时，新写入操作会报错。
2、allkeys-lru：当内存不足以容纳新写入数据时，在键空间中，移除最近最少使用的key，使用最多
3、allkeys-random：当内存不足以容纳新写入数据时，在键空间中，随机移除某个key。
4、volatile-lru：当内存不足以容纳新写入数据时，在设置了过期时间的键空间中，移除最近最少使用的key。
5、volatile-random：当内存不足以容纳新写入数据时，在设置了过期时间的键空间中，随机移除某个key。
6、volatile-ttl：当内存不足以容纳新写入数据时，在设置了过期时间的键空间中，有更早过期时间的key优先移除。
```

## **Redis五大数据类型及应用场景**

| 类型       | 特点                                                         | 使用场景                                                     | 具体数据类型                                                 |
| :--------- | :----------------------------------------------------------- | :----------------------------------------------------------- | ------------------------------------------------------------ |
| string     | 简单key-value类型，value可为字符串和数字                     | 常规计数（微博数, 粉丝数等功能）短信验证码                   | 字符串对象string：int整数、embstr编码的简单动态字符串、raw简单动态字符串 |
| hash       | 是一个string类型的field和value的映射表，hash特别适合用于存储对象 | 存储部分可能需要变更的数据（比如用户信息）                   | 哈希对象hash：ziplist、hashtable                             |
| list       | 有序可重复列表                                               | 消息队列等,常用于生产者消费者模型                            | 列表对象list：ziplist、linkedlist                            |
| set        | 无序不可重复列表                                             | 存储并计算关系（如微博，关注人或粉丝存放在集合，可通过交集、并集、差集等操作实现如共同关注、共同喜好等功能） | 集合对象set：intset、hashtable                               |
| sorted set | 每个元素带有分值的集合                                       | 各种排行榜                                                   | 有序集合对象zset：ziplist、skiplist                          |

## 为什么要用 redis /为什么要用缓存

主要从“高性能”和“高并发”这两点来看待这个问题。

**高性能：**

假如用户第一次访问数据库中的某些数据。这个过程会比较慢，因为是从硬盘上读取的。将该用户访问的数据存在数缓存中，这样下一次再访问这些数据的时候就可以直接从缓存中获取了。操作缓存就是直接操作内存，所以速度相当快。如果数据库中的对应数据改变的之后，同步改变缓存中相应的数据即可！

**高并发：**

直接操作缓存能够承受的请求是远远大于直接访问数据库的，所以我们可以考虑把数据库中的部分数据转移到缓存中去，这样用户的一部分请求会直接到缓存这里而不用经过数据库。

## redis 和 memcached 的区别

对于 redis 和 memcached 我总结了下面四点。现在公司一般都是用 redis 来实现缓存，而且 redis 自身也越来越强大了！

1. **redis支持更丰富的数据类型（支持更复杂的应用场景）**：Redis不仅仅支持简单的k/v类型的数据，同时还提供list，set，zset，hash等数据结构的存储。memcache支持简单的数据类型，String。
2. **Redis支持数据的持久化，可以将内存中的数据保持在磁盘中，重启的时候可以再次加载进行使用,而Memecache把数据全部存在内存之中。**
3. **集群模式**：memcached没有原生的集群模式，需要依靠客户端来实现往集群中分片写入数据；但是redis目前是原生支持cluster模式的，redis官方就是支持redis cluster集群模式的，比memcached来说要更好。
4. **Memcached是多线程，非阻塞IO复用的网络模型；Redis使用单线程的多路 IO 复用模型。**