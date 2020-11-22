#!/usr/bin/python3

n1 = 1
n2 = 2

ans = 2
while True:
	n1, n2 = n2, n2 + n1
	if n2 >= int(4e6):
		break
	if n2 % 2 == 0:
		ans += n2


print (ans)
