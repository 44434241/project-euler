#!/usr/bin/python3
ans = 0
MAX = 25
dp = [[0] * 25 for _ in range(25)]
dp[0][0] = 1
for x in range(21):
	for y in range(21):
		dp[x+1][y] += dp[x][y]
		dp[x][y+1] += dp[x][y]

ans = dp[20][20]
print (ans)
