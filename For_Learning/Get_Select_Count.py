from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

# 開啟無痕模式
option = webdriver.ChromeOptions()
option.add_argument('--incognito')
web = webdriver.Chrome(options=option)

web.get('http://www.wibibi.com/info.php?tid=194')

sleep(2)
try:
    # 取得下拉選單的數量
    m = Select(web.find_element_by_xpath('//*[@id="CodeBox1"]/select'))
    print('有', len(m.options), '個項目')
    # 顯示每個元素位置的文字; Range(x,y) 從x 數到 y-1
    for i in m.options:
        print(i.text)
    web.close()
except:
    print('Fail')
    web.close()
