# test_useampi_muuttuja_tekstissa.py
import io
import sys

def test_script_output():
    # Kaappaa tulosteen
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Suorita skripti
    exec(open('tehtavapalautukset/useampi_muuttuja_tekstissa.py').read())

    # Palauta stdout alkuperäiseen tilaan
    sys.stdout = sys.__stdout__

    # Tarkista tuloste
    expected_output = (
        "Hei, Matti Möttönen! Kuinka voin auttaa sinua tänään?\n"
        "Asun kaupungissa Helsinki, maassa Suomi, ja täällä on hienoa!\n"
        "Ostin juuri uuden tuotteen puhelin, ja se maksoi 599.99 euroa.\n"
        "Tänään on maanantai, ja sää on aurinkoinen. Aurinko paistaa taivaalla!\n"
        "Olen juuri aloittanut lukemaan kirjaa Seitsemän veljestä, jonka on kirjoittanut Aleksis Kivi.\n"
        "Opiskelen kieltä ranska kurssilla keskitaso, ja se on haastavaa mutta hauskaa.\n"
        "Ajan autolla Toyota Corolla, ja se on luotettava kumppani matkoillani.\n"
        "Tänään tilasin ruoan pizza Pizzeria Napoli-ravintolasta, ja se oli herkullista.\n"
        "Nautin aamuisin juomaa kahvi ja juon sen Café Paris-kahvilassa. Se antaa hyvän startin päivälle.\n"
        "Harrastan aktiivisesti urheilulajia tennis Tennis Club-seurassa. Se pitää minut kunnossa."
    )

    assert captured_output.getvalue().strip() == expected_output.strip()
