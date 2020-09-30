# -*- coding:utf-8 -*-
# Atelier 5.2.4


def motMax(lst):
    "renvoie le plus grand mot de la liste"
    max = ""
    for mot in lst :
        if len(mot) > len(max) :
           max = mot
    return max

# Comptage du nombre de mots dans la chaîne ch
# ex. "Les petits ruisseaux font les grandes rivières"
ch = ""
while len(ch) <= 0 :
    ch = input('Une chaîne de caractères :')
    if len(ch) ==0:
        print("Elle est ou la phrase ?") 
        
liste = ch.split()

print('Le mot le plus long est :',motMax(liste))
