import subprocess
import os
import tempfile

# Korvattavat arvot input() kutsuille
INPUT_VALUES = {
    "Anna etunimi: ": "Mikkohermanni",
    "Anna sukunimi: ": "Mallikas",
    "Anna päiväys (dd.mm.yyyy): ": "01.01.2000",
    "Anna koko nimesi: ": "Jaska Grindevald",
    "Anna etunimesi: ": "Mikkohermanni Mallikas",
    "Anna syntymäpäiväsi (dd.mm.yyyy): ": "01.01.2000",
}

def replace_input_prompts(script_path, values):
    """Korvataan input() kutsuja tilapäisessä skriptissä kovakoodatuilla arvoilla."""
    with open(script_path, 'r') as file:
        lines = file.readlines()

    with open(script_path, 'w') as file:
        for line in lines:
            for prompt, value in values.items():
                # Korvataan tarkalleen 'input("Anna etunimi1: ")' -> '"Mikkohermanni"'
                if f'input("{prompt}")' in line:
                    line = line.replace(f'input("{prompt}")', f'"{value}"')
            file.write(line)

def test_script_output():
    """Testaa muokattua skriptiä."""
    # Luo tilapäinen tiedosto
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(open('tehtavapalautukset/merkkien_indeksit.py').read().encode('utf-8'))
        temp_script_path = temp_file.name

    # Korvaa input() kutsut
    replace_input_prompts(temp_script_path, INPUT_VALUES)

    # Tulosta tilapäisen tiedoston sisältö
    with open(temp_script_path, 'r') as file:
        print("Tilapäinen skripti:")
        print(file.read())

    try:
        # Suorita skripti ja kaapataan sen tuloste
        result = subprocess.run(
            ["python3", temp_script_path],
            capture_output=True, text=True
        )

        # Tulosta tuloste debuggausta varten
        print("Skripti tuloste:")
        print(result.stdout)

        # Tarkista tuloste
        expected_output = (
            "jaska.jokunen@sahkoposti.fi\n"
            "MikMal\n"
            "Jokunen\n"
            "raseko\n"
            "2000\n"
            "J.G.\n"
            "Mias\n"
            "Synnyit 01 vuonna 2000\n"
            "21200\n"
            "Jaska Jokunen\n"
            "gfedcba\n"
            "gnimmarg\n"
            "65\n"
            "sisylanA \n"
            "git itervR\n"
            "dlroW olleH\n"
            "gfedc\n"
            " xof nworb\n"
        )

        assert result.stdout.strip() == expected_output.strip()

    finally:
        # Poista tilapäinen skripti
        if os.path.exists(temp_script_path):
            os.remove(temp_script_path)
