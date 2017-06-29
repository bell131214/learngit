#-*- coding:utf-8 -*-
import sqlite3
#连接到数据库，如果文件不存在则创建
conn = sqlite3.connect('testsql.db')
#创建一个游标cursor
cursor = conn.cursor()
#执行一条语句，创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#继续执行一条语句，插入一条记录
cursor.execute('insert into user(id,name) values (\'1\',\'zhang\')')
#通过rowcount获得插入的行数
cursor.rowcount
#关闭游标
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()














