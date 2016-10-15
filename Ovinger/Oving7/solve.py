#!/usr/bin/python3
#-*- coding: utf-8 -*-

resultatet = [None] * (1 + 1)
for w in range(1+ 1):
	resultatet[w] = [-1] * (1 + 1)

def max_value(bredder, hoyder, verdier, paper_width, paper_height):
	#print bredder, hoyder, verdier, paper_width, paper_height
	#[2, 2, 4] [3, 3, 5] [5, 4, 16] 10 3
	try:
		if resultatet[paper_width][paper_height] > 0:
			return resultatet[paper_width][paper_height]
	except:
		pass
	try:
		for i in range(paper_width-len(resultatet) + 1):
			resultatet.append(0)
		for i in range(paper_width-len(resultatet)+1):
			if len(resultatet[i]) < paper_height +1:
				for j in range(len(resultatet[i]), paper_height+1-len(resultatet[i])):
					resultatet[i][j] = -1
		resultatet[i] = [-1] * (paper_width+1)
	except:
		resultatet = [None] * (paper_width + 1)
		for w in range(paper_width + 1):
			resultatet[w] = [-1] * (paper_height + 1)
	minSize = float("inf")
	for x in range(len(verdier)):
		if bredder[x] <= paper_width and hoyder[x] <= paper_height and resultatet[bredder[x]][hoyder[x]] < verdier[x]:
			resultatet[bredder[x]][hoyder[x]] = verdier[x]
		if hoyder[x] <= paper_width and bredder[x] <= paper_height and resultatet[hoyder[x]][bredder[x]] < verdier[x]:
			resultatet[hoyder[x]][bredder[x]] = verdier[x]
    
	for w in range(paper_width + 1):
		for h in range(paper_height + 1):
			if resultatet[w][h] == 0:continue
			if resultatet[w][h] == -1: beste = 0
			else: beste = resultatet[w][h]
			for breddeKutt in range(1, w):
				if beste < resultatet[breddeKutt][h] + resultatet[w - breddeKutt][h]: beste = resultatet[breddeKutt][h] + resultatet[w - breddeKutt][h]
			for hoydeKutt in range(1, h):
				if beste < resultatet[w][hoydeKutt] + resultatet[w][h - hoydeKutt]: beste = resultatet[w][hoydeKutt] + resultatet[w][h - hoydeKutt]
			resultatet[w][h] = beste
	
	return resultatet[paper_width][paper_height]

def main():
	from sys import stdin
	bredder, hoyder, verdier = [],[],[]
	forste = stdin.readline()
	info = [':'.join(i.replace(')','').replace('(','').split('x')).split(':') for i in forste.split()]
	for i in range(len(info)):
		bredder.append(info[i][0]); hoyder.append(info[i][1]); verdier.append(info[i][2])
	bredder = list(map(int,bredder)); hoyder = list(map(int, hoyder)); verdier = list(map(int,verdier))
	papirer = []
	stri = ""
	for line in stdin:
		paper_width, paper_height = [int(x) for x in line.split('x', 1)]
		stri +=str(max_value(bredder, hoyder, verdier, paper_width, paper_height)) + '\n'
	print(stri.strip('\n'))
	
if __name__ == "__main__":
	main()

