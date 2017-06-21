import sqlite3
from urllib import request
from urllib import parse
import traceback
#name.encode("gbk")
warn = '<h2 class=\"icon-attention\">抱歉'
conn = sqlite3.connect('tieba.db3')
c=conn.cursor()

for row in c.execute("SELECT *FROM normal"):
    url0 = 'http://tieba.baidu.com/'+parse.quote(row[0])
    name = row[0]
    url0.encode("GB2312")
    response = request.urlopen(url0)
    html = response.read()
    s = bytes.decode(html)
    s=s.split("class=\"content\"")
    del(s[0])
    s=s[0]
    if(s.find(warn)==-1):
        print(name+"吧健在。")
        ct = 0
        if s.find('关于撤销')!=-1:
            if s.find('吧主权限')!=-1:
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

        if(ct>0):
            print(name+"吧被感染")
            c.execute("INSERT INTO infected VALUES(\'" + name + "\',"+ct.__str__()+",CURRENT_TIMESTAMP)")
            conn.commit()
            c.execute("DELETE FROM normal WHERE name=\'" + name + "\'")
            conn.commit()
        else:
            print(name+"吧还是这么个熊样")
    else:
        print("O---此吧已经被续\n")
        c.execute("INSERT INTO blocked VALUES(\'"+name+"\',CURRENT_TIMESTAMP)")
        conn.commit()
        c.execute("DELETE FROM normal WHERE name=\'"+name+"\'")
        conn.commit()
    print("")
conn.close()