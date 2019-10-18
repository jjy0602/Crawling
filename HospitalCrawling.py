from selenium import webdriver

from bs4 import BeautifulSoup

#ChromeDriver로 접속
driver = webdriver.Chrome(r'C:\Users\multicampus\Desktop\new_crawling\chromedriver.exe')

driver.implicitly_wait(3)

#웹페이지 불러오기

driver.get('https://map.naver.com/')

#검색창에 서울 맛 친 후 검색버튼 클릭

search = driver.find_element_by_id('search-input')

search.send_keys('서울 맛집')

driver.find_element_by_xpath("""//*[@id="header"]/div[1]/fieldset/button""").click()

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

#1페이지 식당이름 크롤링

rname = soup.select('#panel > div.panel_content.nano.has-scrollbar > div.scroll_pane.content > div.panel_content_flexible > div.search_result > ul > li > div.lsnx > dl > dt > a')

category = soup.select('#panel > div.panel_content.nano.has-scrollbar > div.scroll_pane.content > div.panel_content_flexible > div.search_result > ul > li > div.lsnx > dl > dd.cate') #scategoty = soup.select('#panel > div.panel_content.nano.has-scrollbar > div.scroll_pane.content > div.panel_content_flexible > div.search_result > ul > li > div.lsnx > dl > dd.cate')

#출력

for n in rname:

   print(n.text.strip())

#2번페이지 이동

driver.find_element_by_xpath("""//*[@id="panel"]/div[2]/div[1]/div[2]/div[2]/div/div/a[1]""").click()

rname = soup.select('#panel > div.panel_content.nano.has-scrollbar > div.scroll_pane.content > div.panel_content_flexible > div.search_result > ul > li > div.lsnx > dl > dt > a')

for n in rname:

   print(n.text.strip())


