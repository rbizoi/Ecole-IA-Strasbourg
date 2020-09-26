# -*- coding:utf8 -*-
# 23/09/2020 -- Atelier 01

# Comptage des occurrences d'un caractère donné dans une chaîne
ch = input('Une chaîne de caractères :')
car = input('Un caractère :')
  
i, nc = 0, 0 # initialisations
while i < len(ch):
    if ch[i] == car:
        nc = nc + 1 # caractère est trouvé -> on incrémente le compteur
    i = i + 1

if nc > 0 :
   print('le caractère est trouvé ',nc)
else :
   print("le caractère n'est pas trouvé ") 