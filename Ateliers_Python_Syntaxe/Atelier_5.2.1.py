# -*- coding:utf8 -*-
# Atelier 5.2.1

nb = 20 
liste = []
while nb < 41 :
    liste.append((nb,nb**2,nb**3))
    nb = nb + 1

for i in liste : print(i)