# -*- coding:utf8 -*-
# 25/09/2020 -- Atelier 01

def compteCar(ca, ch):
    "Renvoie le nombre de caractères ca trouvés dans la chaîne ch"
    i, tot = 0, 0
    while i < len(ch):
        if ch[i] == ca:
            tot = tot + 1
        i = i + 1
    return tot

def compteCar(ca, ch):
    "Renvoie le nombre de caractères ca trouvés dans la chaîne ch"
    tot = 0, 0
    for i in ch :
        if i == ca: tot = tot + 1
    return tot

    
# test :
print(compteCar("e","Cette chaîne est un exemple"))