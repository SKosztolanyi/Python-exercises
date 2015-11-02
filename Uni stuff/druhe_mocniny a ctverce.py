def je_druha_mocnina(n):
    odmocnina = int(n**0.5)
    return odmocnina**2 == n

def soucet_ctvercu(n):
    for i in range(int(n**0.5) + 1):
        zbytek = n - i**2
        if je_druha_mocnina(zbytek):
            return True
    return False

def vypis_souctu_ctvercu(kolik):
    for i in range(kolik):
        if soucet_ctvercu(i):
            print i,