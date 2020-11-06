# 多行一起註解的快節鍵: Ctrl+/

data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count%1000 == 0:  # 每讀1000筆留言印一次
            print(len(data))

print('檔案讀取玩了，總共有',len(data),'筆資料')

sum_len = 0
for d in data:
    sum_len += len(d)

print('每筆留言平均長度為', sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)

print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
   if 'good' in d:
       good.append(d)
print('一共有', len(good),'筆留言提到good')


#文字計數
wc = {}  # word_count
words = []
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] =1  # 新增新的key進wc字典

for word in wc:
    if wc[word] >1000000:
        print(word, wc[word])
print(len(wc))
print(wc['Allen'])

while True:
    word = input('你想要查什麼字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為: ', wc[word])
    else:
        print('這個字沒有出現過喔!')

print('感謝使用本查詢功能')



