##监督学习算法
###贝叶斯分类器
记住两个,首先要用到贝叶斯公式.
```
Pr(Category | Document) = Pr(Document | Category) * Pr(Category) / Pr(Document)
```
然后是假设所有单词的出现相互独立.
```
Pr (Document | Category) = Pr(Word1 | Category) * Pr(Word2 | Category) * ...
####优缺点
贝叶斯分类器的训练数据可以每次只传入一个,也就是可以增量式学习,像SVM和决策树都需要所有训练集一起训练.
缺点是太naive,无法处理基于特征组合所产生的变化结果.
```
###决策树
就是一系列的if else,关键是如何训练/构建决策树,就是这些if else.
决策树从根部开始构建,尝试所有的拆分,找出拆分数据效果最好的那个.这个优劣性可以由几个指标描述,比如基尼不纯性,一般用的是熵,输出结果是连续数值型的时候用方差.
```
p(i) = frequency(outcome) = count(outcome) / count(total rows)

Entropy = sum of p(i) * log(p(i)) for all outcomes
```
用熵来计算信息增益,用信息增益来决定怎么拆分.
```
weight1 = size of subset1 / size of original set

weight2 = size of subset2 / size of original set

gain = entropy(original) - weight1*entropy(set1) - weight2*entropy(set2)
```
####优缺点
模型易于解释,并且能够给模型构建或者数据收集一些指导.它能够处理变量之间的相互影响,比如online pharmacy分开时不是垃圾,在一起时是垃圾邮件.
缺点不擅长对数值结果进行预测,不是增量学习的,所以不实用.
###神经网络
优点是能处理复杂的非线性函数,可以增量学习.缺点是模型是一个黑盒测试,权值不易解释,不能推导.容易过拟合.
###SVM
寻找最大间隔分割面,利用核函数将低维数据组合成高维特征.优点是准确.
缺点是核函数的参数需要cross validation来确定,需要的数据集较大,决策树适用于小数据.SVM更加黑盒.
###KNN
####加权KNN
KNN可以在线学习,可以用数值优化方法找到特征中每一项的缩放因子,给以后的数据收集做出指导.
缺点是每一次分类都要动用整个数据集.
###聚类
####分层聚类,KMEANS
###矩阵分解
####NMF,SVD,PCA
###数值优化
####模拟退火,遗传
优化参数使代价函数最小