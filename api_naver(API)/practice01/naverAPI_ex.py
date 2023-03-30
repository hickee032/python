# naver api 사용
import datetime
import json
import urllib.parse
import urllib.request
file_name = None

# 예외 처리
def get_requset_url(url):
    req = urllib.request.Request(url)
    # 네이버 -> developer -> 애플리케이션 정보
    req.add_header('X-Naver-Client-Id', 'SrNxTWJA3SuZSEKUsT6J')
    req.add_header('X-Naver-Client-Secret', 'KJl3pu_9oO')
    try:
        response = urllib.request.urlopen(req)
        # 200이 서버응답 성공 값 (http protocol)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception:
        print(f'[{datetime.datetime.now()}] 서버요청 에러 : {url}')
        return None


# 디폴트 매개변수 사용시 주의점
# def getNaverSearchResult(sNode, search_text, page_start = 1, display):
# 중간에 따로 쓰면 오류가 발생함 둘다 쓰거나 마지막에만 사용함

# URL을 만듬
def getNaverSearchResult(sNode, search_text, page_start=1, page_end=5, display=100):
    ret_data = None
    for i in range(page_start, page_end):
        baseUrl = 'https://openapi.naver.com/v1/search/'
        node = f'{sNode}.json'
        param = f'?query={urllib.parse.quote(search_text)}'
        param += f'&start={page_start}'
        param += f'&display={display}'
        URL = baseUrl + node + param
        # print(URL)
        ret_data = get_requset_url(URL)
        # print(ret_data)
    return json.loads(ret_data)


# 파싱과정
def getPostData(post):
    print(type(post))

    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']
    # 25 Jar 2023 12:00:02 +0900
    pdate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    # 2023-1-25 12:00:00
    pdate = pdate.strftime('%Y-%m-%d %H:%M:%S')
    print(f'제목 : {title.replace("&quot;", "").replace("&apos;","")}')
    des = description.replace("<b>", "").replace("</b>", "").replace("&apos;", "").replace("&quot;", "")
    print(f'요약 : {des}')
    print(f'제목 : {title}')
    print(f'원본링크 : {org_link}')
    print(f'링크 : {link}')
    print(f'업로드 날짜 : {pdate}')


def main():
    # 값을 넣을 경우 global 필요
    global file_name
    sNode = 'news'  # 카테고리
    search_text = '우크라이나'  # 검색어
    start_page = int(input('시작 페이지를 입력하세요 : '))
    end_page = int(input('마지막 페이지를 입력하세요 : '))
    display_count = 100
    json_search = getNaverSearchResult(sNode, search_text, start_page, end_page, display_count)
    num = 1
    for post in json_search['items']:
        print('번호', num)
        getPostData(post)
        num += 1
    file_name = f'{search_text}_naver_{sNode}.json'
    try:
        with open(file_name, 'w', encoding='utf-8') as outfile:
            ret = json.dumps(json_search, indent=4, sort_keys=False, ensure_ascii=False)
            outfile.write(ret)
            print(f'{file_name}_json파일이 저장됨')

    except BaseException as ex:
        print('파일 저장 에러', ex)

    load_jsonfile1(file_name)


# def load_jsonfile():
#     # with open() 을 사용하면 close를 안해도 된다
#     with open(file_name, 'r', encoding='utf-8') as readfile:
#         json_dic = json.load(readfile)
#         print(json_dic)


def load_jsonfile1(file_name):
    # with open() 을 사용하면 close를 안해도 된다
    with open(file_name, 'r', encoding='utf-8') as readfile:
        json_dic = json.load(readfile)
        print(json_dic)

        num = 1
        for post in json_dic['items']:
            print('읽어오는 번호', num)
            getPostData(post)
            num += 1


if __name__ == '__main__':
    main()
