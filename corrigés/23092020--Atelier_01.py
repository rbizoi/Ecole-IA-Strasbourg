# -*- coding:utf8 -*-
# 23/09/2020 -- Atelier 02

# Rechercher l'indice d'un caractère donné dans une chaîne
ch = input('Une chaîne de caractères :')
car = input('Un caractère :')

i = 0
while i < len(ch):
    if ch[i] == car:
        print('le caractère est trouvé ',i)
        break
    i = i + 1
if i >= len(ch) :
   print("le caractère n'est pas trouvé ")
