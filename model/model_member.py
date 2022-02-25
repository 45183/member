import sqlite3
from flask import request

# db 접속 함수
def getconn():
    conn = sqlite3.connect("./members.db")
    return conn

def select_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member ORDER BY regDate DESC"
    cur.execute(sql)
    rs = cur.fetchall()                     # 회원 전체의 데이터
    conn.close()
    return rs

def select_one(id):
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member WHERE mid = '%s'" % (id)
    cur.execute(sql)
    rs = cur.fetchone()  # 회원 1명의 데이터
    conn.close()
    return rs

def join_member():
    # 데이터 가져오기
    id = request.form['mid']
    pwd = request.form['passwd']
    name = request.form['name']
    age = request.form['age']

    # db 저장(회원 가입)
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO member(mid, passwd, name, age)" \
          " VALUES('%s', '%s', '%s', '%s')" % (id, pwd, name, age)
    cur.execute(sql)
    conn.commit()

    # 자동 로그인(가입 후 로그인 상태)
    sql = "SELECT * FROM member WHERE mid = '%s' AND passwd = '%s'" % (id, pwd)
    cur.execute(sql)
    rs = cur.fetchone()
    conn.close()
    return rs

def login_member():
    # 입력된 아이디와 비밀번호를 가져오기
    id = request.form['mid']
    pwd = request.form['passwd']

    # db 연동
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member WHERE mid = '%s' AND passwd = '%s'" % (id, pwd)
    cur.execute(sql)
    rs = cur.fetchone()
    conn.close()
    return rs

def delete_member(id):
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM member WHERE mid = '%s'" % (id)
    cur.execute(sql)
    conn.commit()
    conn.close()

def update_member(id):
    # 데이터 수집
    mid = request.form['mid']
    pwd = request.form['passwd']
    name = request.form['name']
    age = request.form['age']

    # db 연동
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE member SET passwd='%s', name='%s', age='%s' " \
          "WHERE mid = '%s'" % (pwd, name, age, mid)
    cur.execute(sql)
    conn.commit()
    conn.close()