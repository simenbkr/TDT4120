#!/usr/bin/python

from sys import stdin, stderr
import traceback

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def bygg(ordliste):
    # SKRIV DIN KODE HER
    topp = Node()
    for ord in ordliste:
        parent = topp
        for a in ord[0]:
            if a not in parent.barn:
                parent.barn[a] = Node()
            parent = parent.barn[a]
        parent.posi.append(ord[1])
    return topp         
        
def posisjoner(ord, indeks, node):
    # SKRIV DIN KODE HER
    if indeks == len(ord):
        return node.posi

    elif ord[indeks] == '?':
        resultat = []
        for key in node.barn:
            resultat += (posisjoner(ord, indeks+1, node.barn[key]))
        return resultat

    elif ord[indeks] not in node.barn:
        return []

    else:
        return posisjoner(ord, indeks+1, node.barn[ord[indeks]])

try:
    ord = stdin.readline().split()
    ordliste = []
    pos = 0
    for o in ord:
        ordliste.append( (o,pos) )
        pos += len(o) + 1
    toppnode = bygg(ordliste)
    for sokeord in stdin:
        sokeord = sokeord.strip()
        print (sokeord + ":", end='')
        posi = posisjoner(sokeord, 0, toppnode)
        posi.sort()
        for p in posi:
            print(' '+str(p),end='')
        print()
except:
    traceback.print_exc(file=stderr)