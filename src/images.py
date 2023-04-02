import os
import random

import cv2
from src.erreurs import afficherErreurEtQuitter


# Classe représentant les pochettes
class Pochette:
    def __init__(self, nom, poids, pixels):
        self.nom = nom
        self.poids = poids
        self.pixels = pixels

    def __lt__(self, other):
        return self.poids >= other.poids

    def __str__(self):
        return f"({self.nom} {self.poids})"


# Lit les pochettes contenues dans le dossier des pochettes
# Paramètres :
# - dossier_pochettes : le dossier contenant les pochettes, un dossier existant, accessible avec les droits de lecture
# - poids_pochettes : un dictionnaire {nom_pochette, poids} des pochettes avec un poids supérieur à 1
# Retourne une liste des images triées par poids
def recuperer_pochettes(dossier_pochettes, poids_pochettes):
    pochettes = []
    nom_fichiers = os.listdir(dossier_pochettes)
    for nom_fichier in nom_fichiers:
        try:
            fichier = open(dossier_pochettes + nom_fichier, "r")

            nom, extension = nom_fichier.split(".")
            poids = poids_pochettes[nom] if nom in poids_pochettes else 1
            pixels = cv2.imread(dossier_pochettes + nom_fichier)

            pochettes.append(Pochette(nom, poids, pixels))
        except PermissionError:
            pass
    if len(pochettes) == 0:
        afficherErreurEtQuitter(f"Aucunes images n'a été lues dans le dossier {dossier_pochettes}", 2)

    random.shuffle(pochettes)
    pochettes.sort()
    return pochettes
