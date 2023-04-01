from src.parametres import lire_parametres
from src.erreurs import afficherErreurEtQuitter


def main():
    try:
        dossier_pochettes, dossier_sauvegarde, nom, format, \
            taille_cases, definition_cible, tailles_pochettes, poids_pochettes = lire_parametres()
    except Exception as e:
        afficherErreurEtQuitter(e, 1)


if __name__ == "__main__":
    main()
