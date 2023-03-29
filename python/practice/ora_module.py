import cx_Oracle as db

con = None
def connectDB():
    global con
    try:
        con = db.connect('test/1234@127.0.0.1/XE')
        print('ORA 버전:', con.version)
    except db.DatabaseError as e:
        err_msg(e)

def closeDB():
    try:
        con.close()
        print('오라클 DB 해제!')
    except db.DatabaseError as e:
        err_msg(e)

def err_msg(e):
    err_obj, = e.args
    print('------------------------')
    print('에러 코드:', err_obj.code)
    print('에러 메시지:', err_obj.message)
    print('------------------------')