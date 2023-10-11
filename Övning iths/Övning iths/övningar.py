# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 20:33:33 2023

@author: SKF
"""

# funktion som beräknar volymen av ett rätblock

def volym_rätblock(l, b, h):
    return l*b*h


# funktion för biljettpriserna för en konsert olika åldrar.

def biljett_automat(ålder):
    
    if 0 < ålder < 7:
        pris = 0
        return pris
    elif 7 < ålder <12:
        pris = 80
        return pris
    else:
        pris = 100
        return pris
    
pris = biljett_automat(10)

print(pris)


# funktion som ger ut information av en lista av siffror:max, min, medelvärde


def indata(lista):
    Max = max(lista)
    Min = min(lista)
    medel = sum(lista) / len(lista)
    return Max, Min, medel

max, min, medel = indata([1,4,3,8,7])

# funktion som kollar om ett ord är en palindrom eller inte ex: kajak

def palindrom(Ord):
    back_ord = ''
    for i in range(len(Ord)):
        back_ord += Ord [-1-i]
    if back_ord.lower( == Ord.lower():
        return f'{Ord} är ett palindrom'
    else:
        return f'{ord} är inte ett palindrom'
    
def palindrom(Ord):
    if Ord == Ord [: -1]:
        return f'{Ord} är ett palindrom'
    else:
        return f'{Ord}är inte ett palindrom' 
print(palindrom('kajak'))
        
    
                   



    
        
        
            