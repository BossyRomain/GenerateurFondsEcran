import sys
# Module de gestion des erreurs

# Messages d'erreurs pour les paramètres lorsqu'ils sont invalides
INVALIDE_DOSSIER = "le dossier doit : exister, être accessible, et le programme doit avoir les droits de lecture sur celui-ci"
INVALIDE_NOM = "le nom ne doit être composé que de caractères ASCII"
INVALIDE_FORMAT = "le format doit être présent dans la liste suivante : "
INVALIDE_TAILLE_CASES = "la taille des cases doit être une valeur entière supérieure à 0"
INVALIDE_DEFINITION_CIBLE = "la défintion cible doit être composée de deux valeurs (séparées par un espace) entières supérieures à 0 et divisibles par la taille des cases"
INVALIDE_TAILLE_POCHETTE = "une taille de pochette doit être composée de deux valeurs (séparées par un espace) entières avec v1 > 1 et v2 > 0."
INVALIDE_POIDS_POCHETTE = "un poids de pochette doit être composée de deux valeurs (séparées par un espace) v1 est une chaine de caractères ASCII sans espace et v2 un entier supérieur à 1."


# Erreur pour un paramètre manquant
class ParametreManquant(Exception):
    def __init__(self, message):
        super(Exception, self).__init__()
        self.message = message

    def __str__(self):
        return f"parametre manquant : {self.message}!"
    

# Erreur pour un paramètre invalide
class ParametreInvalide(Exception):
    def __init__(self, message):
        super(Exception, self).__init__()
        self.message = message

    def __str__(self):
        return f"parametre invalide : {self.message}!"
    
    
# Erreur pour un fichier d'image incorrect
class ImageInvalide(Exception):
    def __init__(self, nom_fichier):
        super(Exception, self).__init__()
        self.nom_fichier = nom_fichier
    
    def __str__(self):
        return f"Le fichier {self.nom_fichier} n'est un fichier d'image ou n'est pas lisible"


# Affiche un message d'avertissement sur la sortie d'erreur en orange
def afficherAvertissement(message):
    print(f'\033[33mAvertissement : \033[00m{message}', file=sys.stderr)


# Affiche un message d'erreur sur la sortie d'erreur
def afficherErreur(message):
    print(f'\033[31mErreur \033[00m{message}', file=sys.stderr)


# Affiche un message d'erreur sur la sortie d'erreur et termine le programme avec le code de retour code_retour
def afficherErreurEtQuitter(message, code_retour):
    afficherErreur(message)
    exit(code_retour)