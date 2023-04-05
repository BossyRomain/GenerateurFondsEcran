import pytest
import os
from src.parametres import lire_parametres
from src.erreurs import ParametreManquant, ParametreInvalide

def test_lecture_correcte(monkeypatch):
    fichier = open("tests/lecture_parametres/parametres.txt", "r")
    iterator = iter([ligne.strip() for ligne in fichier.readlines()])
    monkeypatch.setattr("builtins.input", lambda a: next(iterator))
    fichier.close()

    parametres = lire_parametres()

    fichier = open("tests/lecture_parametres/parametres_corrects.txt", "r")
    iterator = iter([ligne.strip() for ligne in fichier.readlines()])
    monkeypatch.setattr("builtins.input", lambda a: next(iterator))
    parametres_attendus = lire_parametres()
    fichier.close()

    for p, p_a in zip(parametres, parametres_attendus):
        assert p == p_a


def test_parametres_manquant(monkeypatch):
    entrees_valides = [".", ".", "test", "png", "120", "1920 1080"]
    i = 0
    while i < len(entrees_valides):
        entrees = entrees_valides[0:i]
        entrees.append("")
        iterator = iter(entrees)
        monkeypatch.setattr("builtins.input", lambda a: next(iterator))
        with pytest.raises(ParametreManquant):
            lire_parametres() 
        i += 1


def test_dossiers_invalides(monkeypatch):
    entrees = []
    while len(entrees) < 2:
        iterator = iter(entrees + ["tests/lecture_parametres/__init__.py"])
        monkeypatch.setattr("builtins.input", lambda a: next(iterator))
        with pytest.raises(ParametreInvalide):
            lire_parametres()

        iterator = iter(entrees + ["tests/lecture_parametres/noaccessfolder/dossier/"])
        os.system("chmod a-x tests/lecture_parametres/noaccessfolder/")
        monkeypatch.setattr("builtins.input", lambda a: next(iterator))
        with pytest.raises(ParametreInvalide):
            lire_parametres()
        os.system("chmod a+x tests/lecture_parametres/noaccessfolder/")

        iterator = iter(entrees + ["tests/lecture_parametres/norightsfolder/"])
        os.system("chmod a-r tests/lecture_parametres/norightsfolder/")
        monkeypatch.setattr("builtins.input", lambda a: next(iterator))
        with pytest.raises(ParametreInvalide):
            lire_parametres()
        os.system("chmod a+r tests/lecture_parametres/norightsfolder/")
        entrees.append(".")


def test_nom_invalide(monkeypatch):
    iterator = iter([".", ".", "🌷"])
    monkeypatch.setattr("builtins.input", lambda a: next(iterator))
    with pytest.raises(ParametreInvalide):
        lire_parametres()


def test_format_invalide(monkeypatch):
    iterator = iter([".", ".", "test", "blabla"])
    monkeypatch.setattr("builtins.input", lambda a: next(iterator))
    with pytest.raises(ParametreInvalide):
        lire_parametres()


def test_taille_cases_invalide(monkeypatch):
    entrees = [".", ".", "test", "png"]
    tests = ["ee", "5.0", "-15", "15 58"]
    for test in tests:
        iterator = iter(entrees + [test])
        monkeypatch.setattr("builtins.input", lambda a: next(iterator))
        with pytest.raises(ParametreInvalide):
            lire_parametres()


def test_definition_cible_invalide(monkeypatch):
    entrees = [".", ".", "test", "png", "120"]
    tests = ["ee 120", "5.0 120", "-15 120", "1 120", "120 ee", "120 5.0", "120 -5", "120 1", "120 1 1"]
    for test in tests:
        iterator = iter(entrees + [test])
        monkeypatch.setattr("builtins.input", lambda a: next(iterator))
        with pytest.raises(ParametreInvalide):
            lire_parametres()