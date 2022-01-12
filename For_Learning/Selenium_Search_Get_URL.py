# 導入selenium的webdriver
from selenium import webdriver
from time import sleep

# 開啟瀏覽器
web = webdriver.Chrome()
# 網頁最大化
web.maximize_window()
# 前往指定的網址
web.get("https://www.google.com")

try:
    # 利用xpath找到輸入框，並查詢123
    web.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("123\n")
    web.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div[1]/a/h3').click()
    # 縣市當下頁面的URL
    print('Url: ' + web.current_url)
    sleep(2)
    web.close()
except:
    print('查詢失敗')
    web.close()