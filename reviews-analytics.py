import time
import progressbar


# 資料有幾筆
data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('053 reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)	
print('資料讀取完了，總共有', len(data), '筆資料')

# print(data[0])


# 留言的平均長度
Filter_commont = 0
for d in data:
	count += len(line)
print('留言的平均長度為,', count/1000000)	


# 留言長度小於100字
new = []
for d in data:
	if len(d) < 100:
		new.append(d)	
print('有', len(new), '留言長度小於100字') 


#有good的留言
good_massage = []
good = 'good'
for  d in data:
	if good in d:
		good_massage.append(d)
print('有good的留言有', len(good_massage), '筆')


# for i in range(100):
# 	print('hi')		
	

#文字計數
start_time = time.time()
wc = {}
count = 1
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += count
		else:
			wc[word] =	count # 新增新的key進wc字典
for word in wc:
	if wc[word] > 1000000:
		print(word, ':', wc[word])	
end_time = time.time()
print(len(wc))
print('花了', int(end_time - start_time), '秒')	