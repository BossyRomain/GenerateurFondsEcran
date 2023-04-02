from src.parametres import lire_parametres
from src.erreurs import afficherErreurEtQuitter
from src.images import recuperer_pochettes
from src.grille import Grille


def main():
    try:
        dossier_pochettes, dossier_sauvegarde, nom, format, \
            taille_cases, definition_cible, tailles_pochettes, poids_pochettes = lire_parametres()
    except Exception as e:
        afficherErreurEtQuitter(e, 1)

    images = recuperer_pochettes(dossier_pochettes, poids_pochettes)

    grille = Grille(definition_cible, taille_cases, tailles_pochettes)

    coords, taille = grille.trouver_carre_libre()

    grille.ajouter_image(images[0], coords, taille)


if __name__ == "__main__":
    main()
