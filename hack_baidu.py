import sqlite3
import socket
from urllib import request
from urllib import parse
import traceback
#name.encode("gbk")
socket.setdefaulttimeout(15)
while 1:
    conn = sqlite3.connect('tieba.db3')
    c=conn.cursor()
    url0 = 'http://tieba.baidu.com/'
    name = input()
    c.execute("SELECT * FROM blocked WHERE name=\'"+name+"\'")
    if c.fetchone()!=None:
        print("#---数据库显示此吧已经被续")
        continue
    c.execute("SELECT *FROM infected WHERE name=\'"+name+"\'")
    if c.fetchone()!=None:
        for row in c.execute("SELECT *FROM infected WHERE name=\'"+name+"\'"):
            print("#---数据库显示此吧已列入感染名单，匹配度为："+row[1].__str__())
        continue
    c.execute("SELECT * FROM normal WHERE name=\'" + name + "\'")
    if c.fetchone() != None:
        print("#---数据库显示此吧在上次发现时正常")
        continue
    name = parse.quote(name)
    url0 = url0+name

    url0.encode("GB2312")
    response = request.urlopen(url0)
    #print(response.code)


    print("O--数据库空，正在抓取此吧")

    try:
        html = response.read()
    except Exception as e:
        print("访问超时")
        continue
    #print(len(html))

    warn = 'h2 class=\"icon-attention\">抱歉'
    try:
        s = bytes.decode(html)
    except Exception as e:
        print("X---暂无此吧")
        continue

    #print(s.__len__())
    if(s.find(warn)==-1):
        s=s.split("class=\"content\"")
        del s[0]
        s=s[0]
        print("O---此吧健在。")
        ct = 0
        if s.find('关于撤销')!=-1:
            if s.find('吧主管理权限')!=-1:
                print("++++++监测到此吧吧主被撤销")
                ct+=1
        if s.find('苟')!=-1:
            print("++++监测到有人在念诗")
            ct+=5
            if s.find('利')!=-1:
                ct+=45
        if s.find('吼啊')!=-1:
            print("++++监测到有人在大吼")
            ct+=50
        if s.find('蛤')!=-1:
            print("++++监测到有人在召唤长者")
            ct+=10
        if s.find('naive')!=-1:
            print("++++监测到有人在得罪一下")
            ct+=30
        if s.find('给我搞')!=-1:
            print("++++监测到有人正在赛艇")
            ct+=50
        print("O----此吧被感染程度（估）："+ct.__str__())
        print("")
        if(ct>0):
            c.execute("INSERT INTO infected VALUES(\'"+parse.unquote(name)+"\',"+ct.__str__()+",CURRENT_TIMESTAMP)")
            conn.commit()
        else:
            c.execute("INSERT INTO normal VALUES(\'" + parse.unquote(name) + "\',CURRENT_TIMESTAMP)")
            conn.commit()
    else:
        print("O---此吧已经被续\n")
        c.execute("INSERT INTO blocked VALUES(\'"+parse.unquote(name)+"\',CURRENT_TIMESTAMP)")
        conn.commit()
    conn.close()
