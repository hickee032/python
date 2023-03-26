from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ChunkedEncodingError


# URL 정보
def get_page(no):
    url = f'http://kb.or.kr/p/index.php?j=41&ej_code=notice&st=100&sv=&pno=15&sort=0&page={no}'
    return url


# URL 정보로 data 가져오기
def get_data(url):
    try:
        req = requests.get(url, stream=True)
        html = req.content
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find(id='ej-tbl')
        title = table.find_all('a')
        return title

    except ChunkedEncodingError:
        print('에러 발생')


# def show_title(pdata, page_no):
#     BASE_URL = 'http://kb.or.kr/'
#     title = []
#     hrefs = []
#     page_dic = []
#     for i in pdata:


def main():
    for i in range(1, 24):
        page_data = get_data(get_page(i))
        for n in page_data:
            print(n.get_text())


if __name__ == '__main__':
    main()
