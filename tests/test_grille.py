from src.grille import Grille
from src.images import Image
import cv2


def test_creation():
    test_dimensions = (16, 9)
    test_taille_cases = 120
    test_tailles_pochettes = [[5, 4], [9, 1]]

    grille = Grille((test_dimensions[0] * test_taille_cases, test_dimensions[1] * test_taille_cases), test_taille_cases, test_tailles_pochettes)

    assert grille.dimensions == test_dimensions
    assert grille.taille_cases == 120
    assert len(grille.cases) == test_dimensions[1]
    assert len(grille.cases[0]) == test_dimensions[0]
    assert len(grille.cases_libres) == test_dimensions[0] * test_dimensions[1]
    assert grille.tailles_pochettes == sorted(test_tailles_pochettes, reverse=True, key=lambda x: (x[0],x[1]))


def test_get_carre_libre1():
    test_dimensions = (5, 5)
    test_taille_cases = 120
    grille = Grille((test_dimensions[0] * test_taille_cases, test_dimensions[1] * test_taille_cases), test_taille_cases, [[5, 4], [9, 1], [2, 1]])

    coords, taille = grille.get_carrer_cases_libres()
    assert taille == 5


def test_get_carre_libre2():
    test_dimensions = (5, 25)
    test_taille_cases = 120
    grille = Grille((test_dimensions[0] * test_taille_cases, test_dimensions[1] * test_taille_cases), test_taille_cases, [])

    coords, taille = grille.get_carrer_cases_libres()
    assert taille == 1


def test_get_carre_libre2():
    test_dimensions = (25, 25)
    test_taille_cases = 120
    grille = Grille((test_dimensions[0] * test_taille_cases, test_dimensions[1] * test_taille_cases), test_taille_cases, [])

    coords, taille = grille.get_carrer_cases_libres()
    assert taille == 1


def test_ajouter_image():
    test_dimensions = (25, 25)
    test_taille_cases = 120
    test_image = Image("test", 5, cv2.imread("tests/recuperation_pochettes/aNightAtTheOpera.jpeg"))
    grille = Grille((test_dimensions[0] * test_taille_cases, test_dimensions[1] * test_taille_cases), test_taille_cases, [[5, 1]])

    coords, taille = grille.get_carrer_cases_libres()
    grille.ajouter_image(test_image, coords, taille)

    for dl in range(taille):
        for dc in range(taille):
            assert grille.cases[coords[0] + dl][coords[1] + dc] is not None