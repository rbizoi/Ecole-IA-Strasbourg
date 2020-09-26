# -*- coding:utf8 -*-
# 24/09/2020 -- Atelier 02

n,ch =5,"abcdefghijklmnopqrstuvwxyz123456789âêîôûàèìòùáéíóú"
d, f = 0, n # indices de début et de fin de fragment
liste = [] # liste à construire
while d < len(ch):
    if f > len(ch): # on ne peut pas découper au-delà de la fin
        f = len(ch)
    fr = ch[d:f] # découpage d'un fragment
    liste.append(fr) # ajout du fragment à la liste
    d, f = f, f +n # indices suivants

chInv = "" # chaîne à construire
i = len(liste) # on commence par la fin de la liste
while i > 0 :
    i = i - 1 # le dernier élément possède l'indice n -1
    chInv = chInv + liste[i]
    
print("chaîne initiale :")
print(ch)
print("liste de fragments de 5 caractères :")
print(liste)
print("fragments rassemblés après inversion de la liste :")
print(chInv)