##垃圾邮件分类器
使用统计的方法,需要构建训练集.
一封邮件首先要转为特征,这个特征是单词级别的.比如:
```
cl.train('the quick brown fox jumps over the lazy dog','good')
```
把一封邮件先拆成单词,通过这封邮件的训练,('quick','good')=1,即出现quick并且该邮件是垃圾邮件的次数是1.这个次数可以换算成频率,
