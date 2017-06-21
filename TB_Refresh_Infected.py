import sqlite3
import socket
from urllib import request
from urllib import parse
#from goto import *
import traceback
#name.encode("gbk")
socket.setdefaulttimeout(15)
warn = '<h2 class=\"icon-attention\">抱歉'
conn = sqlite3.connect('tieba.db3')
c=conn.cursor()
counter=0
counter1=0
for row in c.execute("SELECT *FROM normal"):
    counter1+=1
    url0 = 'http://tieba.baidu.com/'+parse.quote(row[0])
    name = row[0]
    url0.encode("GB2312")
    while(1):
        try:
            response = request.urlopen(url0)
        except Exception:
            print("超时，正尝试重新抓取。")
        else:
            break
    try:
        html = response.read()
        s = bytes.decode(html)
    except Exception:
        print("网站解析失败，跳过，吧名为："+name)
    else:
        if(s.find(warn)==-1):
            print(name+"吧健在。")
            s = s.split("class=\"content\"")
            del s[0]
            s = s[0]
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

            if(ct==0):
                print(name+"吧依旧正常")
                #c.execute("DELETE FROM infected WHERE name=\'"+name+"\'")
                #conn.commit()
                #c.execute("INSERT INTO normal VALUES(\'"+name+"\',CURRENT_TIMESTAMP)")
                #conn.commit()
            else:
                print(name+"吧感染度有变更")
                #c.execute("UPDATE infected SET matched="+level.__str__()+" WHERE name='"+name+"\'")
                #conn.commit()

        else:
            print(name+"吧已经被续\n")
            counter+=1
for row in c.execute("SELECT *FROM infected"):
    counter1+=1
    level = row[1]
    url0 = 'http://tieba.baidu.com/'+parse.quote(row[0])
    name = row[0]
    url0.encode("GB2312")
    response = request.urlopen(url0)
    html = response.read()
    try:
        s = bytes.decode(html)
    except Exception:
        print("网站解析失败，跳过，吧名："+name)
    else:
        if(s.find(warn)==-1):
            print(name+"吧健在。")
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

            if(ct==0):
                print(name+"吧可能被清场")
                #c.execute("DELETE FROM infected WHERE name=\'"+name+"\'")
                #conn.commit()
                #c.execute("INSERT INTO normal VALUES(\'"+name+"\',CURRENT_TIMESTAMP)")
                #conn.commit()
            elif(ct!=level):
                print(name+"吧感染度有变更")
                #c.execute("UPDATE infected SET matched="+level.__str__()+" WHERE name='"+name+"\'")
                #conn.commit()
            else:
                print(name+"吧还是这么个熊样")
        else:
            print(name+"吧已经被续\n")
            counter+=1
            #c.execute("INSERT INTO blocked VALUES(\'"+name+"\',CURRENT_TIMESTAMP)")
            #conn.commit()
            #c.execute("DELETE FROM infected WHERE name=\'"+name+"\'")
            #conn.commit()
print("")
print("本次一共检查了"+counter1.__str__()+"个有人在膜的吧")
print("其中有"+counter.__str__()+"个吧被续。")
conn.close()