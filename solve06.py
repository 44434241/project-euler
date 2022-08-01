#!/usr/bin/python3
ans = 0

tmp = 0
for i in range(101):
	ans += i
	tmp += i * i

ans = ans * ans - tmp
#ans *= ans

print (ans)
