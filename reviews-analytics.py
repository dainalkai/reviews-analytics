data = []
count = 0
with open('[LINE] Chat with 顧庭瑋.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))		
print('資料讀取完了，總共有', len(data), '筆資料')

print(data[0])

wc = {}
count = 1
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += count
		else:
			wc[word] =	count
for word in wc:
	if wc[word] > 100:
		print(word, wc[word])	







# data = []
# count = 0
# Filter_commont = 0
# with open('053 reviews.txt', 'r') as f:
# 	for line in f:
# 		data.append(line)
# 		total_len = len(line)
# 		if total_len < 100:
# 			Filter_commont += 1
# 		count += total_len
# 		if count % 1000 == 0:
# 			print(len(data))
# average_len = count/1000000			
# print('資料讀取完了，總共有', len(data), '筆資料')
# print('留言的平均長度為,', average_len)
# print('有', Filter_commont, '留言長度小於100字') 

# good_massage = []
# good = 'good'
# for  d in data:
# 	if good in d:
# 		good_massage.append(d)
# print('有good的留言有', len(good_massage), '筆')


# for i in range(100):
# 	print('hi')		
# 	