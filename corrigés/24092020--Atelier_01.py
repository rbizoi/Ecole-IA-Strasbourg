# -*- coding:utf8 -*-
# 24/09/2020 -- Atelier 01

n = 1 # numéro de la case
g = 1 # nombre de grains à y déposer
while n < 65 :
    print('%d %32E'%(n, g))
    n, g = n+1, g*2
 