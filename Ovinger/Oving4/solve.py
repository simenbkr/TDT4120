#!/usr/bin/python3

from sys import stdin
def flyttNed(A,start,slutt):
	rot = start
	while True:
		barn = rot*2+1
		
		if barn > slutt: 
			break
		
		if barn+1 <= slutt and A[barn] < A[barn+1]:
			barn +=1
		
		if A[rot] < A[barn]:
			A[rot],A[barn] = A[barn],A[rot]
			rot = barn
		else:
			break
def sort_list(A):
	for start in range((len(A)-2)//2,-1,-1):
		flyttNed(A,start,len(A)-1)
	
	for slutt in range(len(A)-1,0,-1):
		A[slutt],A[0] = A[0],A[slutt]
		flyttNed(A,0,slutt-1)
	return A


def binsearch(A,n,higher):
	length = len(A)
	start = 0
	slutt = length-1
	while start <= slutt:
		mid = (start+slutt)//2
		
		if A[mid] == n:
			return n
		
		if A[mid] > n:
			slutt = mid-1
		else:
			start = mid+1

	if not higher:
		if start != 0:
			return A[start-1]
		else:
			return A[start]
	else:
		if slutt != length - 1:
			return A[slutt+1]
		else:
			return A[slutt]
	
def find(A, lower, upper):	
	return [binsearch(A,lower,False),binsearch(A,upper,True)]


def main():
	input_list = []
	for x in stdin.readline().split():
		input_list.append(int(x))
	sorted_list = sort_list(input_list)
	for line in stdin:
		word = line.split()
		minimum = int(word[0])
		maximum = int(word[1])
		result = find(sorted_list, minimum, maximum)
		print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
	main()