

mp = {}

def d(num):
	if num in mp:
		return mp[num]
	
	ans = 0
	for i in range(1, num):
		if num % i == 0:
			ans += i
	
	mp[num] = ans
	return ans

mx = 10000
total = 0
for i in range(1, mx):
	other = d(i)
	if i < other and d(other) == i:
		total += i + other
	continue
	flg = False
	for j in range(1, mx):
		if i == j:
			continue
		if d(i) == d(j):
			flg = True
			break
	if flg:
		total += i 
	print(i, flg)

print(total)
