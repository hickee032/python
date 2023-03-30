import numpy as np
import pandas as pd
import folium
import json
from folium import plugins
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import webbrowser
import datetime

plt.rc("font", family="D2Coding")
plt.rcParams["axes.unicode_minus"] = False

# 지도 좌표 데이터
with open('D:\geojson\Japan_Map_Data.geojson', encoding="utf-8") as f:
    geo = json.load(f)

# 지역명과 개화시기 데이터
df = pd.read_csv("D:\geojson\Japan_Cherryblossom_Data.csv", encoding="utf-8")
tempdf = pd.DataFrame(columns=["name", "date"])

# 개화시기를 날짜 형식으로 변환한 후, 가장 개화가 빠른 곳(도쿄)의 개화시기를 기준으로 몇일 늦게 개화하는지를 각 행에 삽입
count = 0
for i, o in zip(df["개화시기"].values, df["name"].values):
    mm = str(i).split('.')[0]
    dd = str(i).split('.')[1]
    if len(dd) == 1:
        if mm == "3":
            dd = dd + str(0)
        else:
            dd = str(0) + dd
    # print(f"2023-0{mm}-{dd}")
    now = datetime.datetime.strptime(f"2023-0{mm}-{dd}", "%Y-%m-%d")
    tempdf.loc[count] = [o, now]
    count += 1
now = tempdf.loc[12, "date"]
tempdf["diff"] = tempdf["date"] - now
tempdf["diff"] = tempdf["diff"].dt.days
df["개화시기"] = tempdf["date"]
df["diff"] = tempdf["diff"]
df["개화시기"] = df["개화시기"].astype(str)
print(df)

# 기본 좌표를 도쿄로 설정하여 지도 생성
# 분홍색이 진할수록 벚꽃이 빨리 피는 지역(도쿄를 기준으로)
# 분홍색이 연해지고 초록색이 진해질수록 벚꽃이 늦게 피는 지역
center = [35.680732, 139.767270]
m = folium.Map(location=center, zoom_start=7)
choropleth = folium.Choropleth(
    geo_data=geo,
    data=df,
    columns=('id', 'diff'),
    key_on='feature.properties.id',
    fill_color='PiYG',
    legend_name='벚꽃 개화 시기',
).add_to(m)

# 마우스를 올렸을 때 지역명과 개화시기가 팝업으로 뜨게 설정
for idx, sigun_dict in enumerate(geo['features']):
    sigun_id = sigun_dict['properties']['id']
    sigun_nmm = df.loc[(df.id == sigun_id), 'name'].iloc[0]
    bloom = str(df.loc[(df.id == sigun_id), '개화시기'].iloc[0]).split("-")
    txt = f'<b><h3>{sigun_nmm}</h3></b><h4>개화시기 :{bloom[1]}월 {bloom[2]}일</h4>'
    geo['features'][idx]['properties']['tooltip1'] = txt
choropleth.geojson.add_child(folium.features.GeoJsonTooltip(['tooltip1'], labels=False))
title_html = '<h3 align="center" style="font-size:30px"><b>2023년 일본 벚꽃 개화 시기</b></h3>'
m.get_root().html.add_child(folium.Element(title_html))

# 지도를 파일로 저장하고 열기
m.save("D:\\Japan_Cherryblossom_Map.html")
webbrowser.open_new_tab("D:\\Japan_Cherryblossom_Map.html")
