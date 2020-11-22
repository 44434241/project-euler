#!/usr/bin/python3
ans = 0
of_one_strings = [
	"", # 0
	"one",
	"two",
	"three",
	"four",
	"five",
	"six",
	"seven",
	"eight",
	"nine"
]
of_ten_strings = [
	"", # 0
	"", # 1
	"twenty",
	"thirty",
	"forty",
	"fifty",
	"sixty",
	"seventy",
	"eighty",
	"ninety"
]

till_twenty_strings = [
	"ten",
	"eleven",
	"twelve",
	"thirteen",
	"fourteen",
	"fifteen",
	"sixteen",
	"seventeen",
	"eighteen",
	"nineteen"
]

def int_len(num):
	if num >= 1000:
		return int_len(num // 1000) + len("thousand") + int_len(num % 1000) 
	if num >= 100:
		return int_len(num // 100) + len("hundred") + int_len(num % 100) + (0 if num % 100 == 0 else 3)
	if num >= 20:
		return len(of_ten_strings[num // 10]) + int_len(num % 10)
	if num >= 10:
		assert till_twenty_strings[num-10] != ""
		return len(till_twenty_strings[num - 10])
	if num >= 0:
		return len(of_one_strings[num])

ans = sum(int_len(i) for i in range(1, 1001))
print (ans)
