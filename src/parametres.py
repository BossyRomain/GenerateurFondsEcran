import os.path

from src.erreurs import ParametreManquant, ParametreInvalide, \
    INVALIDE_DOSSIER_POCHETTES, INVALIDE_DOSSIER_SAUVEGARDE, INVALIDE_NOM, INVALIDE_FORMAT, INVALIDE_TAILLE_CASES, \
    INVALIDE_DEFINITION_CIBLE

VALID_FORMATS = ("bmp", "dib", "jpeg", "jpg," "jpe," "jp2", "png", "pbm", "pgm", "ppm", "sr", "ras", "tiff", "tif")


# Lit les paramètres du programme sur l'entrée standard
# Lève une exception dès qu'un paramètre est manquant ou invalide
# Retourne les paramètres du programme dans l'ordre suivant :
# 1 - dossier des pochettes
# 2 - dossier de sauvegarde
# 3 - nom de l'image résultat
# 4 - format de l'image résultat
# 5 - taille des cases sur la grille
# 6 - définition ciblée de l'image résultat
# 7 - les tailles des pochettes
# 8 - les poids des pochettes
def lire_parametres():
    # Dossier des pochettes
    try:
        dossier_pochettes = input("Entrer le dossier dans lequel se trouve les pochettes (dossier des pochettes):\n")
    except EOFError:
        raise ParametreManquant("dossier des pochettes")
    if dossier_pochettes == "":
        raise ParametreManquant("dossier des pochettes")

    if not os.path.exists(dossier_pochettes) or \
            not os.path.isdir(dossier_pochettes) or \
            not os.access(dossier_pochettes, os.R_OK):
        raise ParametreInvalide(INVALIDE_DOSSIER_POCHETTES)

    # Dossier de sauvegarde
    try:
        dossier_sauvegarde = input(
            "Entrer le dossier dans lequel sera sauvegardé l'image résultat (dossier de sauvegarde):\n")
    except EOFError:
        raise ParametreManquant("dossier de sauvegarde")
    if dossier_sauvegarde == "":
        raise ParametreManquant("dossier de sauvegarde")

    if not os.path.exists(dossier_sauvegarde) or \
            not os.path.isdir(dossier_sauvegarde) or \
            not os.access(dossier_sauvegarde, os.R_OK):
        raise ParametreInvalide(INVALIDE_DOSSIER_SAUVEGARDE)

    # Nom de l'image
    try:
        nom = input("Entrer le nom de l'image résultat:\n")
    except EOFError:
        raise ParametreManquant("nom de l'image résultat")
    if nom == "":
        raise ParametreManquant("nom de l'image résultat")

    if not nom.isascii():
        raise ParametreInvalide(INVALIDE_NOM)

    # Format
    try:
        format = input("Entrer le format de l'image résultat:\n")
    except EOFError:
        raise ParametreManquant("format de l'image résultat")
    if format == "":
        raise ParametreManquant("format de l'image résultat")

    if format not in VALID_FORMATS:
        raise ParametreInvalide(f"{INVALIDE_FORMAT}{VALID_FORMATS}")

    # Taille des cases
    try:
        taille_cases = input("Entrer le format de l'image résultat:\n")
        if taille_cases == "":
            raise ParametreManquant("taille des cases de la grille")
        taille_cases = int(taille_cases)

    except EOFError:
        raise ParametreManquant("taille des cases de la grille")
    except ValueError:
        raise ParametreInvalide(INVALIDE_TAILLE_CASES)
    except Exception as e:
        raise e
    if taille_cases <= 0:
        raise ParametreInvalide(INVALIDE_TAILLE_CASES)

    # Définition cible
    try:
        ligne = input("Entrer la définition de l'image résultat (largeur hauteur):\n")
        if ligne == "":
            raise ParametreManquant("définition de l'image résulat")
        ligne = ligne.strip().split(" ")
        if len(ligne) != 2:
            raise ParametreInvalide("")

        definition_cible = (int(ligne[0]), int(ligne[1]))
        if definition_cible[0] <= 0 or definition_cible[1] <= 0:
            raise ParametreInvalide(INVALIDE_DEFINITION_CIBLE)
        elif definition_cible[0] % taille_cases > 0 or definition_cible[1] % taille_cases > 0:
            raise ParametreInvalide(INVALIDE_DEFINITION_CIBLE)

    except EOFError:
        raise ParametreManquant("définition de l'image résulat")
    except ValueError:
        raise ParametreInvalide(INVALIDE_DEFINITION_CIBLE)
    except Exception as e:
        raise e

    # Section tailles des pochettes
    tailles_pochettes = []
    try:
        ligne = input("")
        while ligne != "":
            try:
                ligne = ligne.strip().split(" ")
                if len(ligne) == 2:
                    ligne = [int(ligne[0]), int(ligne[1])]
                    if ligne[0] > 1 and ligne[1] > 0:
                        tailles_pochettes.append(ligne)
                ligne = input("")
            except EOFError:
                ligne = ""
            except ValueError:
                ligne = "continue"
    except EOFError:
        pass

    # Section poids des pochettes
    poids_pochettes = {}
    try:
        ligne = input("")
        while ligne != "":
            try:
                ligne = ligne.strip().split(" ")
                if len(ligne) == 2:
                    ligne = (ligne[0], int(ligne[1]))
                    if ligne[0] != "" and ligne[0].isascii() and ligne[1] > 1:
                        poids_pochettes[ligne[0]] = ligne[1]
                ligne = input("")
            except EOFError:
                ligne = ""
            except ValueError:
                ligne = "continue"
    except EOFError:
        pass
    return dossier_pochettes, dossier_sauvegarde, nom, format, taille_cases, definition_cible, tailles_pochettes, poids_pochettes
