#!/usr/bin/python3

Inf = 1000000000
def min_coins_greedy(coins, value):
	coins = sorted(coins)[::-1]
	number = 0
	myvalue = 0
	for i in range(len(coins)):
		count = 0
		while (count+1)*coins[i] <= value and myvalue+(count+1)*coins[i] <= value:
			count +=1
		myvalue += count*coins[i]
		number += count	
	return number

def min_coins_dynamic(coins, value, length):
		
	antall = [0]
	for i in range(1,value+1):
		antall.append(antall[i-1] + 1)
		for mynt in coins:
			if mynt <= i and antall[i-mynt] + 1 < antall[i]:
				antall[i] = antall[i-mynt] + 1	
	return antall[value]

def can_use_greedy(coins):
	for i in range(1, len(coins)):
		if coins[i]%coins[i-1] != 0:
			return False
	return True
	
def main():
	from sys import stdin
	coins = []
	for c in stdin.readline().split():
		coins.append(int(c))
	coins.sort()
	coins.reverse()
	method = stdin.readline().strip()
	if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
		for line in stdin:
			print(min_coins_greedy(coins, int(line)))
	else:
		for line in stdin:
			print(min_coins_dynamic(coins, int(line), len(coins)))
			
			
if __name__ == '__main__':
	main()