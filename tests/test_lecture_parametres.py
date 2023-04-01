import os
import random

import pytest

from src.parametres import lire_parametres
from src.erreurs import ParametreManquant, ParametreInvalide


def test_lecture_correcte(monkeypatch, generer_parametres_valides):
    iterator = iter(generer_parametres_valides[1])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))

    parametres = lire_parametres()
    for p, p_t in zip(parametres, generer_parametres_valides[0]):
        assert p == p_t


def test_dossier_pochettes_manquant(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda a: '')
    with pytest.raises(ParametreManquant):
        lire_parametres()


def test_dossier_sauvegarde_manquant(monkeypatch):
    iterator = iter(['../', ''])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreManquant):
        lire_parametres()


def test_nom_manquant(monkeypatch):
    iterator = iter(['../', '../', ''])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreManquant):
        lire_parametres()


def test_format_manquant(monkeypatch):
    iterator = iter(['../', '../', 'test', ''])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreManquant):
        lire_parametres()


def test_taille_cases_manquant(monkeypatch):
    iterator = iter(['../', '../', 'test', 'png', ''])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreManquant):
        lire_parametres()


def test_definition_cible_manquant(monkeypatch):
    iterator = iter(['../', '../', 'test', 'png', '120', ''])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreManquant):
        lire_parametres()


def test_dossier_pochettes_invalide(monkeypatch):
    iterator = iter(['./dossierinexistant'])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreInvalide):
        lire_parametres()

    os.system("chmod a-r dossierAucunsDroits")
    iterator = iter(['./dossierinexistant'])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreInvalide):
        lire_parametres()
    os.system("chmod a+r dossierAucunsDroits")

    iterator = iter(['./__init__.py'])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreInvalide):
        lire_parametres()


def test_dossier_sauvegarde_invalide(monkeypatch):
    iterator = iter(['../', './dossierinexistant'])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreInvalide):
        lire_parametres()

    os.system("chmod a-r dossierAucunsDroits")
    iterator = iter(['../', './dossierinexistant'])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreInvalide):
        lire_parametres()
    os.system("chmod a+r dossierAucunsDroits")

    iterator = iter(['../', './__init__.py'])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreInvalide):
        lire_parametres()


def test_nom_invalide(monkeypatch):
    iterator = iter(['../', '../', '👀'])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreInvalide):
        lire_parametres()


def test_format_invalide(monkeypatch):
    iterator = iter(['../', '../', 'test', 'teu'])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreInvalide):
        lire_parametres()


def test_taille_cases_invalide(monkeypatch):
    iterator = iter(['../', '../', 'test', 'png', 'grzg'])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreInvalide):
        lire_parametres()

    iterator = iter(['../', '../', 'test', 'png', '5.0'])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreInvalide):
        lire_parametres()

    iterator = iter(['../', '../', 'test', 'png', '-5'])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreInvalide):
        lire_parametres()


def test_definition_cible_invalide(monkeypatch):
    iterator = iter(['../', '../', 'test', 'png', '120', 'ee '])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreInvalide):
        lire_parametres()

    iterator = iter(['../', '../', 'test', 'png', '120', 'ee 120'])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreInvalide):
        lire_parametres()

    iterator = iter(['../', '../', 'test', 'png', '120', '120 5.0'])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreInvalide):
        lire_parametres()

    iterator = iter(['../', '../', 'test', 'png', '120', '1 120'])
    monkeypatch.setattr('builtins.input', lambda a: next(iterator))
    with pytest.raises(ParametreInvalide):
        lire_parametres()
