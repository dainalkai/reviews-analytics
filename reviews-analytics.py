data = []
count = 0
Filter_commont = 0
with open('053 reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		total_len = len(line)
		if total_len < 100:
			Filter_commont += 1
		count += total_len
		if count % 1000 == 0:
			print(len(data))
average_len = count/1000000			
print('資料讀取完了，總共有', len(data), '筆資料')
print('留言的平均長度為,', average_len)
print('有', Filter_commont, '留言長度小於100字') 


	