import pytest
import random
from src.grille import Grille
from src.images import recuperer_pochettes


@pytest.fixture()
def generer_parametres_valides():
    parametres_test = ["./pochettesTests/", "../", "test", "jpeg", 120, (1920, 1080), [[5, 1], [4, 1]],
                       {"holyDiver": 5, "kingsOfMetal": 3}]
    lignes = parametres_test[:4]
    lignes.append(str(parametres_test[4]))
    lignes.append(f"{parametres_test[5][0]} {parametres_test[5][1]}")
    for elem in parametres_test[6]:
        lignes.append(f"{elem[0]} {elem[1]}")
        if random.randint(0, 2) == 1:
            # Ajout de bruit
            rand = random.randint(0, 5)
            if rand == 0:
                lignes.append(f"ee 15")
            elif rand == 1:
                lignes.append(f"{random.random()} 15")
            elif rand == 2:
                lignes.append(f"{random.randint(-5, 1)} 15")
            elif rand == 3:
                lignes.append(f"10 ee")
            elif rand == 4:
                lignes.append(f"5 {random.random()}")
            elif rand == 5:
                lignes.append(f"5 {random.randint(-5, 0)}")
    lignes.append('')
    for key in parametres_test[7]:
        lignes.append(f"{key} {parametres_test[7][key]}")
        if random.randint(0, 2) == 1:
            # Ajout de bruit
            rand = random.randint(1, 5)
            if rand == 1:
                lignes.append(f"👀 15")
            elif rand == 2:
                lignes.append(f"test {random.randint(-5, 1)}")
            elif rand == 3:
                lignes.append(f"test {random.random()}")
            elif rand == 4:
                lignes.append(f"test est")
            elif rand == 5:
                lignes.append(f"test ")
    lignes.append('')
    return parametres_test, lignes


@pytest.fixture()
def images(generer_parametres_valides):
    parametres = generer_parametres_valides[0]
    return recuperer_pochettes(parametres[0], parametres[-1])


@pytest.fixture()
def grille(generer_parametres_valides):
    parametres = generer_parametres_valides[0]
    grille = Grille(parametres[5], parametres[4], parametres[-2])
    return grille
