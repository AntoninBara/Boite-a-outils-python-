import zipfile

zip_path = "danger2.zip"
wordlist_path = "10-million-password-list-top-10000.txt"

def bruteforce_zip(zip_file, wordlist):
    try:
        with zipfile.ZipFile(zip_file) as zf:
            with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    password = line.strip()
                    try:
                        zf.extractall(pwd=password.encode('utf-8'))
                        print(f"\n✅ Mot de passe trouvé : {password}")
                        return
                    except RuntimeError as e:
                        if 'password required' in str(e).lower() or 'bad password' in str(e).lower():
                            print(f"Échec : {password}")
                        else:
                            print(f"Erreur : {password} → {e}")
                    except Exception as e:
                        print(f"Erreur inattendue avec {password} : {e}")
        print("\nAucun mot de passe correct trouvé.")
    except FileNotFoundError:
        print("Fichier ZIP ou wordlist introuvable.")
    except Exception as e:
        print(f"Erreur lors de l'ouverture du fichier : {e}")

if __name__ == "__main__":
    bruteforce_zip(zip_path, wordlist_path)
