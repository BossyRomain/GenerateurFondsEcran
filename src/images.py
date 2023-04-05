import os
import cv2
import random
from src.erreurs import afficherErreurEtQuitter, afficherAvertissement, ImageInvalide
from src.parametres import FORMATS_VALIDES

# La classe représentant une image
class Image:
    def __init__(self, nom, poids, pixels):
        self.nom = nom
        self.poids = poids
        self.pixels = pixels

    
    def __lt__(self, other):
        return self.poids > other.poids


# Récupère les pochettes d'albums depuis le dossier des pochettes d'albums
def recuperer_pochettes(dossier_pochettes, poids_pochettes):
    nom_fichiers = os.listdir(dossier_pochettes)
    pochettes = []

    print(f"Récupération des pochettes dans le dossier {dossier_pochettes}")
    for nom_fichier in nom_fichiers:
        try:
            nom, extension = nom_fichier.split(".")
            if extension not in FORMATS_VALIDES or os.access(nom_fichier, os.R_OK):
                raise ImageInvalide(nom_fichier)

            img = cv2.imread(dossier_pochettes + nom_fichier)
            pochettes.append(Image(nom, poids_pochettes[nom] if nom in poids_pochettes else 1, img))
        except ImageInvalide as e:
            afficherAvertissement(str(e))
        except Exception:
            pass

    if len(pochettes) == 0:
        afficherErreurEtQuitter(f"Aucunes images n'a été trouvée dans le dossier {dossier_pochettes}" ,2)

    random.shuffle(pochettes)
    pochettes.sort()
    return pochettes