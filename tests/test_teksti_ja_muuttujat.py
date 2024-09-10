import subprocess

def test_script_output():
    # Suoritetaan skripti ja kaapataan sen tuloste
    result = subprocess.run(
        ["python3", "tehtavapalautukset/teksti_ja_muuttujat.py"],  # Vaihda polku oikeaan skriptiin
        capture_output=True, text=True
    )
    
    # Tarkista tuloste
    expected_output = (
        "Hei, Matti! Miten voit?\n"
        "Olen 30-vuotias ja viihdyn hyvin omana itsenäni.\n"
        "Pituuteni on 175 cm, ja se on aina ollut minulle ylpeyden aihe.\n"
        "Painoni on 70.5 kg, ja pyrin pysymään terveenä liikkumalla säännöllisesti.\n"
        "Vuonna 1990 tapahtui historiallinen käännekohta maailmanpolitiikassa.\n"
        "Minulla on yhteensä 10 kukkaa, ja ne tuovat kotiini iloa ja väriä.\n"
        "Kengänkokoni on 42, ja se on ollut vakiovalinta monissa kengissäni.\n"
        "Harrastan aktiivisesti jalkapalloa, ja se on intohimoni.\n"
        "Meillä on perheessämme yhteensä 3 kissaa, ja ne ovat osa arkeamme.\n"
        "Tämän päivän lämpötila on 25.5 astetta, ja aurinko paistaa taivaalla.\n"
        "Meillä on neljä lasta, ja he tuovat iloa ja vilskettä kotiimme.\n"
        "Lempparinumeroni on 7, ja se on aina tuonut minulle onnea.\n"
        "Auton hinta oli 25000 euroa, mutta se oli sen arvoinen.\n"
        "Ystäväni on 35-vuotias, ja olemme jakaneet monet ilot ja surut yhdessä.\n"
        "Lempikukkani on ruusu, ja sen kauneus lumoaa minut aina uudelleen.\n"
        "Matkan pituus oli 10 kilometriä, ja se oli pitkä mutta palkitseva reitti.\n"
        "Lääkkeen käyttöannos on 500 mg, ja se otetaan päivittäin lääkärin ohjeiden mukaan.\n"
        "Työpaikka sijaitsee 15 kilometrin päässä kotoani, joten matkaan menee päivittäin aikaa.\n"
        "Tämä kuukausi on helmikuu, ja se tuo mukanaan talven viimeiset viikot.\n"
        "Ulkona sataa tänään: kyllä. Muista ottaa sateenvarjo mukaasi!"
    )
    
    assert result.stdout.strip() == expected_output.strip()
