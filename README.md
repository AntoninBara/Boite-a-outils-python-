# Boite-a-outils-python-
Bienvenue dans ma boîte à outils Python

Tu y trouveras 3 code prêts à l’emploi pour :
- Forcer un ZIP avec une attaque par dictionnaire
- Générer un mot de passe complexe
- Générer toutes les combinaisons possibles pour une attaque brute force
  
Prérequis :
- Avoir Python installé sur ton système.

Attaque par dictionnaire : 

Objectif :
Essayer tous les mots de passe d’un fichier texte (wordlist) sur un fichier ZIP protégé.

Fichiers nécessaires :
- Le fichier .zip que tu veux déverrouiller ex: danger2.zip
- Pour ca crée un dossier installe winrar clique droit sur le fichier winrar → ajouter a l'archive
- Attention bien cocher le zip et le chiffrement zip image (https://github.com/user-attachments/assets/dbfc150e-5ed1-4a72-9ea9-26fb4ec2e6bb)
- Une wordlist → ex: 10-million-password-list-top-10000.txt trouver sur : https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt
- puis lance le code panse a modifier le nom.zip et la wordlist si tu les change

Générateur de mots de passe :

Objectif : 
Créer un mot de passe fort de 12 caractères de manière aléatoire.

Comment utiliser :
- Lance simplement le code

Générateur de combinaisons (Brute Force) :

Objectif :
Générer toutes les combinaisons possibles de lettres minuscules (a-z) pour un mot de passe de longueur donnée.

Comment utiliser :
- Dans le script, change si besoin : nbre_rep = 3 (Nombre de lettres dans chaque combinaison)

Tu obtiendras :
- Un fichier brutforce.txt avec toutes les combinaisons générées
- Le temps total d’exécution

Ces outils sont uniquement faits pour l’apprentissage, les tests de sécurité sur tes propres fichiers ou avec autorisation explicite.
