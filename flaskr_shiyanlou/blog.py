# -*- coding:utf-8 -*-
from __future__ import with_statement
from contextlib import closing
import sqlite3
from flask import Flask,request,session,g,redirect,url_for,render_template,abort,flash

#配置文件
DATEBASE = 'F:\\PycharmProjects\\flaskr_shiyanlou\\tmp\\flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

#创建应用
app = Flask(__name__)
app.config.from_object(__name__)

#连接数据库
def connect_db():
    return sqlite3.connect(app.config[DATEBASE])
#初始化数据库-创建表
def init_db():
    with closing(connect_db()) as db:#连接数据库，并执行完下面代码之后关闭
        with app.open_resource('schema.sql',mode='rb') as f:#打开蓝本
            db.cursor().executescript(f.read)#用数据库指针执行蓝本
        db.commit()#提交
#请求数据库连接
@app.before_request#在请求开始时，我们可能需要创建数据库连接或者认证发起请求的用户
#before_request 处理程序可以从数据库中加载已登录用户，并将其保存到 g.user 中。
def before_request():
    g.db = connect_db()
#不管怎样关闭数据库
@app.teardown_request
def teardown_request():
    g.db.close()
#显示条目
app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html',entries=entries)
#添加条目
app.route('/add',methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',[request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

#登录
@app.route('/login',methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

#注销
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))






