import pytest
from src.images import recuperer_pochettes

def test_recuperation_pochettes_correcte():
    pochettes = recuperer_pochettes("tests/recuperation_pochettes/", {"lastInLine": 5, "blackDogBarking": 5, "dirt": 2, "dreamEvil": 2})

    poids_precedent = 100000000
    for p in pochettes:
        assert p.poids <= poids_precedent
        poids_precedent = p.poids


def test_recuperation_pochettes_vide():
    with pytest.raises(SystemExit) as err:
        recuperer_pochettes("tests/", {})
    assert err.value.code == 2