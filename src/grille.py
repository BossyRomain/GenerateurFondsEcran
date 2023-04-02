import copy
import random
import cv2


# Classe représentant la grille
class Grille:
    def __init__(self, definition_cible, taille_cases, tailles_pochettes):
        self.taille_cases = taille_cases
        # (Largeur, Hauteur)
        self.dimensions = (int(definition_cible[0] / taille_cases), int(definition_cible[1] / taille_cases))
        # Les cases de la grille
        self.cases = [[None for c in range(self.dimensions[0])] for l in range(self.dimensions[1])]
        # L'ensemble de cases libres sur la grille
        self.cases_libres = [(x, y) for x in range(self.dimensions[0]) for y in range(self.dimensions[1])]
        random.shuffle(self.cases_libres)
        # Les tailles des pochettes possibles sur la grille
        self.tailles_pochettes = copy.deepcopy(tailles_pochettes)

    # Résultat : retourne les coordonnées du coin haut gauche ainsi
    # que la longueur des côtés en nombre de cases d'un carré de cases libres sur la grille
    def trouver_carre_libre(self):
        toutes_tailles = [elem[0] for elem in self.tailles_pochettes]
        if len(toutes_tailles) == 0:
            taille = 1
        else:
            taille = max(toutes_tailles)

        trouver = False
        coords = self.cases_libres[0]
        while taille > 1 and not trouver:
            i = 0
            while i < len(self.cases_libres) and not self.est_carrer_libre(self.cases_libres[i], taille):
                i += 1

            if i < len(self.cases_libres):
                coords = self.cases_libres[i]
                trouver = True
            else:
                taille -= 1

        return coords, taille

    # Résultat : retourne True si le carré de cases de coin haut gauche coords et
    # de longueur taille est libre sinon False
    def est_carrer_libre(self, coords, taille):
        if coords[0] + taille > self.dimensions[0] or coords[1] + taille > self.dimensions[1]:
            return False

        i = j = 0
        while j < taille and self.cases[coords[1] + j][coords[0] + i] is None:
            i += 1
            if i == taille:
                i = 0
                j += 1
        return j == taille

    # Paramètres :
    # - image : l'image à mettre dans le carré
    # - coords : les coordonnées du coin haut gauche du carré
    # - taille : la longueur des côtés du carré en nombre de cases
    # Pré-conditions :
    # - le carré doit être libre
    # Résultat : place image dans le carré sur la grille
    def ajouter_image(self, image, coords, taille):
        x, y = coords
        for i in range(taille):
            for j in range(taille):
                self.cases_libres.remove((x + i, y + j))

        if taille == 1:
            img = cv2.resize(image.pixels, (taille * self.taille_cases, taille * self.taille_cases))
            self.cases[y][x] = copy.deepcopy(img)
        else:
            index = 0
            while self.tailles_pochettes[index][0] != taille:
                index += 1
            self.tailles_pochettes[index][1] -= 1
            if self.tailles_pochettes[index][1] == 0:
                self.tailles_pochettes.pop(index)

            L = self.taille_cases * taille
            step = int(L / taille)
            img = cv2.resize(image.pixels, (L, L))
            for j in range(taille):
                for i in range(taille):
                    x_start = i * step
                    x_end = (i + 1) * step
                    y_start = j * step
                    y_end = (j + 1) * step
                    self.cases[y + j][x + i] = img[y_start:y_end, x_start:x_end]

    # Résultat : retourne l'image résultat
    def obtenir_image_resultat(self):
        lignes_fusionnees = []
        for y in range(self.dimensions[1]):
            lignes_fusionnees.append(cv2.hconcat(self.cases[y]))

        return cv2.vconcat(lignes_fusionnees)
