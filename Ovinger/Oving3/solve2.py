#!/usr/bin/python3

from sys import stdin
from itertools import repeat
from collections import deque

def merge2(del1,del2):
	del3 = deque()
	del1 = deque(del1)
	del2 = deque(del2)
	
	while len(del1)>0 and len(del2)>0:
		if del1[0][0] > del2[0][0]:
			del3.append(del2[0])
			del2.popleft()
		else:
			del3.append(del1[0])
			del1.popleft()
	
	while len(del1)>0:
		del3.append(del1[0])
		del1.popleft()
	
	while len(del2)>0:
		del3.append(del2[0])
		del2.popleft()
	return del3

def mergesort(deck):
	if len(deck) == 1:
		return deck[0]
		
	del1 = deque()
	del2 = deque()
	
	length = len(deck)
	
	if length % 2 == 0:
		del1 = deck[:length//2]
		del2 = deck[length//2:]
	else:
		del1 = deck[:length//2]
		del2 = deck[length//2:]
	
	del1 = mergesort(del1)
	del2 = mergesort(del2)
	
	return merge2(del1,del2)
	
	

def merge(decks):
	"""
	[[(1, 'i'), (3, 'i'), (5, 'i'), (8, 'i')],
	[(2, 'n')],
	[(4, 't'), (7, 't')],
	[(6, 'a')],
	[(9, 'v')]]
	"""
	a = (mergesort(decks))
	#a = [i for sub in mergesort(decks) for i in sub]
	#print a
	
	return ''.join([item[1] for item in a if type(item[1]) == str])
	"""
	out = ''
	for index, char in a:
		out += char
	return out
	"""
	
	
	
	
	
	
	
	

def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))


if __name__ == "__main__":
    main()
