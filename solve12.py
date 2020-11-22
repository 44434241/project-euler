#!/usr/bin/python3
ans = 0
MAX = int(1e8)
grid = [0] * MAX

for i in range(1, MAX):
	for j in range(i, MAX, i):
		grid[j] += 1

max_grid = 0
for i in range(1, 999999):
	ans += i
	if ans > MAX:
		print ("reached max, max = {}".format(max_grid)), exit(1)
	max_grid = max(max_grid, grid[ans])
	if grid[ans] > 500:
		break

print (ans)
