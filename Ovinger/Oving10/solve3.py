#!/usr/bin/python3
def main():
	Inf = float(1e3000)
	from sys import stdin
	linjer = stdin.readlines()
	n = len(linjer)
	node = 0
	nList = [None]*n

	for linje in linjer:
		cNode = []

		for k in linje.split():
			data = k.split(':')
			weight = int(data[1])
			target = int(data[0])
			kant = (weight, target)
			cNode.append(kant)
		nList[node] = cNode
		node += 1
	from heapq import heappush, heappop
	heap = []
	merket = [0]*n
	tyngst = 0
	for i in nList[0]:
		heappush(heap, i)
	merket[0] = 1
	for i in range(1,n):
		if not 0 in merket:
			break
		
		while heap:
			kant = heappop(heap)
			target = kant[1]
			if merket[target]:
				continue
			merket[target] = 1
			
			if tyngst < kant[0]:
				tyngst = kant[0]
				
			for e in nList[target]:
				if not  merket[e[1]]:
					heappush(heap, e)
			break
	print(tyngst)
main()