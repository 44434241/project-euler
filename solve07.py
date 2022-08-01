#!/usr/bin/python3
import math
ans = 0
def is_prime(num):
	for i in range(2, min(math.ceil(math.sqrt(num))+1, num-1)):
		if num % i == 0:
			return False
	return True

cnt = 0
i = 2
seek = 10001
while True:
	if is_prime(i):
		cnt += 1
	if cnt == seek:
		ans = i
		break
	i += 1
print (ans)
