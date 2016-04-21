nb_liste = int(input("Entrer le nombre de variable à entrer dans le fichier (2 maximum) :"))
essaie = 0
if nb_liste > 3 :
    while essaie <= 5 :
        print("Il y a trop de variable pour ce document")
        nb_liste = int(input("Entrer le nombre de variable à entrer dans le fichier :"))
        essaie += 1
        if nb_liste <=2:
            break
    
    
if nb_liste <= 2 :
    nb_donnee = int(input("Entrer le nombre de données à entrer :"))
    nom1 = input("Entrer le nom de la première liste de donnée :")
    nom2 = input("Entrer le nom de la seconde liste de donnée :")
    liste1 = []
    liste2 = []
    fd=open("donnee.txt" , "w")
    fd.write(str(nom1) + "         ")
    fd.write(str(nom2) + "\n")

   
    nb = 0
    nb2=0
        
    while nb < nb_donnee:
        donnee1 = float(input("Entrer la prochaine valeur de la donnee de la première liste: "))
        liste1.append(donnee1)
        nb+=1
    while nb2 < nb_donnee:
        donnee2 = float(input("Entrer la valeur de la donnee de la seconde liste : "))
        liste2.append(donnee2)
        nb2+=1
    for i in range (nb_donnee):
        fd.write(str(liste1[i]) + "         " + str(liste2[i]) + "\n")
            
        


        
print(nom1, liste1)
print(nom2, liste2)
fd.close()
print ("La liste de données est enregistre sous le nom donnee [sans extension] dans le même répertoir qu'où le code se situe")
