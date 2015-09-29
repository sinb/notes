##垃圾邮件分类器
使用统计的方法,需要构建训练集.
一封邮件首先要转为特征,这个特征是单词级别的.比如:
```
cl.train('the quick brown fox jumps over the lazy dog','good')
```
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
所以垃圾邮件分类最后变成了3个类, good,bad,和unknown