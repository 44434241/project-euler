#!/usr/bin/python3
ans = 0
def is_palin(num):
	s = str(num)
	tmp = len(s) // 2

	return s[:tmp] == s[::-1][:tmp]
for a in range(100, 1000):
	for b in range(100, 1000):
		if is_palin(a * b):
			ans = max(ans, a * b)

print (ans)
