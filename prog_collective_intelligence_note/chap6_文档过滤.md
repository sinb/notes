##垃圾邮件分类器
使用统计的方法,需要构建训练集.
###特征
一封邮件首先要转为特征,这个特征是单词级别的.比如:
```
cl.train('the quick brown fox jumps over the lazy dog','good')
```
最简单的特征,一个词典,里面是出现过的单词,不记次数,只要出现过1次就记为1.比如:
```
{'hello': 1, 's': 1, 'up': 1, 'what': 1, 'world': 1}
```
当然,要过滤掉太长或者太短的.根据这个最简单的特征,就可以做统计然后训练了.比如可以统计出某单词出现在各个分类中的次数.如下.
```
{'python': {'bad': 0, 'good': 6}, 'the': {'bad': 3, 'good': 3}}
```
###训练
把一封邮件先拆成单词,通过这封邮件的训练,('quick','good')=1,对于good分类,曲线quick的次数是1.这个次数可以换算成频率(or概率).
换算成概率后得到类似如下信息,P('quick'|'good') = 0.66666,即便fprob('quick', 'good') = 0.6666.
这样会产生一些问题,在训练数据较少的情况下,比如某些中性词money,只出现在了一份垃圾邮件中,这样P('money'|'bad') = 1,对于bad分类出现money的概率为1.明显不合理,应该做一个加权的概率,即假设概率0.5.比如money出现在一篇bad邮件中,则加权后的概率为
```
(weight*assumedprob + count*fprob)/(count+weight)
= (1*1.0+1*0.5)/(1.0 + 1.0)
= 0.75
```
##最简单的分类器,朴素贝叶斯
假定一份邮件中出现各个单词相互独立,P(这封邮件|'bad') 等于所有单词概率的乘积.即便P(这封邮件|'bad') = P(word1|'bad')*P(word2|'bad')*P(word3|'bad')........P(wordn|'bad').
但我们最后要求的是P('bad'|这封邮件),要用贝叶斯定理.
Pr(A | B) = Pr(B | A) × Pr(A)/Pr(B)
贝叶斯定理放在这里就是
```
Pr(Category | Document) = Pr(Document | Category) × Pr(Category) / Pr(Document)
```
由于计算概率的目的是为了比较,所以可以忽略分母.
计算出P('bad'|邮件)和P('good'|邮件)比较一下就能分类了.
##给朴素贝叶斯分类器加入阈值
问题是,错误地把一份正常邮件分类为垃圾邮件会造成很大损伤,所以要加入阈值,即只有P('bad'|邮件) > 3 * P('good'|邮件)才能划分到bad中去,这个意思是bad的阈值设为3.good的阈值设为1表示只要P('good'|邮件) > P('bad'|邮件)就应该分类为good.如果P('good'|邮件) < P('bad'|邮件) < 3 * P('good'|邮件),则这个邮件应该被划分为未知.
实际实现的时候,如果是多分类问题,要让最大的P大于(阈值*次大的P)才能进行划分,否则返回默认('unknow'之类的).
所以垃圾邮件分类最后变成了3个类, good,bad,和unknown.
##Fisher方法
朴素贝叶斯假定各个单词之间相互独立,这样就能通过连乘计算联合概率.Fisher方法在这点上做了改进.
Fisher方法为文档中的每个特征都求得了属于某个类的概率,然后再组合.具体是这样做的.
```
Pr(category | feature)  = (number of documents in this category with the feature) / (total number of documents with the feature)
```
还需要做归一化.
```
clf = Pr(feature | category) for this category

freqsum = Sum of Pr(feature | category) for all the categories

cprob = clf / (clf+nclf)
```
然后概率组合,所有概率相乘,取-2log,去计算得到的这个东西属于chi-square分布的概率.这样做的原因是如果概率彼此独立且随机分布,这个结果就应该满足对数chi-square分布.
然后判断分类,对每个类设定阈值即可.
##持久化
之前所有的实验变量都没有存储,模型参数也没存储.持久化就是把特征全放进数据库,