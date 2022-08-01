#!/usr/bin/python3
ans = 1
def lcm(a, b):
	local_ans = 1
	i = 2
	while a != 1 or b != 1:
		while a % i == 0 or b % i == 0:
			local_ans *= i
			if a % i == 0:
				a //= i
			if b % i == 0:
				b //= i

		i += 1
	return local_ans

for i in range(2, 21):
	ans = lcm(ans, i)
print (ans)
