import json

from deepdiff import DeepDiff


while True:

    nomefile1 = str(input("Inserisci il cognome del CV che vuoi confrontare (esci per uscire): ")) + "true"

    nomefile2 = nomefile1.replace("true", "")


    if nomefile2.lower() == "esci":

        exit()

    

    # CARICAMENTO FILE JSON

    try:

        with open(f"Verita/{nomefile1}.json", encoding="utf-8") as f:

            data_true = json.load(f)


        with open(f"DaComparare/{nomefile2}.json", encoding="utf-8") as f:

            data_cv = json.load(f)


        break

    except FileNotFoundError:

        print("File non trovato. Riprova.")


# CONFRONTO

diff = DeepDiff(data_true, data_cv, ignore_order=True)


if not diff:

    print("I file sono uguali")

    exit()


print("I file sono diversi\n")


# FUNZIONE PER LA MAPPA DELLE CATEGORIE


def mappa_categoria(path):

    path = path.lower()


    if "nome" in path or "cognome" in path:

        return "Nome e Cognome"

    if "età" in path or "eta" in path:

        return "Età"

    if "istruzione" in path:

        return "Livello di istruzione"

    if "anzian" in path:

        return "Anni di anzianità"

    if "ruolo" in path:

        return "Ruolo"

    if "competenze_tecniche" in path:

        return "Competenze Tecniche"

    if "lingue" in path:

        return "Lingue"

    if "soft_skills" in path:

        return "Soft skills"

    if "tecnologie" in path:

        return "Tecnologie conosciute"

    if "certific" in path:

        return "Certificazioni"


    return None




# RACCOLTA CATEGORIE CON DIFFERENZE

categorie_con_differenze = set()


# valori modificati

if "values_changed" in diff:

    for path in diff["values_changed"]:

        cat = mappa_categoria(path)

        if cat:

            categorie_con_differenze.add(cat)


# elementi aggiunti

if "iterable_item_added" in diff:

    for path in diff["iterable_item_added"]:

        cat = mappa_categoria(path)

        if cat:

            categorie_con_differenze.add(cat)


# elementi rimossi

if "iterable_item_removed" in diff:

    for path in diff["iterable_item_removed"]:

        cat = mappa_categoria(path)

        if cat:

            categorie_con_differenze.add(cat)



# OUTPUT FINALE PULITO

for categoria in sorted(categorie_con_differenze):

    print(f"Differenze trovate in {categoria}")