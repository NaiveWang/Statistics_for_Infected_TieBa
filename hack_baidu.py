
from urllib import request
from urllib import parse


url1 = u'http://tieba.baidu.com/%E6%B1%9F%E5%93%A5%E5%AE%8B%E5%A6%B9'
url2 = u'http://tieba.baidu.com/glgjssy'
#name.encode("gbk")

while 1:
    url0 = 'http://tieba.baidu.com/'
    name = input()
    name = parse.quote(name)
    url0 = url0+name

    url0.encode("GB2312")
    response = request.urlopen(url0)
    #print(response.code)



    html = response.read()

    warn = '抱歉，根据相关法律法规和政策，本吧暂不开放。'
    s = bytes.decode(html)
    #print(s.__len__())
    if(s.find(warn)==-1):
        print("此吧健在")
        if s.find('苟')!=-1:
            print("+++监测到有人在念诗")
        if s.find('吼啊')!=-1:
            print("+++监测到有人在大吼")
    else:
        print("此吧已经被续")