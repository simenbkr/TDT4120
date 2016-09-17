#!/usr/bin/python
from sys import stdin
def make_trie(words):
	root = dict()
	pos = 0
	for word in words:
		current_dict = root
		for letter in word:
			current_dict = current_dict.setdefault(letter,{})
		current_dict['_end_'] = '_end_'
		if '_value_' in current_dict:
			current_dict['_value_'].append(pos)
		else: current_dict['_value_'] = [pos]
		pos += len(word) + 1
	return root
def finnb(trie,ord,indeks):
	if indeks >= len(ord):
		return trie['_value_']
	elif ord[indeks] == '?' or ord[indeks] == '*':
		pos = []
		for char in trie:
			pos+= finnb(trie[char],ord,indeks+1)
		return pos
	elif ord[indeks] in trie:
		return finnb(trie[ord[indeks]],ord,indeks+1)
	else:
		return []

def finn(trie,ord):
	curr_dic = trie
	#for letter in ord:
	terms = ord.split('?')
	if not terms or len(terms) == 1:
		for i in range(len(ord)):
			letter = ord[i]
			if letter in curr_dic:
				curr_dic = curr_dic[letter]
			else: return None
		else:
			if '_end_' in curr_dic:
				return curr_dic['_value_']
			else: return None
	elif len(terms) == 2:
		return finnb(trie,ord,0)
	else:
		try:
			return finnb(trie,ord,0)
		except:
			return None
	return None
		

def main():
	try:
		settning = stdin.readline()
		ord = settning.split()
		trien = make_trie(ord)
	except: pass
	for sokeord in stdin:
		sokeord = sokeord.strip().strip('\n')
		print("%s:" % sokeord, end='')
		resultat = []
		try:
			resultat = sorted(finn(trien,sokeord))
		except: pass
		if resultat:
			for things in resultat:
				print(" %s" %things, end='')
		print()
		
if __name__ == '__main__':
	try:
		main()
	except: pass
