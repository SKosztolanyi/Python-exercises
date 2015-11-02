# -*- coding: utf-8 -*-
def posl1(N):
    '''
    prints odd integers divisible by 7
    '''
    for i in range(N):
        if i%2 == 1 and i%7 ==0:
                print i
    # This functions has two conditions, and returns the integet that fulfils both.

def posl2(N):
    '''
    This function returns increasing odd numbers followed by 2.
    '''
    # vas kod
    for i in range(1, N+1): # The 1 is to exclude 0. The +1 is to add the N to the end.
        if i%2==0:
           print 2,
        else:
            print i,

def tabulka(N):
    '''
    Funkce vypíše tabulku malé násobilky pro dané N. Pozor na zarovnání u větších číslic (stačí přizpůsobit pro dvojciferné čísla).
    '''
    # vas kod
    for i in range (1, N+1):
        for j in range(1, N+1):
            print i*j,
        print # This statement functions like enter, ending a line and starting a new one.
# V tomto pripade som nedokazal urobit formatovanie a nedokazal som vytvorit cisla pred tabulkou, cize ake cislo s akym nasobene da ten ktory vysledok v tabulke.
# To, co sa mi podarilo, bolo vytvorit cistu tabulku nasobenia pomocou vnoreneho cyklu      

def pyramida(N):
    '''
    Funkce vytiskne pyramidu o N patrech.
    '''
    # vas kod
    inside=0
    for i in range(N):
        if i<1:
            print (N-i)*" ", "*",(N-i)*" ",
            print
        else:
            print (N-i)*" ", "*", (inside)*" ", "*",
            inside+=2
            print
#Prvy riadok funkcie je iny, pretoze vytlacim iba 1 mriezku.
#Kedze na prvom riadku chcem len 1 mriezku, chcem ju umiestnit do stredu pyramidy.
#V dalsich riadkoch chcem umiestnit mriezku stale menej od kraju, preto N-i.
#Sucasne potrebujem zvysovat medzeru vovnutri pyramidy, preto clen "inside".

#Neviem ci je tato pyramida identicka s predlohou, ale vizualne sa jej najviac podoba.

from math import pi
from turtle import Turtle
julie = Turtle()
julie.speed(10)

def oblouk(radius, angle):
    for j in range(angle):
        julie.right(90)
        for i in range(radius):
            julie.forward(pi)
            julie.right(2)

oblouk(90, 6)

def flower(radius, angle, leaves):
    for i in range(leaves):
        julie.forward()
        
## Tu som sa na to snazil ist cez obluk. Este sa mi to nepodarilo optimalizovat, ale uz nemam na to cas aby som to doriesil.
## V podstate by som potreboval nakreslit pocet zhodnych listov za sebou v spravnych uhloch, aby vytvorili kvet.
## Myslim, ze mi tam chyba este jeden for loop pre leaves.