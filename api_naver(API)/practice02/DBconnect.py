import cx_Oracle as Db

# 전역변수 사용
con = None
cursor = None


# db 연결
def connect_db():
    global con
    global cursor
    try:
        con = Db.connect('test/1234@127.0.0.1/XE')
        print('ORA 버전:', con.version)
        cursor = con.cursor()
    except Db.DatabaseError as e:
        err_msg(e)


# db 연결 해제
def close_db():
    try:
        con.close()
        print('오라클 DB 해제!')
    except Db.DatabaseError as e:
        err_msg(e)


# 에러
def err_msg(e):
    err_obj, = e.args
    print('에러코드', err_obj.code)
    print('에러 메세지', err_obj.message)


# 테이블 생성
def create_tbl():
    try:
        sql = """
                create table book_serch_t(
                title varchar2(1000),
                link varchar2(1000),
                author varchar2(1000),
                publisher varchar2(1000),
                description varchar2(1000)
                )
            """
        cursor.execute(sql)
        con.commit()
        print('테이블 생성 성공')
    except Db.DatabaseError as e:
        err_msg(e)


def insert_tbl(title, link, author, publisher, description):
    try:
        sql = f"insert into book_serch_t values('{title}', '{link}', '{author}', '{publisher}', '{description}')"
        cursor.execute(sql)
        con.commit()
    except Db.DatabaseError as e:
        err_msg(e)
