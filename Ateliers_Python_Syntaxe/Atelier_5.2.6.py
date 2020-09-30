# -*- coding:utf-8 -*-
# Atelier 5.2.6

def tri_bulle(liste):
    """L'algorithme du tri à bulles
    Le principe du tri à bulles est de comparer deux valeurs adjacentes 
    et d'inverser leur position si elles sont mal placées. 
    """
    permutation = True
    passage = 0
    while permutation == True:
        permutation = False
        passage = passage + 1
        for en_cours in range(0, len(liste) - passage):
            if liste[en_cours] > liste[en_cours + 1]:
                permutation = True
                # On echange les deux elements
                liste[en_cours], liste[en_cours + 1] = \
                liste[en_cours + 1],liste[en_cours]
    return liste  

lst = [9, 12, 40, 5, 12, 3, 27, 5, 9, 3, 8, 22, 40, 3, 2, 4, 6, 25]
tri_bulle(lst)
print(lst)
