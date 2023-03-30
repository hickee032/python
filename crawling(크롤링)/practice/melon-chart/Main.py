import db_module as db
import Menu as menu

if __name__ == '__main__':
    db.connect_db()
    while True:
        m = menu.main_menu()
        if m == '1':
            print('테이블 생성')
            db.create_tbl()
        elif m == '2':
            print('테이블 삭제')
            db.drop_tbl()
        elif m == '3':
            print('데이터 추가')
            # for i in range(2, 100):
            #     ora.insert_tbl(i + 1, '전우치', 100, '강원')
            # ora.insert_tbl2()
            db.insert_tbl3()
        elif m == '4':
            print('데이터 출력')
            db.select_db2()
        elif m == '5':
            print('데이터 삭제')
            db.delete_db(1111)
        elif m == '6':
            print('종료')
            db.close_db()
            exit()
