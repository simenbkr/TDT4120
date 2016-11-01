#!/usr/bin/python3
Inf = float(1e3000)
def mst(nm):
	denne_noden = 0
	antall_noder = len(nm)
	noder_ink = []
	node_tall = []
	mulige_noder = []
	for iterasjoner in range(antall_noder-1):
		for node, vekt in enumerate(nm[denne_noden]):
			if node not in node_tall and vekt != Inf:
				mulige_noder.append((denne_noden, node, vekt))	
		minimum, minimum_kant, minste_indeks = Inf, None, None
		for i, kant in enumerate(mulige_noder):
			if kant[2] < minimum:
				minimum = kant[2]
				minimum_kant = kant
				minste_indeks = i
		index, kant = minste_indeks, minimum_kant
		mulige_noder.pop(index)
		noder_ink.append(kant)
		node_tall.append(denne_noden)
		denne_noden = kant[1]
	maks = -Inf
	for node in noder_ink:
		if node[2] > maks:
			maks = node[2]
	return maks
	
def main():
	from sys import stdin
	lines = []
	for str in stdin:
		lines.append(str)
	n = len(lines)
	neighbour_matrix = [None] * n
	node = 0
	for line in lines:
		neighbour_matrix[node] = [Inf] * n
		for k in line.split():
			data = k.split(':')
			neighbour = int(data[0])
			weight = int(data[1])
			neighbour_matrix[node][neighbour] = weight
		node += 1
	print (mst(neighbour_matrix))
try:
	main()
except: print(Inf)