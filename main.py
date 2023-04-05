from src.parametres import lire_parametres
from src.images import recuperer_pochettes
from src.erreurs import afficherErreurEtQuitter
from src.grille import Grille


def main():
    try:
        dossier_pochettes, dossier_sauvegarde, nom, format, taille_cases, definition_cible, tailles_pochettes, poids_pochettes = lire_parametres()
    except Exception as e:
        afficherErreurEtQuitter(str(e), 1)

    pochettes = recuperer_pochettes(dossier_pochettes, poids_pochettes)

    grille = Grille(definition_cible, taille_cases, tailles_pochettes)
    
    coords, taille = grille.get_carrer_cases_libres()

    grille.ajouter_image(pochettes[0], coords, taille)

if __name__ == "__main__":
    main()