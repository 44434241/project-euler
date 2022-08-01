
def is_leap(yr):
	if yr % 4 != 0:
		return False
	if yr % 100 == 0:
		return yr % 400 == 0
	return True
# how much days are from this to start of `y`

def get_m(yr):
	return [31, (29 if is_leap(yr) else 28), 31,
			30, 31, 30,
			31, 31, 30,
			31, 30, 31]

def get_day_cnt(y):
	res = 0
	for yr in range(1900, y+1):
		res += 30 * 4
		res += 31 * 7
		res += 29 if is_leap(yr) else 28
	return res

ans = 0
for yr in range(1900, 2000):
	s = 0
	#print(get_m(yr))
	for m in get_m(yr):
	#v = (((get_day_cnt(yr) + 1)// 7) - get_day_cnt(yr) // 7)
		cnt = get_day_cnt(yr) + s
		#print(cnt%7)
		if cnt % 7 == 0:
			#print(m)
			ans += 1
		s += m
	#print(yr, v)

#print(get_day_cnt(1910) % 7)
print(ans)


