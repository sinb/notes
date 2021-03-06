##爬虫
首先有一个url列表,对里面的每个url,下载它的html,将这个网页加入索引,同时找到这个网页里所有的link,检查这些link是否索引过,加入一个新的列表.这样重复几次(depth),就可以广度遍历到depth层的网页.
##索引
就是建立数据表.
![](images/4.png)
link表记录网页之间的跳转关系.
urllist记录所有的url.
wordlist记录所有的word.
wordlocation记录某单词在某url中出现的位置.
linkwords记录每个url里对应的word.
##查询,返回匹配的urlid,以及匹配单词的位置.
多词查询,针对每个单词都要查.
![](images/5.png)
比如查询了w0和w1,对应的查询语句是这样的.
查询结果为(urlid, 单词0的位置, 单词1的位置)
```
select w0.urlid,w0.location,w1.location
from wordlocation w0,wordlocation w1
where w0.urlid=w1.urlid
and w0.wordid=10
and w1.wordid=17
```
##排序,基于内容的排序
之返回结果对用户来说很不方便,因此还需要对结果进行排序.分为基于内容的排序和基于行为的排序.
但这里没有用TFIDF.
##单词频度
对于多次查询返回的匹配的行与位置进行处理,统计词频,排序后能够将词频高的url放前面.
##文档位置
对与查询的单词,统计所有出现位置的和,越小就说明这些单词越靠前,得分就越高.
##单词距离
查询的各个词之间应该距离相近.
##外部回指链接数
之前的搜索结果排序都利用的是网页本身的内容提取的特征.回指链接是指,指向这个网页的其它网页链接个数.这样可以防作弊,因为一些刷排名的网站虽然有其他方面优势,但不会被其他网站引用,所以这一项分很低.
##PageRank
PR利用了回指链接数目,给每个网页一个评分.这个评分理论上反映的是,一个用户点击这个网页的可能性.例如要计算下图网页A的PR,需要用到所有指向它的链接的PR,再做点处理得到.

![](images/6/png)
```
PR(A) = 0.15 + 0.85 * ( PR(B)/links(B) + PR(C)/links(C) + PR(D)/links(D) )
      = 0.15 + 0.85 * ( 0.5/4 + 0.7/5 + 0.2/1 )
      = 0.15 + 0.85 * ( 0.125 + 0.14 + 0.2)
      = 0.15 + 0.85 * 0.465
      = 0.54525
```
0.15是加上的最小值,0.85称为阻尼因子,是因为用户点一会就不想点了.后面是各个回指网页PR的归一化.PR的计算是个迭代过程,首先给所有网页一个初始PR值1,结果几十次迭代就能接近真实值.
在建立好其他表之后就能计算PR了,而且PR只在更新索引时才需要重新计算,其他时候用离线数据既可.
##利用链接的文本
由于指向一个网页的其它链接非常重要(如前所述,这一点不能作弊),那么就应该利用这些回指链接本身的文本.对于一组查询,去查询所有包含该单词的网页,如果这个网页链接就是指向最初查询返回结果的链接,就把该链接的PR加入到结果链接的PR中去.