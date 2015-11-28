##Map Reduce设计模式
![](image/12.png)
像什么min/max,top 10,sampling啥的都可以用总结好的模式.参考书map reduce design pattern.
这些练习记录在[https://github.com/sinb/Map-Reduce-Recipe](https://github.com/sinb/Map-Reduce-Recipe).
##Combiners
Map在每个节点上计算出key value对,然后通过网络传输到reducer上.如果map的结果很琐碎,
比如都是('name', 2)之类,可以在map的节点上做pre-reduction,再把结果给reducer,减少网络传输.pre-reduction就是combiner.