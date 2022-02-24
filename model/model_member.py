import sqlite3

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