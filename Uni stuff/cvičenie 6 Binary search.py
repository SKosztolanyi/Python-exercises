import random

# Binary search - human vs computer
def hum_vs_comp(number):
    comp_number = random.randint(1, number)
    zadej_cislo = input("Vyberte si cislo od 1 do n: ")
    while int(zadej_cislo) != comp_number:
        if int(zadej_cislo) < comp_number:
            print "Spatny tip. Moje cislo je vetsi. Zkus znova."
            zadej_cislo = input("Vyberte si cislo od 1 do n: ")
        if int(zadej_cislo) > comp_number:
            print "Spatny tip. Moje cislo je mensi. Zkus znova."
            zadej_cislo = input("Vyberte si cislo od 1 do n: ")
        if int(zadej_cislo) == comp_number:
            print "Uhodl jsi, moje cislo bylo", zadej_cislo

def comp_vs_hum(n):
    zadej_cislo = input("Myslete si cislo od 1 do n (a pro jistotu si ho sem i napiste): ")
    moje_cislo = int(zadej_cislo)
    spodek = 1
    vrch = n
    pocet_pokusu = 0
    pocitac_hleda = (vrch+spodek)/2
    while moje_cislo != pocitac_hleda:
        print pocitac_hleda
        if pocitac_hleda < moje_cislo:
            print "Spatny tip. Moje cislo je vetsi. Zkus znova."
            spodek = (vrch+spodek)/2
            pocitac_hleda = (vrch+spodek)/2
            pocet_pokusu += 1
        elif pocitac_hleda > moje_cislo:
            print "Spatny tip. Moje cislo je mensi. Zkus znova."
            vrch = (vrch + spodek)/2
            pocitac_hleda = (vrch + spodek)/2
            pocet_pokusu += 1
        if moje_cislo == pocitac_hleda:
            print pocitac_hleda
            pocet_pokusu += 1
            print "Good job computer, you did it again! Pocet tvych pokusu byl:", pocet_pokusu
            

def comp_vs_comp(n):
    # Comp1 chooses a number randomly from range n and Comp2 wants to find it in the least possible amount of tries.
    comp1 = random.randint(1, 10)
    print comp1
    spodek = 1
    vrch = n
    tries = 0
    comp2 = (vrch+spodek) / 2
    while comp1 != comp2:
        print "Comp2 looks for comp1 number and chooses number: ", comp2
        if comp1 > comp2:
            print "Not now Comp2. My randomly chosen number is bigger. Try it again."
            spodek = (vrch + spodek) / 2 + 1
            comp2 = (vrch + spodek) / 2  # Lepsi odhad, spodni hranici zvysit o 1.
            # Kdyz hadam 5 tak vim, ze to 5 nebude, takze posunu spodni hranici vys o 1
            tries += 1
        elif comp1 < comp2:
            print "Not now Comp2. My randomly chosen number is smaller. Try it again."
            vrch = (vrch + spodek) / 2 
            comp2 = (vrch + spodek) / 2 
            tries += 1
        if comp1 == comp2:
            print "Comp2 looks for comp1 number and chooses number: ", comp2
            tries += 1
            print "Darn you comp2, this time you win! Your number of tries was:", tries
            
            # funguje to pre randrange, ale nefunguje pre randint ak si zvoli najvyssie mozne cislo
            # niekde musim pridat +1, aby sa spodok - 
            # Riesenie: do spodek +1, kvoli deleniu so zvyskom
                         
        

    
 