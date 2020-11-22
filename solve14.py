#!/usr/bin/python3
import sys
#sys.setrecursionlimit(int(1e7))
ans = (0, 0)
MAX = int(1e7)
dp = [-1] * MAX
dp[1] = 1
slow_dp = {}
slow_dp[1] = 1

def solve(num):
	if num > MAX or True:
		if num in slow_dp:
			return slow_dp[num]
		if num & 1 == 1:
			slow_dp[num] = solve(num * 3 + 1) + 1
		else:
			slow_dp[num] = solve(num // 2) + 1
		return slow_dp[num]

	if dp[num] != -1:
		return dp[num]
	if num & 1 == 1:
		dp[num] = solve(num * 3 + 1) + 1
	else:
		dp[num] = solve(num // 2) + 1
	return dp[num]


for i in range(1, int(1e6)):
	
	ans = max(ans, (solve(i), i))

print (ans[1])
