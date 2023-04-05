import copy
import random
import cv2

# Classe représentant la grille
class Grille:
    def __init__(self, definition_cible, taille_cases, tailles_pochettes):
        # Dimensions de la grille (largeur, hauteur)
        self.dimensions = (int(definition_cible[0] / taille_cases), int(definition_cible[1] / taille_cases))
        # Taille des cases sur la grille
        self.taille_cases = taille_cases
        # Taille des pochettes sur la grille (Triées par taille décroissante)
        self.tailles_pochettes = sorted(tailles_pochettes, reverse=True, key=lambda x: (x[0],x[1])) if len(tailles_pochettes) > 0 else []
        # Les cases de la grille
        self.cases = [[None for c in range(self.dimensions[0])] for l in range(self.dimensions[1])]
        # L'ensemble des cases libres sur la grille (ligne, colonne)
        self.cases_libres = [(l, c) for c in range(self.dimensions[0]) for l in range(self.dimensions[1])]
        random.shuffle(self.cases_libres)


    def get_carrer_cases_libres(self):
        taille = 1
        coords_coin_hg = None
        h = 0
        while h < len(self.tailles_pochettes) and coords_coin_hg is None:
            i = 0
            while i < len(self.cases_libres) and not self.__est_carrer_libre(self.cases_libres[i], self.tailles_pochettes[h][0]):
                i += 1 
            if i == len(self.cases_libres):
                h += 1
            else:
                coords_coin_hg = self.cases_libres[i]
        if h < len(self.tailles_pochettes):
            taille = self.tailles_pochettes[h][0]

        if coords_coin_hg is None:
            coords_coin_hg = self.cases_libres[0]

        return coords_coin_hg, taille


    # Retourne vrai si le carre de cases est libre sur la grille
    def __est_carrer_libre(self, coords_coin_hg, taille):
        ligne, colonne = coords_coin_hg
        if ligne + taille - 1 >= self.dimensions[1] or colonne + taille - 1 >= self.dimensions[0]:
            return False
        
        dl = dc = 0
        while dl < taille and self.cases[ligne + dl][colonne + dc] is None:
            dc += 1
            if dc == taille:
                dc = 0
                dl += 1
        return dl == taille
    

    # Ajout l'image dans le carré de cases sur la grille
    def ajouter_image(self, image, coords_coin_hg, taille):
        ligne, colonne = coords_coin_hg
        for dl in range(taille):
            for dc in range(taille):
                self.cases_libres.remove((ligne + dl, colonne + dc))

        # Redimmensionnement de l'image
        img = cv2.resize(image.pixels, (self.taille_cases, self.taille_cases))

        if taille == 1:
            self.cases[ligne][colonne] = copy.deepcopy(image)
        else:
            step = int(self.taille_cases / taille)
            for dl in range(taille):
                for dc in range(taille):
                    crop = img[dl * step:(dl + 1) * step, dc * step:(dc + 1) * step]   
                    self.cases[ligne + dl][colonne + dc] = copy.deepcopy(crop)