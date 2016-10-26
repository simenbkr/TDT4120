#!/usr/bin/python3
class Node:
	def __init__(self):
		self.child = []
		self.ratatosk = False
		self.next_child = 0
		self.dybde = 0
def dfs(root):
	stack = [root]
	while len(stack) > 0:
		denne_noden = stack.pop()
		if denne_noden.ratatosk: return denne_noden.dybde
		for barn in range(len(denne_noden.child) - 1, -1, -1):
			denne_noden.child[barn].dybde = denne_noden.dybde + 1
			stack.append(denne_noden.child[barn])
def bfs(root):
	from collections import deque
	queueueueueu = deque([(root, 0)])
	while len(queueueueueu) > 0:
		tmp, path_length = queueueueueu.popleft()
		if tmp.ratatosk: return path_length		
		for barn in tmp.child: queueueueueu.append((barn, path_length + 1))	
def main():
	from sys import stdin
	function = stdin.readline().strip()
	number_of_nodes = int(stdin.readline())
	nodes = []
	for i in range(number_of_nodes):
		nodes.append(Node())
	start_node = nodes[int(stdin.readline())]
	ratatosk_node = nodes[int(stdin.readline())]
	ratatosk_node.ratatosk = True
	for line in stdin:
		number = line.split()
		temp_node = nodes[int(number.pop(0))]
		for child_number in number:
			temp_node.child.append(nodes[int(child_number)])
	if function == 'dfs':
		print(dfs(start_node))
	elif function == 'bfs':
		print(bfs(start_node))
	elif function == 'velg':
		print(bfs(start_node))	
main()