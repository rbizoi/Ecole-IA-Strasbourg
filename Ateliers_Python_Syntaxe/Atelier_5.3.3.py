# -*- coding:utf-8 -*-
# Atelier 5.3.3

def list_aleat(n):
    s = [0]*n
    for i in range(n):
        s[i] =random()
    return s

#Test :
list_aleat(10)