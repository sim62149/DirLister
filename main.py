import os

def afficher_arborescence(repertoire, niveau=0):
    # Parcourt tous les fichiers et dossiers dans le répertoire
    for element in os.listdir(repertoire):
        chemin_complet = os.path.join(repertoire, element)
        # Ajoute des indentations pour afficher l'arborescence
        indentation = "│   " * (niveau - 1) + "├── " if niveau > 0 else ""
        print(indentation + element)
        # Si c'est un dossier, lister son contenu récursivement
        if os.path.isdir(chemin_complet):
            afficher_arborescence(chemin_complet, niveau + 1)

# Chemin du répertoire à explorer
repertoire_cible = input("Entrez le chemin du dossier à explorer : ").strip()

if os.path.exists(repertoire_cible) and os.path.isdir(repertoire_cible):
    print(os.path.basename(repertoire_cible))
    afficher_arborescence(repertoire_cible)
else:
    print(f"Erreur : '{repertoire_cible}' n'est pas un répertoire valide.")
