from src.parametres import lire_parametres
from src.images import recuperer_pochettes
from src.erreurs import afficherErreurEtQuitter


def main():
    try:
        dossier_pochettes, dossier_sauvegarde, nom, format, taille_cases, definition_cible, tailles_pochettes, poids_pochettes = lire_parametres()
    except Exception as e:
        afficherErreurEtQuitter(str(e), 1)

    pochettes = recuperer_pochettes(dossier_pochettes, poids_pochettes)
    
    

if __name__ == "__main__":
    main()