# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:40:05 2020

@author: Laurier
"""

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import sys
import unicodedata

nom_fichier = input("Entrer le nom que vous desirez donner au fichier: ") #nom attribué au fichier

try:
    nb_liste = int((input("Le nombre de variable à entrer dans le fichier: "))) #nombre de variable qui vont être ecrite
except ValueError:
    print("Il y a une erreur, veuillez entrez un nombre entier")
    nb_liste = int(input("Veuillez entrer le nombre de variable dans le fichier: "))

try:
    nb_donnee = int(input("Le nombre de donnees à entrer:"))
except ValueError:
    print("Il y a une erreur, veuillez entrez un nombre entier")
    nb_donnee = int(input("EVeuillez entrer le nombre de donnees:"))
 
liste = [[] for i in range(nb_liste)]    
nom = []
i=0
while i < nb_liste:
    nom1 = input("Entrer le nom de la " + str(i+1) + "ième variable :")
    nom.append(nom1)
    i+=1

fd=open(nom_fichier +'.txt', "w")
for name in nom:
    fd.write(str(name)+", " )
fd.write("\n")

k=0
while k < nb_liste:
    j=0
    while j < nb_donnee:
        donnee = (input("Entrer la " + str(j+1) +"ieme valeur de la variable " + str(nom[k]) + ": "))
        liste[k].append(donnee)
        j+=1
    k+=1
print(liste)
for m in range (int(nb_donnee)):
    for n in range (int(nb_liste)):
        fd.write(str(liste[n][m]) + ", " )
    fd.write("\n")

fd.close()
print("Votre fichier est enregistre sous le nom <<" + nom_fichier + ">>  dans le même répertoir qu'où le code se situe")
