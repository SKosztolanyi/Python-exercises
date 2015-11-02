# -*- coding: utf-8 -*-
def binarne(n):
    new = ""
    while n > 0:   
    	if n % 2 == 0: new += "0"
    	else: new += "1"
        n /= 2
    return int(new[::-1])
    
def binarne2(n):
    new = ""
    while n>0:
        if n % 2 == 0:
            new += "0"
        else: 
            new += "1"
        n = int(n/2) # implicitne tu bol float, takže sa to muselo upravit
    print int(new[::-1])
    
def tajna_posloupnost(n):
    count = n
    for i in range(1, n+1):
        if count == 0:
            break
        for j in range(1, i+1):
            print j,
            count -= 1
            if count == 0:
                break
                
def tajna_posloupnost2(n):
    aktualni = 1
    strop = 1
    for i in range(n):
        print aktualni,
        aktualni += 1
        if aktualni > strop:
            aktualni = 1
            strop += 1
            
def velkex(n):
    for i in range(1, n+1):
    	for j in range(1, n+1):
            if i == j or i == (n-j+1):
                print "#",
            else:
                print ".",
        print
        
def velkex2(n):
    for x in range(n):
        for y in range(n):
            if x == y or x == n - 1 - y: print '#',
            else: print '.',
        print

def prvni_pismena(text):
    smes = text[0]
    for i in range(len(text)):
        if text[i-1] == " ":
            smes += text[i]
    return smes

def cikcak(text):
    for i in range(len(text)):    
        if i%2 == 0:
            print text[i],
        else:
            print ".",
    print
    for j in range(len(text)):
        if j%2 == 1:
            print text[j],
        else:
            print ".",

cikcak("PARDUBICE")

def ctverec(n):
    for i in range(n):   
    	if i == 0 or i == (n-1):
            print "*"*n
       	else:
            print "*" + "+"*(n-2) + "*" 
        
ctverec(9)

import string

def caesar(text, klic):
    words = ""
    newLetter = ""
    for c in text:
        if c == " " :
            words += " "
        elif ord(c)+klic > ord("z"):
            newLetter = chr(ord(c) + klic - 26)
            words += newLetter
        else:
            newLetter = chr(ord(c)+klic)
            words += newLetter
    return words

caesar("Pivko na trave.", 7)

def nejdelsi_slovo(text):
    slova = text.split(" ")
    nejdelsi = ""
    for slovo in slova:
        if len(slovo) >= len(nejdelsi):
            nejdelsi = slovo
    return nejdelsi
    
def frekvencni_analyza(text):
    for i in range(26):
        pismeno = chr(ord('a')+i)
        if pismeno in text:
            count = 0
            for char in range(len(text)):
                if pismeno == text[char]:
                	count += 1
            print pismeno, count
            
frekvencni_analyza("lopatkova nadrz na odreagovanie zdochliny")

def sachovnice(n): 
    # Funguje len pri n je parne
    for y in range(1, n+1):
        if y%2 != 0:
            print "X . "*n,
            print
    	else:
            print ". X "*n,
            print
            
def ciferny_soucet(n):
    soucet = 0
    while n > 1:        
        soucet += n % 10
        n /= 10
        print n
    return soucet

