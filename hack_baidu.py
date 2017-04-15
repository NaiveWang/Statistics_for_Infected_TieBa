import sqlite3
from urllib import request
from urllib import parse


url1 = u'http://tieba.baidu.com/%E6%B1%9F%E5%93%A5%E5%AE%8B%E5%A6%B9'
url2 = u'http://tieba.baidu.com/glgjssy'
#name.encode("gbk")

while 1:
    conn = sqlite3.connect('tieba.db3')
    c=conn.cursor()
    url0 = 'http://tieba.baidu.com/'
    name = input()
    c.execute("SELECT * FROM blocked WHERE name=\'"+name+"\'")
    if c.fetchone()!=None:
        print("数据库显示此吧已经被续")
        continue

    name = parse.quote(name)
    url0 = url0+name

    url0.encode("GB2312")
    response = request.urlopen(url0)
    #print(response.code)



    html = response.read()

    warn = '<h2 class=\"icon-attention\">抱歉，根据相关法律法规和政策，本吧暂不开放。'
    s = bytes.decode(html)
    #print(s.__len__())
    if(s.find(warn)==-1):
        print("此吧健在\n")
        if s.find('苟')!=-1:
            print("+++监测到有人在念诗")
        if s.find('吼啊')!=-1:
            print("+++监测到有人在大吼")
        if s.find('蛤')!=-1:
            print("+++监测到有人在召唤长者")
        if s.find('naive')!=-1:
            print("+++监测到有人在批判")
        if s.find('给我搞')!=-1:
            print("+++监测到有人正在赛艇")
    else:
        print("此吧已经被续\n")
        c.execute("INSERT INTO blocked VALUES(\'"+parse.unquote(name)+"\',CURRENT_TIMESTAMP)")
        conn.commit()
    conn.close()