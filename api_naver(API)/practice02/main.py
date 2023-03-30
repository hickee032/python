import naverSearchEx01 as Ns
import menu
import DBconnect as Db

if __name__ == '__main__':

    input_book = "파이썬"
    result_data = None
    dic = None
    rlist = None
    while True:
        Db.connect_db()
        m = menu.main_menu()
        if m == '1':
            input_book = input('검색 할 책 제목을 입력하세요 : ')
            s_url = Ns.search_book(input_book)
            result_data = Ns.sever_request(s_url)
            print(Ns.sever_request(s_url))
        elif m == '2':
            print('json 파일로 저장')
            Ns.json_searchfile(input_book, result_data)
        elif m == '3':
            print('json 파일 불러오기')
            dic, rlist = Ns.json_readfile(input_book)
            print(dic)
            print(rlist)
        elif m == '4':
            print('엑셀 파일로 저장')
            Ns.xml_writer(dic)
        elif m == '5':
            print('csv 파일 저장')
            Ns.csv_writer(dic)
        elif m == '6':
            print('DB 테이블 생성')
            Db.create_tbl()
        elif m == '7':
            print('DB 데이터 추가')
            num =0
            for i in rlist:
                print(num)
                Db.insert_tbl(i["title"], i["link"], i["author"], i["publisher"], i["description"])
                num+=1
        elif m == '0':
            print('종료')
            exit()
