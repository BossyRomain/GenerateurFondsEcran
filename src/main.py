from src.parametres import lire_parametres
from src.erreurs import afficherErreurEtQuitter
from src.images import recuperer_pochettes
from src.grille import Grille
import cv2


def main():
    try:
        dossier_pochettes, dossier_sauvegarde, nom, format, \
            taille_cases, definition_cible, tailles_pochettes, poids_pochettes = lire_parametres()
    except Exception as e:
        afficherErreurEtQuitter(e, 1)

    images = recuperer_pochettes(dossier_pochettes, poids_pochettes)

    key = -5
    while key != ord('s'):
        grille = Grille(definition_cible, taille_cases, tailles_pochettes)
        i = 0
        while len(grille.cases_libres) > 0:
            coords, taille = grille.trouver_carre_libre()

            grille.ajouter_image(images[i % len(images)], coords, taille)
            i += 1

        image_resultat = grille.obtenir_image_resultat()
        cv2.imshow("resultat", image_resultat)
        key = cv2.waitKey(0)
        del grille

    cv2.imwrite(f"{dossier_sauvegarde}{nom}.{format}", image_resultat)


if __name__ == "__main__":
    main()
