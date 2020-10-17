
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


path = r"C:\Users\Administrator\PycharmProjects\crawling\chromedriver_win32\chromedriver.exe"                               # 내 컴퓨터의 크롬 드라이버 경로
driver = webdriver.Chrome(path)                                                                                             # 크롬 드라이버 실행.
driver.get("https://programmers.co.kr/learn/challenges")                                                                    # programmers 실행
driver.find_element_by_css_selector(r"body > div.main > div.challenges__tabs--wrap > ul > li:nth-child(3) > a").click()     # 모든 문제버튼 클릭
time.sleep(1)                                                                                                               # 1초 쉼


driver.find_element_by_xpath(r'//*[@id="collapseFilterLanguage"]/li[9]/label').click()                                      # python3 문제 클릭.
time.sleep(1)                                                                                                               #휴식..
href_inform = driver.find_elements_by_css_selector(r"#tab_all_challenges > section > div > div.challenge__algorithms--index.col-md-8 > div.algorithm-list > div.row > div > div > a")
next_page_inform = driver.find_elements_by_css_selector(r"#tab_all_challenges > section > div > div.challenge__algorithms--index.col-md-8 > div.algorithm-list > div.d-flex.justify-content-center > nav > ul > li")
i = 1
for next_pg in next_page_inform:
    for href in href_inform :
        link = href.get_attribute('href')
        move = requests.get(link)
        html_move = BeautifulSoup(move.text,"html.parser")
        desc = html_move.select("#tour2 > div")
        file_path = r"C:\Users\Administrator\Documents\programmers\%d.md"%i
        with open(file_path,'wt',-1,'utf-8') as f:
            print("%d번째 파일 작성중..."%i)
            f.write(str(desc))
        print("%d번째 파일 작성 완료!"%i)
        i += 1
        time.sleep(1)
    print("다음 페이지로 이동중...")
    next_page_inform[i].click()
    time.sleep((2))














# 썼던 코드 모음

# for data in move_data :
#     time.sleep(1)
#     driver.get("https://programmers.co.kr/learn/challenges")
#     html = BeautifulSoup(move_data[0], "html.parser")
#     href = html.select_one(html.body.div.div.section.div.div.div.div.div.div.div.div)
#     print(href.text)
# time.sleep(1)
# data.find_element_by_xpath("")
# time.sleep(1)


# //*[@id="tab_all_challenges"]/section/div/div[2]/div[2]/div[1]/div[1]/div/a
# //*[@id="tab_all_challenges"]/section/div/div[2]/div[2]/div[1]/div[2]/div/a
# #tab_all_challenges > section > div > div.challenge__algorithms--index.col-md-8 > div.algorithm-list > div.row > div > div > a
# #tab_all_challenges > section > div > div.challenge__algorithms--index.col-md-8 > div.algorithm-list > div.row > div:nth-child(2) > div > a

# search_box.submit()
# res = requests.get("https://comic.naver.com/webtoon/detail.nhn?titleId=662774&no=208&weekday=wed")
#
# html = BeautifulSoup(res.text, "html.parser")
#
# path = "C:/Users/Administrator/Downloads/img_files"
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
#                           Chrome/76.0.3809.146 Whale/2.6.89.9 Safari/537.36',
#            'Referer': "https://comic.naver.com/webtoon/detail.nhn?titleId=662774&no=208&weekday=wed"}
#
# for img in html.select("#comic_view_area > div.wt_viewer img"):
#     img_res = (requests.get(img['src'], headers=headers))
#     img_name = (img['src'].split('_')[-1])
#     with open(path  + '/' + img_name,"wb") as f:
#         f.write(img_res.content)


# Python Summary 레포 1-2 자료형 복습, 1-3 도, 1-5도, 1-6도, 1-8도 , 2-1의 정규표현식
