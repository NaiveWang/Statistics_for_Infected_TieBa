# 一个关键词语法解释器
用来更便捷地进行关键词匹配。

值得注意的是，在此项目中效率不在优化范围内。
## 具体功能
### 1.兼容更多“火星文”
中国的网络特色嘛，大家都懂的蛤蛤，比如“吼啊”，假设“吼啊”是屏蔽字，那么网友如何解决此问题呢？
稍有常识的人都能看出，就百度那SB过滤器，你打成“吼蛙”，“口孔口阿”之类的就能暗中膜蛤。
那么很显然，我们得增加两个关键字。那么现在的问题是，如果又有“吼口阿”、“口孔蛙”之类的词条出现，根本没必要
再增加词条，因为前者已经部分包含了。

只需将词条分段，每一段分成一组，再在组组之间进行全排列就可。

再考虑另一种情况：“给我搞的这个吧啊”、“给我搞得这个吧啊”和“搞的这个”三个匹配字

按照分组：“给我”和空串，“搞”，“得”和“的”，“这个”，“吧啊”和空串
它们的全排列远不仅资瓷以上三种关键字。
#### pitfalls
正是此函数能产生笛卡儿积的缘故，没法去掉全排列内不想要的情况，比如上述里面，我不想用“搞得这个”关键字，就无力从心。

此缺陷尚待解决。

但实际使用中此缺陷可以忽略。
### 2.进阶匹配
考虑以下问题：有这种情况，你进入某个吧的时候，楼主会发一贴，标题“苟”，或者包含“苟”的句子。
那么如何判断哪个帖子更有膜性呢？显然上述情况，若是楼主讲“今天去苟不理，服务员态度太差，也比庆丰的强”，虽然也可能有膜的嫌疑，但肯定
没有直接发“苟”的大。而在字符串匹配里，发去吃苟不理发牢骚，跟直接念诗得到的是同一个结果：发现了“苟”。

难道人工智能就一蹴而就了么？？一派胡言！

试想一下，若是此贴有人膜，按照常识，二楼会出现“利”的字样，这是关键。
于是乎程序这样运行：找到了“苟”，进一步又找到了“利”，跟之前等价匹配不一样，这个匹配是嵌套的，
第一个功能匹配完“吼蛙”以后还能匹配“口孔口阿”，但在这里，在匹配到“苟”之前是不会匹配“利”的。