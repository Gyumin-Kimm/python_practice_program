from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%ED%97%A4%EC%9D%B4%EC%A6%88") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

# thumnails = soup.select_one('#imgList > div:nth-child(1) > a > img')['src']
thumnails = soup.select('#imgList > div > a > img')

i = 1
for thumbnail in thumnails:
    img = thumbnail['src']
    dload.save(img,f'imgs_homework/{i}.jpg')
    i += 1

driver.quit() # 끝나면 닫아주기