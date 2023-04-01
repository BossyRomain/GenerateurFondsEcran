import pytest
import random


@pytest.fixture()
def generer_parametres_valides():
    parametres_test = ["../../AlbumsCovers/", "../", "test", "jpeg", 120, (240, 360), [[5, 1], [4, 1]],
                       [("test", 5), ("blabla", 3)]]
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
    for elem in parametres_test[7]:
        lignes.append(f"{elem[0]} {elem[1]}")
        if random.randint(0, 2) == 1:
            # Ajout de bruit
            rand = random.randint(0, 5)
            if rand == 0:
                lignes.append(f"120 15")
            elif rand == 1:
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
