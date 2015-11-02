# -*- coding: utf-8 -*-
#Napište funkce nad seznamem čísel, které zjistí:

#součet všech čísel v seznamu,
#nejvyšší číslo v seznamu,
#zda se určitá hodnota vyskytuje v seznamu,
#tedy ekvivalenty operací max, sum a in (ale s použitím pouze základních operací nad seznamy).

def my_sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

def my_max(numbers):
    max = 0
    for i in numbers:
        if i > max:
            max = i
    return max

def my_in(x, array):
    if x in array:
        return True
    else:
        return False

print my_sum([6, 5, 11, 8])    # 30
print my_max([6, 5, 11, 8])    # 11
print my_in(5, [6, 5, 11, 8])  # True
print my_in(4, [6, 5, 11, 8])  # False

#Napište funkci, která vypočítá součin čísel v seznamu, ale ignoruje přitom případné nuly.

def nonzero_product(numbers):
    total = 1
    for i in numbers:
        if i == 0:
            pass
        else:
            total *= i
    return total

print nonzero_product([0, 2, 3, 0, 0, 3])    # 18
print nonzero_product([0, 0, 0, 0])          # 1

#Napište funkci double_all, která dostane na vstupu seznam čísel a každý jeho prvek vynásobí dvěma.
#Dále napište funkci create_doubled, která dostane na vstupu seznam čísel a vrátí nový seznam získaný ze vstupního tak, že každý prvek vynásobí dvěma. 
#Na rozdíl od předchozí funkce však nemění předaný seznam.

def double_all(numbers):
    for i in range(len(numbers)): # ak sa chcem pozerat na prvky zoznamu, musim ist cez range
        numbers[i] *= 2
    print numbers

def create_doubled(numbers):
    b = []
    for i in numbers:
        b.append(i*2)
    return b

a = [1, 4, 2, 5]
double_all(a)
print a  # [2, 8, 4, 10]

a = [1, 4, 2, 5]
b = create_doubled(a)
print a  # [1, 4, 2, 5]
print b  # [2, 8, 4, 10]

# Napište funkci, jejímž vstupem je seznam seznamů a výstupem je seznam, který obsahuje prvky všech jednotlivých seznamů.
def flatten(lists):
    flat = []
    for list_ in lists:
        for element in list_:
            flat.append(element)
    return flat 

print flatten([[0, 2, 3], [1, 2, 3], [9, 10]])
# [0, 2, 3, 1, 2, 3, 9, 10]

#Napište funkci, která vrátí nový řetězec, ve kterém bylo každé písmenko zdvojeno.

def duplication(text):
    word = ""
    for i in text:
        double = i*2
        word += double
    return word

print duplication("PYTHON")
# PPYYTTHHOONN

# Napište funkci, která vám vrátí řetězec s písmeny uspořádanými pozpátku.

def reverse(text):
    word = ""
    for i in text[::-1]:
        word += i
    return word

print reverse('ONMEJATEJOLSEH')
# H E S L O J E T A J E M N O

#Napište funkci, která spočítá počet výskytů písmene (znaku) A/a.

def count_a(text):
    counter = 0
    for char in text.lower():
        if char == "a":
            counter += 1
    return counter

print count_a('Liska Adelka')
# 3

#Napište funkci, která zcenzuruje dodaný řetězec tak, že každé druhé písmeno nahradí za X.

def censorship(text):
    word = ""
    for char in text[:-1:2]:
        word += char+"X"
    return word

print censorship("Vinnetou: Jsem krestan.")
# VXnXeXoX:XJXeX XrXsXaX.

# Napište funkci, která dostane dva řetězce a vypíše ty znaky, které jsou na shodných pozicích stejné.

def string_intersection(left, right):
    for i in range(len(left)):
        if left[i] == right[i]:
            print left[i],

string_intersection('ZIRAFA', 'KARAFA')
# R A F A
string_intersection('PES', 'KOCKA')
# (prazdny retezec)

def diff_a(left, right):
    return abs(count_a(left) - count_a(right))

#Napište funkci, která vrátí, zda je řetězec palindromem.
#Palindromem je takové slovo či věta, která má při čtení v libovolném směru stejný význam, například nepotopen či jelenovi pivo nelej (mezery můžete ignorovat).    
def palindrom(text):
    backword = text[::-1]
    return backword == text

print palindrom("JELENOVIPIVONELEJ")
# True

#Každý znak A-Z má hodnotu 1-26 (diakritiku a velikost písmen pro tento příklad ignorujte).
# Napište funkci, která spočítá a vrátí hodnotu vloženého řetězce (slova).

import string

def word_value(text):
    val = 0
    for char in text.upper():
        val += (ord(char)-64) # A begins on 65
    return val

print word_value("ahoj")
# 34

# -*- coding: utf-8 -*-

# Napište funkci pro kapitalizaci všech slov v dodaném vstupním řetězci.
# -*- coding: utf-8 -*-
def capitalize(text):
    return text.title()
        
print capitalize("jenom tak klidne levituji ve vzduchu.");
# Jenom Tak Klidne Levituji Ve Vzduchu


# Napište funkci pro generování náhodných řetězců, která bude brát dva parametry: 
# length udávající délku výstupu a chars obsahující řetězec všech povolených znaků.
import random

def random_string(length, chars):
    word = ""
    for char in range(length):
        word += random.choice(chars)
    return word

print random_string(10, "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

# Napište funkci se dvěma parametry needle (jehla) a haystack (kupka sena) pro hledání začáteční pozice subřetězce.
# Pokud nebude podřetězec nalezen vrátí funkce -1.

# Poznámka: použijte naivní algoritmus... ona existuje spousta chytrých algoritmů na hledání podřetězců, jejichž pochopení a implementace je nad rámec tohoto předmětu.
def search(needle, haystack):
    index = -1
    
    if needle in haystack:
        for char in haystack:
            index += 1
            if needle == haystack[index:index + len(needle)]:
                break
    else:
        pass                     
    
    return index

print search("tro", "bratr")
# 3

#Napište funkci, která zašifruje text tak, že posune všechna jeho písmena v abecedě o n dopředu (cyklicky)
# můžete se inspirovat popisem Caesarovy šifry.
import string
    
def caesar(text, klic):
    word = ""
    newLetter = ""
    for c in text.upper():
        if c == "" :
            word += ""
        elif ord(c)+klic > ord("Z"):
            newLetter = chr(ord(c) + klic - 26)
        else:
            newLetter = chr(ord(c)+klic)
        word += newLetter
    return word

print caesar('zirafa', 3)
# CLUDID

#Napište funkci, která zašifruje text podle předem daného klíče. Pro posun písmen zdrojového textu se postupně používají písmena z klíče: ‘a’ posouvá o 0, ‘b’ o 1, ... ‘z’ o 25. 
#Pokud je klíč kratší než zdrojový text, jsou použita písmena z klíče opět od začátku. 
#Můžete se inspirovat popisem Vigenèrovy šifry.
