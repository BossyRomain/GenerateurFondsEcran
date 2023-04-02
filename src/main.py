from src.parametres import lire_parametres
from src.erreurs import afficherErreurEtQuitter
from src.images import recuperer_pochettes


def main():
    try:
        dossier_pochettes, dossier_sauvegarde, nom, format, \
            taille_cases, definition_cible, tailles_pochettes, poids_pochettes = lire_parametres()
    except Exception as e:
        afficherErreurEtQuitter(e, 1)

    recuperer_pochettes(dossier_pochettes, poids_pochettes)


if __name__ == "__main__":
    main()
