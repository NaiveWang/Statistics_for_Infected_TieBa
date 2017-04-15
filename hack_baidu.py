
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






    html = response.read()
    #print(html)
    warn = '抱歉，根据相'
    s = bytes.decode(html)
    if(s.find(warn)==-1):
        print("此吧健在")
    else:
        print("此吧已经被续")