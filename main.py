import cv2
import copy
import subprocess

from src.parametres import lire_parametres
from src.images import recuperer_pochettes
from src.erreurs import afficherErreurEtQuitter
from src.grille import Grille


def get_screend_dimension():
    cmd = ['xrandr']
    cmd2 = ['grep', '*']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)
    p.stdout.close()

    resolution_string, junk = p2.communicate()
    resolution = resolution_string.split()[0]
    return resolution.split('x')


def main():
    try:
        dossier_pochettes, dossier_sauvegarde, nom, format, taille_cases, definition_cible, tailles_pochettes, poids_pochettes = lire_parametres()
    except Exception as e:
        afficherErreurEtQuitter(str(e), 1)

    pochettes = recuperer_pochettes(dossier_pochettes, poids_pochettes)

    # screen_width, screen_height = get_screend_dimension()
    cv2.namedWindow("Resultat", cv2.WINDOW_NORMAL)

    toucheAppyuee = 1
    while toucheAppyuee != ord('s'):
        grille = Grille(definition_cible, taille_cases, copy.deepcopy(tailles_pochettes))
        indice_image = 0

        while len(grille.cases_libres) > 0:
            coords, taille = grille.get_carrer_cases_libres()
            grille.ajouter_image(pochettes[indice_image % len(pochettes)], coords, taille)
            indice_image += 1

        image_resultat = grille.get_image_resultat()

        cv2.imshow("Resultat", image_resultat)
        toucheAppyuee = cv2.waitKey(0)
        del grille

    cv2.destroyAllWindows()
    cv2.imwrite(f"{dossier_sauvegarde}{nom}.{format}", image_resultat)
        

if __name__ == "__main__":
    main()