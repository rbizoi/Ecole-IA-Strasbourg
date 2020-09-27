#!/bin/bash

for annee in `seq 1996 2020`
do
    for mois in `seq 1 12`
    do
        fichier=`printf "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.%d%02d.csv.gz" $annee $mois`
        wget $fichier
        gunzip -d $fichier
    done
done
