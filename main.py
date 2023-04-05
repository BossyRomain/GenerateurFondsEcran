from src.parametres import lire_parametres
from src.erreurs import afficherErreurEtQuitter


def main():
    try:
        dossier_pochettes = lire_parametres()
    except Exception as e:
        afficherErreurEtQuitter(str(e), 1)


if __name__ == "__main__":
    main()