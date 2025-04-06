import string
import time

def recursive_choixcaracteres(liste, mdp, nbrepetitions, fichier):
    
    if len(mdp) == nbrepetitions:
        print(mdp)
        fichier.write(mdp + "\n")  
    else:
        for char in liste:
            recursive_choixcaracteres(liste, mdp + char, nbrepetitions, fichier)

dateDebut = time.time()
liste_caracteres = string.ascii_lowercase 
mdp_de_depart = ""  
nbre_rep = 3  

with open('brutforce.txt', 'a') as fichier:  
    fichier.write(f"Nombre de répétitions: {nbre_rep}\n")  
    recursive_choixcaracteres(liste_caracteres, mdp_de_depart, nbre_rep, fichier)


dateFin = time.time()
print(f"Temps d'exécution: {dateFin - dateDebut} secondes")
