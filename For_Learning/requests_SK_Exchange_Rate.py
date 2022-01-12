import requests
import time

exchange = input('選擇要做的功能 1:檢查匯率 2:計算兌換金額 ')
category = input('請輸入貨幣類別 1:美金 2:日幣 3:人民幣 4:港幣 ')

# 取得真實時間
second = int(time.time())

# 設置查詢參數
search = {'action': 'rate', 'rateType': 'ExchangeRate', 'v': time.time()}
# 增加URL查詢參數方法 params
shingown = requests.get('https://www.skbank.com.tw/skbank_web/data', params=search)

# 轉換為json格式
data = shingown.json()

# 取得指定dictionary值
table = data['tableJSON']['table']['row']['data'][int(category)-1]

y = []

# 尋找指定的值並將其存放至list中
for x in table:
    exchange_rate = x['itemContent']
    y.append(exchange_rate)


if exchange == '1':
    print('貨幣類型:', y[0], '\n買進匯率:', y[2], '\n賣出匯率:', y[3])
elif exchange == '2':
    Conversion = input('選擇轉換方式 1:台幣轉外幣 2:外幣轉台幣 ')
    Amount = input('請輸入轉換金額: ')

    # 依據input結果，計算金額、取小數點第二位的方法('%.2f' % 變數)
    if Conversion == '1':
        NT = float(Amount) / float(y[3])
        print('當下匯率:', y[3] + '\n', y[0], '%.2f' % NT)
    elif Conversion == '2':
        NT1 = float(Amount) * float(y[2])
        print('當下匯率:', y[2], '\nNT', '%.2f' % NT1)
    else:
        print('輸入發生錯誤')
else:
    print('無此項功能')



