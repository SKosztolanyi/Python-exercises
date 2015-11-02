

def vigenere(text, klic):
    word = ""
    newLetter = ""
    remaining = len(text)
    while remaining > 0:
    for c in text.upper():
        for d in klic.upper():
            # potrebujem cyklicky prechadzat klic a postupne z neho vyberat podla indexu pismeno
            # ak je index vacsi ako dlzka slova, tak vydlim index dlzkou slova a tym pojdem od zaciatku
            if c == "" :
                word += ""
            elif ord(c)+ord(klic > ord("Z"):
                newLetter = chr(ord(c) + klic - 26)    
            newLetter = char(ord(c+
            
            
    # potrebujem
print vigenere('pampeliska', 'klic')
# ZLUROWQUUL
