import sys

# Messages d'erreurs pour chaque paramètre lorsqu'il est invalide
INVALIDE_DOSSIER_POCHETTES = "le dossier des pochettes doit être un dossier existant et accessible (droits lectures)."
INVALIDE_DOSSIER_SAUVEGARDE = "le dossier de sauvegarde doit être un dossier existant et accessible (droits lectures)."
INVALIDE_NOM = "le nom de l'image résultat ne doit contenir que des caractères ASCII"
INVALIDE_FORMAT = "le format de l'image résultat doit être dans la liste suivante: "
INVALIDE_TAILLE_CASES = "la taille des cases de la grille doit être une valeur entière positive supérieure à 0"
INVALIDE_DEFINITION_CIBLE = "la définition de l'image résultat doit être composée de deux valeurs séparées par un espace. " \
                            "Chaque valeur doit être un entier positif supérieur à 0 et divisible par la taille des cases de la grille."


class ParametreManquant(Exception):
    def __init__(self, message):
        super(Exception, self).__init__()
        self.message = message

    def __str__(self):
        return f"\nParametre manquant: {self.message}"


class ParametreInvalide(Exception):
    def __init__(self, message):
        super(Exception, self).__init__()
        self.message = message

    def __str__(self):
        return f"\nParametre invalide: {self.message}"


def afficherErreur(message):
    print(message, file=sys.stderr)


def afficherErreurEtQuitter(message, code_retour):
    afficherErreur(message)
    exit(code_retour)
