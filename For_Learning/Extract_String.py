text = '6516516516 sdfasdf asdfsdfsadfsdfds    asdfsdfasdfsdf    ABCE-EEEE-FFFF-CCCC\n\r\n'

# 取得key的起始位置與結束位置
start = text.index('-') - 4
end = text.index('-') + 15

key = text[start:end]

# 將key放入list
key_list = key.split('-')

# 將list各元素放入字串並用 . 區隔
key_str = '.'.join(key_list)

print(key_str)

new_str = key_list[0], key_list[1], key_list[2]

print(new_str)
