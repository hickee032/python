from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_page(no):
    URL = f'http://kb.or.kr/p/index.php?' \
          f'j=41&ej_code=notice&st=100&sv=&pno=15&sort=0&page={no}'
    return URL

def get_data(url):
    page = urlopen(url)
    doc = page.read()
    page.close()
    soup = BeautifulSoup(doc, 'html5lib')
    table = soup.find(id='ej-tbl')
    title = table.find_all('a')
    return title

def show_title(pdata,page_no):
    BASE_URL = 'http://kb.or.kr'
    titles = []
    hrefs = []
    page_dic = {}

    for i in pdata:
        titles.append(i.get_text())
        temp = i.get('href')
        url_new = BASE_URL + temp.replace('..', '')
        hrefs.append(url_new)
        page_dic = dict(zip(titles, hrefs))

    for key in page_dic.keys():
        print(f'{key}:{page_dic[key]}')

def main():
    for i in range(1,23):
       page_data = get_data(get_page(i))
       show_title(page_data,i)

if __name__ == '__main__':
    main()