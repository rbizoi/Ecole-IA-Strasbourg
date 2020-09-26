# -*- coding:utf8 -*-
# 24/09/2020 -- Atelier 03

# Comptage du nombre de mots dans la chaîne ch
#ch = input('Une chaîne de caractères :')
ch = "Les petits ruisseaux font les grandes rivières"

if len(ch) ==0:
    print("ou est la chaîne ?") 
nm = 1 # la chaîne comporte au moins un mot
for c in ch:
    if c == " ": # il suffit de compter les espaces
        nm = nm + 1

if nm >= 1 :
   print('le nombre des mots ',nm)
