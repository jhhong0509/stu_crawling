import requests
from bs4 import BeautifulSoup

res = requests.get("https://comic.naver.com/webtoon/list.nhn?titleId=662774&weekday=wed")

# print(res)
# print(type(res))
# print(dir(res))
# print(*dir(res), sep='\n')
# print(res.status_code)
html = BeautifulSoup(res.text, "html.parser")
html2 = html.select_one("#content > div.comicinfo > div.detail > h2")
print(html2.text);
# for i in html.select("#content > ul li a"): #요소 담기
#     print(i['href']) #요소 내의 속성 값
#     print(i.text) #요소 내의 글
# dir() : 객체의 필드 알 수 있고, 리스트 출력
# type() : 객체 타입 출력
# find(태그)한개
# find_all(태그) 전부
# select() 전부
# select_one() 맨 처음 한개