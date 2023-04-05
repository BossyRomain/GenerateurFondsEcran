import os

from src.erreurs import ParametreManquant, ParametreInvalide, afficherAvertissement
from src.erreurs import INVALIDE_DOSSIER, INVALIDE_NOM, INVALIDE_FORMAT, INVALIDE_TAILLE_CASES, INVALIDE_DEFINITION_CIBLE, INVALIDE_TAILLE_POCHETTE, INVALIDE_POIDS_POCHETTE

# Ensemble des formats valides pour l'image résultat
FORMATS_VALIDES = ("jpeg", "png", "bpm", "dib", "jpe", "jpg", "jp2", "pbm", "pgm", "ppm", "sr", "ras", "tiff", "tif")

# Lis les paramètres sur l'entrée standard
# Lève une erreur dès que l'un d'entre eux est manquant ou invalide
def lire_parametres():
    try:
        # Dossier des pochettes
        dossier_pochettes = __lire_chemin_dossier("Entrer le chemin du dossier des pochettes d'albums :\n", 
                                                  "dossier des pochettes", 
                                                  INVALIDE_DOSSIER)
    
        # Dossier de sauvegarde
        dossier_sauvegarde = __lire_chemin_dossier("Entrer le chemin du dossier où sera sauvegardée l'image résultat :\n", 
                                                   "dossier de sauvegarde", 
                                                   INVALIDE_DOSSIER)
    
        # Nom de l'image résultat
        nom = __lire_ligne("Entrer le nom de l'image résultat :\n", "nom de l'image résultat")

        if not nom.isascii():
            raise ParametreInvalide(INVALIDE_NOM)
        
        # Format de l'image résultat
        format = __lire_ligne("Entrer le format de l'image résultat :\n", "format de l'image résultat")

        if format not in FORMATS_VALIDES:
            raise ParametreInvalide(f"{INVALIDE_FORMAT}{FORMATS_VALIDES}")
        
        # Taille des cases sur la grille
        taille_cases = __lire_valeur("Entrer la taille des cases (en nombre de pixels) de la grille :\n", "taille des cases", INVALIDE_TAILLE_CASES, int)

        if taille_cases <= 0:
            raise ParametreInvalide(INVALIDE_TAILLE_CASES)

        # Définition cible de l'image résultat
        definition_cible = __lire_n_valeurs("Entrer la définition cible de l'image résultat (largeur, hauteur) :\n", "définition cible", INVALIDE_DEFINITION_CIBLE, (int, int))

        if definition_cible[0] <= 0 or definition_cible[1] <= 0 or definition_cible[0] % taille_cases > 0 or definition_cible[1] % taille_cases > 0:
            raise ParametreInvalide(INVALIDE_DEFINITION_CIBLE)

        # Section taille des pochettes
        tailles_pochettes = []
        stop = False
        print("Entrer la section des tailles de pochettes (ligne vide pour terminer) :")
        while not stop:
            try:
                taille = __lire_n_valeurs("", "", "", (int, int))

                if taille[0] > 1 and taille[1] > 0:
                    tailles_pochettes.append(taille)
            except ParametreInvalide:
                afficherAvertissement(INVALIDE_TAILLE_POCHETTE)
            except Exception:
                stop = True

        # Section poids des pochettes
        poids_pochettes = []
        print("Entrer la section des poids des pochettes (ligne vide pour terminer) :")
        stop = False
        while not stop:
            try:
                poids = __lire_n_valeurs("", "", "", (str, int))
                if poids[1] > 1:
                    poids_pochettes.append(poids)
            except ParametreInvalide:
                afficherAvertissement(INVALIDE_POIDS_POCHETTE)
            except Exception:
                stop = True
        poids_pochettes = dict(poids_pochettes)
    except Exception as e:
        raise e
        

    return dossier_pochettes, dossier_sauvegarde, nom, format, taille_cases, definition_cible, tailles_pochettes, poids_pochettes


# Lit une ligne sur l'entrée standard
# Lève une erreur si EOF ou ligne vide
# Paramètres :
# - message : le message affiché sur l'entrée standard
# - erreur : le message d'erreur
# Retourne la ligne lue sur l'entrée standard
def __lire_ligne(message, erreur):
    try:
        ligne = input(f"{message}")
    except EOFError:
        raise ParametreManquant(erreur)
    if ligne == "":
        raise ParametreManquant(erreur)

    return ligne


# Lit le chemin d'un dossier sur l'entrée standard
# Lève une erreur s'il est manquant ou invalide
# Paramètres :
# - message : le message à afficher dans input
# - manquant : le message d'erreur si manquant
# - invalide : le message d'erreur si invalide 
# Retourne : le chemin du dossier lu
def __lire_chemin_dossier(message, manquant, invalide):
    try:
        dossier = __lire_ligne(message, manquant)
    except Exception as e:
        raise e

    if not os.path.isdir(dossier) or not os.access(dossier, os.R_OK):
        raise ParametreInvalide(invalide)
    
    return dossier


# Lit une valeur de type type sur l'entrée standard
def __lire_valeur(message, manquant, invalide, type):
    try:
        valeur = type(__lire_ligne(message, manquant))
    except ValueError:
        raise ParametreInvalide(invalide)
    except Exception as e:
        raise e
    return valeur


# Lit N valeurs sur l'entrée standard chacune pouvant être de type différent
def __lire_n_valeurs(message, manquant, invalide, types):
    try:
        N = len(types)
        str_valeurs = __lire_ligne(message, manquant).strip().split(" ")
        if len(str_valeurs) != N:
            raise ParametreInvalide(invalide)
        valeurs = [types[i](str_valeurs[i]) for i in range(N)]
    except ValueError:
        raise  ParametreInvalide(invalide)
    except Exception as e:
        raise e
    return valeurs
