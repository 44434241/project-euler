#!/usr/bin/python3

_primes = [2]
def is_prime(num):
	if num <= 1:
		return True
	for i in _primes:
		if num % i == 0:
			if num == i:
				return True
			return False
	_primes.append(i)
	return False

# (that doesnt make sense i have no idea what my intention with it was but i'm sure ill figure it out)
