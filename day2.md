查准率与查全率一般情况有反向变动关系，查准率越高，相应的查全率就会降低；反过来也一样
那么问题来了，如何定义最优？
1.平衡点  p=r的点
2.F1
3.Fbeta


F1 为何选用调和平均数？各种解释似乎都在告诉我，没有更好的选择。。。
就是当a和b很接近的时候，调和平均数和算术平均数很接近，但是两者偏离的话，就远小于算术平均数了。
调和平均数受极端值影响较小，更适合评价不平衡数据的分类问题

Fbeta,通过beta的值控制查全率和查准率对 F 值的影响度

模型评估：
P-R 曲线：
曲线交叉时：1.算面积，2.F1，3.Fbeta
大部分肉眼可以判断好坏 😁

代价曲线😵😵😵
ROC 曲线😵😵😵
AUC😵😵😵
😵😵😵😵
什么玩意儿？

假设检验，二项分布，T分布 。我学的概率论终于用上了


今天主要学习西瓜书第二章，很多地方看了不下十遍也不能理解，有些地方理解之后给我的感觉就是，用例子很容易说清楚，但很难沉淀出具体定义，然而前人真的总结出了公式，公式吓死人，导致学习者恶性循环