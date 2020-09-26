# -*- coding:utf8 -*-
# 25/09/2020 -- Atelier 04

def inverse(ch):
    "renvoie la chaîne inversée"
    i, chInv  = len(ch),""
    while i > 0 :
        i = i - 1 # le dernier élément possède l'indice n -1
        chInv = chInv + ch[i]
    return chInv

# test :
chaine = 'abcdefghijklmnopqrstuvwxyz'
print(inverse(chaine))


