#!/usr/bin/python3

Inf = 1000000000
memo2 = {}
def min_coins_greedy(coins, value):
	if value in memo2: return memo2[value]
	antall, indeks = 0, 0
	while value > 0:
		if value/coins[indeks] >= 1:
			antall += value//coins[indeks]
			value %= coins[indeks]
		indeks += 1
	memo2[value] = antall
	return antall

memo = {}
def min_coins_dynamic(coins, value, length):
	if value in memo: return memo[value]
	antall = [0]
	for i in range(1,value+1):
		antall.append(antall[i-1] + 1)
		for mynt in coins:
			if mynt <= i and antall[i-mynt] + 1 < antall[i]:
				antall[i] = antall[i-mynt] + 1	
				memo[i] = antall[i]
	memo[value] = antall[value]
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
	coins.sort(reverse=True)
	method = stdin.readline().strip()
	if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
		for line in stdin:
			print(min_coins_greedy(coins, int(line)))
	else:
		for line in stdin:
			print(min_coins_dynamic(coins, int(line), len(coins)))
			

main()