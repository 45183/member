# DB 관리

import sqlite3

def getconn():
    conn = sqlite3.connect("./members.db")      # 현재 위치에 데이터베이스 생성
    return conn

def creat_table():
    # 테이블 생성
    conn = getconn()
    cur = conn.cursor()
    sql = """
        CREATE TABLE member(
            mid char(5) PRIMARY KEY,
            passwd  char(8) NOT NULL,
            name    text NOT NULL,
            age integer,
            regDate timestamp date DEFAULT (datetime('now', 'localtime'))
        )
    """
    cur.execute(sql)
    conn.commit()
    print("테이블 생성")
    conn.close()

def insert_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO member(mid, passwd, name, age) VALUES(?, ?, ?, ?)"
    cur.execute(sql, ('10001', 'm1234567', '최민정', 24))
    cur.execute(sql, ('10002', 'm1234568', '안산', 21))
    conn.commit()
    conn.close()

def select_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member ORDER BY regDate DESC"
    cur.execute(sql)
    rs = cur.fetchall()
    # print(rs)
    for i in rs:
        print(i)
    conn.close()

# conn = getconn()
# print('접속', getconn())
# creat_table()
# insert_member()
select_member()