# -*- coding:utf8 -*-
# 25/09/2020 -- Atelier 03

def nomMois(n):
    "renvoie le nom du n-ième mois de l'année"
    mois = ['Janvier,', 'Février', 'Mars', 'Avril', 'Mai', 
            'Juin', 'Juillet', 'Août', 'Septembre', 
            'Octobre', 'Novembre', 'Décembre']
    return mois[n -1] # les indices sont numérotés à partir de zéro

# test :
print(nomMois(4))

#----------------------------------------------------------------------------

mois = {1:'Janvier,',2:'Février',3:'Mars', 
        4:'Avril', 5:'Mai',6:'Juin', 7:'Juillet', 
        8:'Août', 9:'Septembre', 10:'Octobre', 
        11:'Novembre', 12:'Décembre'}

def nomMois(n):
    "renvoie le nom du n-ième mois de l'année"
    m = mois.get(n,"Il n'y a pas de mois {0} !".format(n))
    return m # les indices sont numérotés à partir de zéro
    
# test :
print('%s    --    %s'%(nomMois(4),nomMois(14)))
    