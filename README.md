# 被续贴吧统计器
Note: This project is just for kicking ass in China mainland.

用来统计、识别被续的贴吧
## 简单描述
### 1.能够识别哪个贴吧被续，哪个没被续
此功能来自于网页分析，值得注意的是，若是百度更改网页排版，此功能将报废
### 2.本地记录
将贴吧按照被续、被膜、没人膜三类进行记录
### 3.是否被膜判定(非精确)
通过检索页面关键字来确定此吧是否有人在膜
#### 注：此功能将在下一阶段推广为独立模块
### 4.已有贴吧刷新
刷新器用来刷新数据库已有的贴吧，并重新分类
## 用法
### 1.需要有Python3.X资瓷
### 2.将三个Python脚本、一个db3数据库文件下载到本地，并在有网络的环境里即可运行
#### hack_baidu:直接输入贴吧名即可
#### refresh_normal:刷新已经记录在案的健康贴吧
#### refresh_infected:刷新已经记录在案的被膜贴吧
### 3.其中db3文件可以直接用sqlitespy直接打开，另，统计信息脚本以后再码
## 要是出错了看这里
### 1.看看你是不是落了什么东西了
### 2.可以给我commit，讲清楚情况，平台即可。目前在win上可以谈笑风生
