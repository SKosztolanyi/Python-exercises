def najdi_pismeno(sekvence):
    for i in range(len(morse)):
        if morse[i] ==        sekvence:
            return chr(ord("A")+i)
    return "?"

def prevod_z_morse(zprava):
    vystup = ""
    sekvence = ""
    for znak in zprava:
        print znak
        if znak == "|":
            vystup += najdi_pismeno(sekvence)
            sekvence = ""
        else:
            sekvence += znak
    
    return vystup 
    # Nie je nutne pisat kod linearne. Mozme ho pisat systematicky podla potreby 