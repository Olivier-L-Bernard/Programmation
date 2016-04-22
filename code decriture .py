#-utf-8


import numpy as np
from matplotlib import pyplot as plt
import sys

def ecriture ():
    nom_fichier = input("Entrer le nom que vous desirez donner au fichier : ") #nom attribué au fichier
    nb_liste = (input("Entrer le nombre de variable à entrer dans le fichier : ")) #nombre de variable qui vont être ecrite

    if not nb_liste.isdigit():
        print("Il y a une erreur, veuillez entrez un nombre entier")
        nb_liste = int(input("Entrer le nombre de variable à entrer dans le fichier: "))

      
    if int(nb_liste) <= 3 :
        nb_donnee = (input("Entrer le nombre de donnees à entrer :"))

        if not nb_donnee.isdigit():
            print("Il y a une erreur, veuillez entrez un nombre")
            nb_donnee = int(input("Entrer le nombre de donnees à entrer :"))
        
        #Nom des variables
        nom1 = input("Entrer le nom de la première variable :")
        nom2 = input("Entrer le nom de la seconde variable :")

        if int(nb_liste) == 3:
            nom3 = input("Entrer le nom de la troisième variable :")
        
        liste1 = []
        liste2 = []
        liste3 = []
       
        #ecriture des noms dans le fichier
        fd=open(nom_fichier , "w")
        fd.write(str(nom1) + "         ")
        fd.write(str(nom2) + "         ")

        if int(nb_liste)>2 and int(nb_liste) == 3:
            fd.write(str(nom3) + "         ")

           
                
        fd.write("\n")
 
        nb = 0
        nb2 = 0
        nb3 = 0
        
        #Entrees des données ainsi que leur écriture dans le fichier
        while nb < int(nb_donnee):
            donnee1 = (input("Entrer la prochaine valeur de la variable" +" "+ nom1 + ": "))
            if not donnee1.isdigit():
                print("Il y a une erreur, veuillez entrez un nombre")
                donnee1 = (input("Entrer la prochaine valeur de la variable" +" "+ nom1 + ": "))
            liste1.append(float(donnee1))
            nb+=1
        
        while nb2 < int(nb_donnee):
            donnee2 = (input("Entrer la prochaine valeur de la variable" +" " + nom2 + ": "))
            if not donnee2.isdigit():
                print("Il y a une erreur, veuillez entrez un nombre")
                donnee2 = (input("Entrer la prochaine valeur de la variable" +" "+ nom2 + ": "))  
            liste2.append(float(donnee2))
            nb2+=1
        
        #Nous avons un minimum de 2 variables. Donc pour 2 ou 3 variables le programme reste tres conviviale
        if int(nb_liste)>2 and int(nb_liste) == 3:
            while nb3 < int(nb_donnee):
                donnee3 = (input("Entrer la prochaine valeur de la variable" + " " + nom3 + ": "))
                if not donnee3.isdigit():
                    print("Il y a une erreur, veuillez entrez un nombre")
                    donnee3 = (input("Entrer la prochaine valeur de la variable" +" "+ nom3 + ": "))  
                liste3.append(float(donnee3))
                nb3+=1
        
        #ecriture des données dans le fichiers
        if int(nb_liste) == 3:
            for i in range (int(nb_donnee)):
                fd.write(str(liste1[i]) + "         " + str(liste2[i]) +  "         " + str(liste3[i]) +  "\n")

        if int(nb_liste) == 2:
            for i in range (int(nb_donnee)):
                fd.write(str(liste1[i]) + "         " + str(liste2[i])+ "\n")

        print(nom1, liste1)
        print(nom2, liste2)
        if int(nb_liste) == 3:
            print(nom3, liste3)
            
                
        fd.close()
        print ("Votre est enregistre sous le nom <<" + nom_fichier + ">>  dans le même répertoir qu'où le code se situe")


    #Écriture du fichier avec plus de 3 variables différentes
    if int(nb_liste) > 3 :
        #nombre de données à entrer par variable
        nb_donnee_n = (input("Entrer le nombre de données à entrer :")) #nobre de données pour chaque variable
        if not nb_donnee_n.isdigit():
            print("Il y a une erreur, veuillez entrez un nombre")
            nb_donnee_n = (input("Entrer le nombre de données à entrer :"))

        nb_titre = 0
        nb_3 = 0
        liste_nom = []
        
        fd=open(nom_fichier , "w")
    
        while nb_titre < int(nb_liste):
            nom_n = input("Entrer le nom de la nième variable :")
            liste_nom.append(nom_n) #Mise en mémoire des noms des variables
            nb_titre += 1
        #Écriture des noms des variables dans le fichier        
        for i in range (int(nb_liste)):
            fd.write(str(liste_nom[i]) + "         ")

        fd.write("\n")  

        while nb_3 < int(nb_donnee_n):
 
            nb_4=0
            i=0
        
            while nb_4 < int(nb_liste):
                donnee_n = (input("Entrer la prochaine valeur de la variable" + " " + liste_nom[i] + ": "))
                if not donnee_n.isdigit():
                    print("Il y a une erreur, veuillez entrez un nombre")
                    donnee_n = (input("Entrer la prochaine valeur de la variable" + " " + liste_nom[i] + ": "))
        
                fd.write(str(float(donnee_n)) + "         ")
                i +=1
                nb_4 +=1
            
            fd.write("\n" )
            nb_3 += 1

    fd.close()
    print ("Le document" +" " + nom_fichier + " est enregistre sous le nom <<" + nom_fichier + ">>  dans le même répertoir qu'où le code se situe")

    main() #retour au main

#Lecture d'une fichier
def lecture():
    nom_doc = input("Entrez le nom complet (avec l'extension) du ficihier que vous voulez lire :")

    gd = open(nom_doc, 'r')
    print(gd.read())
    gd.close()
    
    graph = input("Voulez vous en faire une graphique (O: Oui, N: Non) :")
    
    if graph == 'O' or graph == 'o':
        
        saut= input("Combien de ligne désirez vous sauter (combien de ligne ne sont pas des données) :")
        var =np.loadtxt(nom_doc,skiprows= int(saut) ,unpack=True)
        
        x = (input("Entrez le numéros de la colonne qui sera la composante X du graphique :"))
        if not x.isdigit():
            print("Il y a une erreur, veuillez entrez un nombre")
            x = (input("Entrez le numéros de la colonne qui sera la composante X du graphique :"))
        
        y = (input("Entrez le numéros de la colonne qui sera la composante Y du graphique :"))
        if not y.isdigit():
            print("Il y a une erreur, veuillez entrez un nombre")
            y = (input("Entrez le numéros de la colonne qui sera la composante Y du graphique :"))
            
        
        
        plt.plot(var[int(x)-1], var[int(y)-1])
        plt.xlabel('some numbers')
        plt.ylabel('some numbers')
        plt.show()

    if graph == 'N' or graph == 'n':
        main()
        
    main() # retour au main
    

#main, choix entre les différentes options
def main():
    commande= input("Que voulez-vous faire (E: Ecrire un fichier, L: Lire un fichier, S: arret du programme): ")

    if (commande == 'E' or commande == 'e' ) :
        ecriture()

    if (commande == 'L' or commande == 'l' ):
        lecture()

    if (commande == 'S' or commande == 's'):
        sys.exit()
       

    if not commande == 'E' and commande == 'e' and commande == 'L' and commande == 'l':
        print("Veuillez choisir une des deux options de ce programme s'il-vous-plaît")
        commande= input("Que voulez-vous faire ? (E: Ecrire un fichier, L: Lire un fichier) :")
        

if __name__ == '__main__':
  main()   
