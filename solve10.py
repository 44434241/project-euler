#!/usr/bin/python3
# accidentally did it the slower way, takes like 3 minutes, oops
ans = 0
def solve(args):
	global ans
	for i in args:
		ans += i

primes = []
def check_prime(num):
	global primes
	for i in primes:
		if num % i == 0:
			return
	primes.append(num)

check_prime(2)

for i in range(3, int(2e6), 2):
	check_prime(i)

solve(primes)
print (ans)
