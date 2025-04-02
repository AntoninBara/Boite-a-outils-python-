import random
mot_de_passe = ""
alphabet = "AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn!@#$%^&*()_+-=[]{}|;:,.<>?/"
for i in range(12):
    nombre_ale = random.randint(0, len(alphabet) - 1)  
    mot_de_passe += alphabet[nombre_ale]  
print(mot_de_passe) 
