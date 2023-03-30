# service key 설정
import urllib.request
from urllib.parse import quote

service_key = 'NMEoUhvnwRKfms6GyYCguKH9EylZibVsxnK91C%2B1iwyLQNnN%2Bj41aKFDl%2F2%2BGFMIHtlNQf6N4eVMIuLXmrFKBg%3D%3D'
# service url 설정
service_url = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'


# url 세팅
def url_setting_page_non(ym, sido, items=50, page_no=1, servicekey=service_key, serviceurl=service_url):
    parameter = f'?_type=json&serviceKey={servicekey}'
    parameter += f'&YM={ym}&SIDO={quote(sido)}'
    parameter += f'&numOfRows={items}'
    parameter += f'&pageNo={page_no}'
    url = serviceurl + parameter
    return url


# 데이터 가져오기
def get_tour_data(templist, url):
    request = urllib.request.Request(url)
    res = urllib.request.urlopen(request)
    try:
        if res.getcode() == 200:
            data = res.read().decode('utf-8')
            templist.append(data)
    except Exception as ex:
        print('http 에러 코드', ex)


