#!/usr/bin/python3
from sys import stdin
#from string import ascii_lowercase as chars
from collections import deque

BASE = 26
"""
def flexradix(A, d):
	lista = deque(A)
	
	for i in range(d,-1,-1):
		hauger = deque([deque() for _ in range(len(chars))])
		
		for string in lista:
			if len(string) > i:
				indeks = chars.index(string[i])
			else:
				indeks = 0
			hauger[indeks].append(string)

		lista = deque()
		for haug in hauger:
			lista.extend(haug)
	return lista
"""



def flexradix(A,siffer):
	
	if len(A) <= 1: return A
		
	ferdig = []
	hauger = [[] for _ in range(BASE)]

	for streng in A:
		if siffer >= len(streng):
			ferdig.append(streng)
		else:
			hauger[ord(streng[siffer])-ord('a')].append(streng)
	
	hauger = [flexradix(haug, siffer+1) for haug in hauger]
	
	return ferdig + [b for haugene in hauger for b in haugene]

def main():
	d = int(stdin.readline())
	strings = []
	for line in stdin:
		strings.append(line.rstrip())
	A = flexradix(strings, 0)
	for string in A:
		print(string)


if __name__ == "__main__":
	main()
