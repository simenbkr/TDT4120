#!/usr/bin/python

from sys import stdin


class Record:
    value = None
    next = None

    def __init__(self, value):
        self.value = value
        self.next = None
    def getValue(self):
        return self.value
    def getNext(self):
        return self.next

def search(record):
	try:
		maks = record.getValue()
		neste = record.getNext()
	except:
		return None
	while neste != None:
		if neste.getValue()>maks:
			maks = neste.getValue()
		if neste.getNext() is None: break
		neste = neste.getNext()
	return maks


def main():
    # reading from stdin and creating a linked list
    first = None
    last = None
    for line in stdin:
        penultimate = last
        last = Record(int(line))
        if first is None:
            first = last
        else:
            penultimate.next = last

    # searching and printing out the result
    print(search(first))


if __name__ == "__main__":
    main()
