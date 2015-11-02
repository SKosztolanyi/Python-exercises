# -*- coding: utf-8 -*-
# Podminky:
# velikost_planu je prirozene cislo urcujici delku drahy
# cilovych_poli je prirozene cislo urcujici kolik je cilovych poli od konce
# vypis je boolean hodnota (True, False), ktera rika zda se ma
# vypisovat informativni vypis (viz priklad nize)


import random
# ukol 1
def clovece(velikost_planu, cilovych_poli, vypis):
    '''
    velikost_planu = pocet policek hraci plochy
    cilovych_poli = pocet poli, ktere predstavuji cil
    vypis = True or False, pokud je True, vypise vsechny tahy a hody
    '''
    pocet_hodu = 0
    poloha = 0
    vysledek_hodu = 0
    prvni_cilove_policko = velikost_planu - cilovych_poli +1
    posledni_cilove_policko = velikost_planu
    while poloha < prvni_cilove_policko or poloha > posledni_cilove_policko:
        hod = random.randrange(1, 7)
        pocet_hodu += 1
        if hod == 6:
            hod2 = random.randrange(1, 7)
            vysledek_hodu = hod + hod2
            if (poloha + vysledek_hodu) <= posledni_cilove_policko:
                poloha += vysledek_hodu     
        elif (poloha + hod) <= posledni_cilove_policko:
            poloha += hod
        if vypis == True:
            if hod == 6:
                print "V", pocet_hodu, ". kole padlo", hod, hod2
                print "Jsem na pozici ", poloha 
            else:
                print "V", pocet_hodu, ". kole padlo", hod
                print "Jsem na pozici ", poloha     
    print "Hra dokoncena v", pocet_hodu,". kole"
    # Ak chcem pocitat v dalsej funkcii s potctom hodov, musim skryt print a vracat iba jedno cislo pomocou return
    return pocet_hodu


# Popis hry:
# Kedze pri hode cisla 6 ide hrac znovu, ma osobitne podmienky ako pre scitavanie hodov, tak pre vypis akcie.
# Pravidla hry dovoluju hadzat znova kockou len 1 krat a to aj v pripade, ze by druhy hod bol znova 6
# Maximalny posun za jeden tah je teda o 12 policok
# Velikost planu je sucasne poslednym polickom na hracej ploche.
# Ak je iba 1 cielove policko, je totozne s velkostou planu
# Ak je cielovych policok viac


# Ukol 2
def prumerna_delka_trvani(kolik):
    '''
    kolik = pocet partii ve hre clovece
    Tato funkce pocita prumernou delku hry pro ruzne druhy hracich ploch
    Z poctu odehranych partii udela funkce prumer tak, ze vydeli soucet tahu poctem partii.
    '''
    vsechny_prumery = []
    for j in range(1, 6):
        for k in range(5, 31):
            delka_her = []
            prumerna_delka = 0.0
            for i in range(kolik):
                delka_partie = (clovece(k, j, False))
                delka_her.append(delka_partie)
                prumerna_delka += delka_partie
            print "pro velikost pole", k, "a velikost cile", j,
            print "je prumerna delka hry", prumerna_delka/kolik, "tahu."
            vsechny_prumery.append(prumerna_delka/kolik)
    print vsechny_prumery
    print len(vsechny_prumery)
    
# Kedze som pracoval s hodnotami 1 az 5 cielovych poli vratane a velkost plochy 5 az 30 vratane,
# vysledny pocet priemerov je 130 a nie 125. Nevidim dovod, preco by som to mal zmenit, pretoze nie je zrejme, ci nezahrnut 5 alebo 30.
# Nie je to sice tabulka, ale je to zoznam

# Legenda ku zoznamu:
# Od 1 po 26 ide o hraciu plochu od velkosti 5 do 30, s 1 cielovym polickom.
# Od 27 do 52 je cielovych policok 2 atd, az po 130, kde je cielovych policok 5 a velkost hracej plochy 30.

# zoznam, ktory som dostal si manualne priradim k novej premennej, s ktorou budem dalej pracovat vo vytvarani tabulky:
zoznam_hodnot = [5.937, 7.4, 7.053, 7.489, 7.833, 8.005, 8.114, 8.161, 8.484, 8.524, 9.232, 9.233, 9.525, 9.665, 9.85, 9.8, 10.521, 10.329, 11.007, 11.26, 11.311, 11.468, 12.114, 12.032, 12.287, 12.894, 2.842, 3.579, 4.144, 4.364, 4.5, 4.587, 4.939, 5.116, 5.314, 5.573, 5.965, 6.071, 6.459, 6.644, 6.898, 6.987, 7.421, 7.675, 7.809, 8.097, 8.335, 8.468, 8.749, 8.844, 9.11, 9.571, 2.058, 2.374, 2.798, 3.116, 3.416, 3.54, 3.743, 3.922, 4.256, 4.438, 4.766, 4.858, 5.052, 5.429, 5.635, 5.992, 6.119, 6.423, 6.618, 6.995, 7.206, 7.45, 7.639, 7.868, 8.157, 8.374, 1.494, 1.812, 2.117, 2.411, 2.79, 2.9, 3.174, 3.284, 3.611, 3.752, 3.988, 4.313, 4.579, 4.764, 5.068, 5.309, 5.588, 5.794, 5.984, 6.372, 6.464, 6.778, 6.946, 7.318, 7.535, 7.814, 1.207, 1.426, 1.701, 1.931, 2.18, 2.584, 2.746, 2.862, 3.125, 3.383, 3.553, 3.927, 4.171, 4.382, 4.686, 4.759, 4.99, 5.339, 5.588, 5.846, 6.084, 6.229, 6.576, 6.765, 7.046, 7.257]
print len(zoznam_hodnot) # 130
# Z tohto zoznamu urobim tabulku nasledujucim sposobom:
for h in range(len(zoznam_hodnot)/5): # vytvori 26 cyklov - pre kazdy riadok jeden
    for i in range(0, 130, len(zoznam_hodnot)/5): # vytvori 5 stlpcov, bude preskakovat po 26
        print zoznam_hodnot[h+i], # ciarkou to pisem do riadku
    print # urobi zariadkovanie ked skonci i cyklus
    
# Takto vyzera tabulka:
#5.937 2.842 2.058 1.494 1.207
#7.4 3.579 2.374 1.812 1.426
#7.053 4.144 2.798 2.117 1.701
#7.489 4.364 3.116 2.411 1.931
#7.833 4.5 3.416 2.79 2.18
#8.005 4.587 3.54 2.9 2.584
#8.114 4.939 3.743 3.174 2.746
#8.161 5.116 3.922 3.284 2.862
#8.484 5.314 4.256 3.611 3.125
#8.524 5.573 4.438 3.752 3.383
#9.232 5.965 4.766 3.988 3.553
#9.233 6.071 4.858 4.313 3.927
#9.525 6.459 5.052 4.579 4.171
#9.665 6.644 5.429 4.764 4.382
#9.85 6.898 5.635 5.068 4.686
#9.8 6.987 5.992 5.309 4.759
#10.521 7.421 6.119 5.588 4.99
#10.329 7.675 6.423 5.794 5.339
#11.007 7.809 6.618 5.984 5.588
#11.26 8.097 6.995 6.372 5.846
#11.311 8.335 7.206 6.464 6.084
#11.468 8.468 7.45 6.778 6.229
#12.114 8.749 7.639 6.946 6.576
#12.032 8.844 7.868 7.318 6.765
#12.287 9.11 8.157 7.535 7.046
#12.894 9.571 8.374 7.814 7.257

