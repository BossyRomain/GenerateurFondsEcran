# Classe représentant la grille
import copy
import random


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
        taille = max(toutes_tailles)

        trouver = False
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
        while j < taille and (coords[0] + i, coords[1] + j) in self.cases_libres:
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
            self.cases[y][x] = copy.deepcopy(image.pixels)
        else:
            index = 0
            while self.tailles_pochettes[index][0] != taille:
                index += 1
            self.tailles_pochettes[index][1] -= 1
            if self.tailles_pochettes[index][1] == 0:
                self.tailles_pochettes.pop(index)

            step = int(100 / taille)
            for i in range(taille):
                for j in range(taille):
                    self.cases[y + j][x + i] = image.pixels[i * step:(i + 1) * step, j * step:(j + 1) * step]
