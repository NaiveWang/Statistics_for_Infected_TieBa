import sqlite3
#encoding=<"gbk">
conn = sqlite3.connect('tieba.db3')
c=conn.cursor()
o=open('blocked.txt','w')
for row in c.execute('SELECT * FROM blocked'):
    o.writelines(row[0]+'\n')
