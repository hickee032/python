# Oracle
import cx_Oracle as db
import pandas as pd

# db 전역변수
con = None
cursor = None


# db 연결
def connect_db():
    global con
    global cursor
    try:
        con = db.connect('test/1234@127.0.0.1/XE')
        print('ORA 버전:', con.version)
        cursor = con.cursor()
    except db.DatabaseError as e:
        err_msg(e)


# db 연결 해제
def close_db():
    try:
        con.close()
        print('오라클 DB 해제!')
    except db.DatabaseError as e:
        err_msg(e)


def err_msg(e):
    err_obj, = e.args
    print('에러코드', err_obj.code)
    print('에러 메세지', err_obj.message)


# 테이블 생성
def create_tbl():
    try:
        sql = """
                create table melon_Chart(
                ranking number,
                sing_name varchar2(200),
                title  varchar2(200),
                album_name varchar2(200)
                )
            """
        cursor.execute(sql)
        con.commit()
        print('테이블 생성 성공')
    except db.DatabaseError as e:
        err_msg(e)


# 테이블 삭제
def drop_tbl():
    try:
        sql = 'drop table melon_Chart'

        cursor.execute(sql)
        con.commit()
        print('테이블 삭제 성공')
    except db.DatabaseError as e:
        err_msg(e)


# 테이블 데이터 추가
def insert_tbl2():
    data = [1000, '김유신', 100, '조선 한양 홍대감네']
    try:
        # binding 바인딩 -> 값
        sql = f"insert into melon_Chart values(:1,:2,:3,:4)"
        cursor.execute(sql, data)
        con.commit()
    except db.DatabaseError as e:
        err_msg(e)
