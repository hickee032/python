import datetime
import json
import urllib.parse
import urllib.request

file_name = None


def get_request_url(url):
    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id', 'bwvcfH0XTJPsuWGdKnjW')
    req.add_header('X-Naver-Client-Secret', 'b5BbKw3Owy')
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print(f'[{datetime.datetime.now()}]서버요청성공:{url}')
            return response.read().decode('utf-8')
    except Exception:
        print(f'[{datetime.datetime.now()}]서버요청에러:{url}')
        return None


def getNaverSearchResult(sNode, search_text, page_start=1, display=10):
    baseURL = 'https://openapi.naver.com/v1/search/'
    node = f'{sNode}.json'
    param = f'?query={urllib.parse.quote(search_text)}'
    param += f'&start={page_start}'
    param += f'&display={display}'
    URL = baseURL + node + param
    # print(URL)
    ret_data = get_request_url(URL)
    return json.loads(ret_data)


def getPostData(post):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']
    # Wen, 25 Jan 2023 12:00:02 +0900
    pdate = datetime.datetime.strptime(post['pubDate'],
                                       '%a, %d %b %Y %H:%M:%S +0900')
    # 2023-1-25 12:01:30
    pdate = pdate.strftime('%Y-%m-%d %H:%M:%S')
    print('제목:', title)
    print('요약:', description)
    print('원본 링크:', org_link)
    print('링크:', link)
    print('업로드날짜:', pdate)


def main():
    global file_name
    sNode = 'news'
    search_text = '마스크'
    display_count = 10  # 100 최대
    start_page = 1  # 1000
    json_search = \
        getNaverSearchResult(sNode, search_text, start_page, display_count)
    num = 1
    # for post in json_search['items']:
    #     print('번호:', num)
    #     getPostData(post)
    #     print('-------------------------------------------')
    #     num += 1

    file_name = f'{search_text}_naver_{sNode}.json'
    try:
        with open(file_name, 'w', encoding='utf-8') as outfile:
            ret = json.dumps(json_search, indent=4,
                             sort_keys=False, ensure_ascii=False)
            outfile.write(ret)
            print(f'{file_name} 저장 성공!')
    except BaseException as ex:
        print('파일 저장 에러:', ex)


def load_jsonFile():
    with open(file_name, 'r', encoding='utf-8') as rf:
        json_dic = json.load(rf)
        num = 1
        for post in json_dic['items']:
            print('번호:', num)
            getPostData(post)
            print('-------------------------------------------')
            num += 1


if __name__ == '__main__':
    main()
    load_jsonFile()
