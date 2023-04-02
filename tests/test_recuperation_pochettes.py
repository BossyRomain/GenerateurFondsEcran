import math
import os

import pytest

from src.images import recuperer_pochettes


def test_recuperation_correcte(generer_parametres_valides):
    images = recuperer_pochettes(generer_parametres_valides[0][0], generer_parametres_valides[0][-1])
    prec = math.inf
    for img in images:
        assert img.poids <= prec
        prec = img.poids


def test_recuperation_vide(generer_parametres_valides):
    os.system("chmod a-r pochettesTests/*")
    with pytest.raises(SystemExit):
        recuperer_pochettes(generer_parametres_valides[0][0], generer_parametres_valides[0][-1])
    os.system("chmod a+r pochettesTests/*")
