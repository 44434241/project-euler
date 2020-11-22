#!/usr/bin/python3
ans = 0
for a in range(1, 1000):
	for b in range(a+1, 1000 - a):
		c = 1000 - (a+b)
		if a * a + b * b == c * c:
			ans = a * b * c
			#print(ans)
				

print (ans)
