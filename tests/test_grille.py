from src.grille import Grille


def test_creation_grille(generer_parametres_valides):
    parametres = generer_parametres_valides[0]
    grille = Grille(parametres[5], parametres[4], parametres[-2])

    assert grille.dimensions == (int(parametres[5][0] / parametres[4]), int(parametres[5][1] / parametres[4]))
    assert grille.tailles_pochettes == parametres[-2]
    assert len(grille.cases) == grille.dimensions[1]
    assert len(grille.cases[0]) == grille.dimensions[0]
    assert len(grille.cases_libres) == grille.dimensions[0] * grille.dimensions[1]
    for x in range(grille.dimensions[0]):
        for y in range(grille.dimensions[1]):
            assert grille.cases[y][x] is None


def test_est_carre_libre(grille):
    assert grille.est_carrer_libre((0, 0), 5)
    assert not grille.est_carrer_libre((0, 0), 50)


def test_trouver_carrer_libre(grille):
    coords, taille = grille.trouver_carre_libre()
    assert taille == 5


def test_ajouter_carrer(grille, images):
    coords, taille = grille.trouver_carre_libre()
    grille.ajouter_image(images[0], coords, taille)

    assert len(grille.cases_libres) == grille.dimensions[0] * grille.dimensions[1] - taille * taille
    for x in range(coords[0], coords[0] + taille):
        for y in range(coords[1], coords[1] + taille):
            assert grille.cases[y][x] is not None
