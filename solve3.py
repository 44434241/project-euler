#!/usr/bin/python3
ans = 0
num = 600851475143
i = 2
while i <= num:
	while num % i == 0:
		ans = num
		num //= i
	i += 1


print (ans)
