import json
import csv

# lecture du fichier JSON
def json_to_csv(fichier1,fichier2):
    with open(fichier1, "r", encoding="utf-8") as f:
        data = json.load(f)

# ajout du contenu du fichier JSON dans le fichier CSV
    with open(fichier2, 'w', newline = '', encoding= "utf-8") as f:
        ecrivain_csv = csv.writer(f, delimiter=',')
        # ajout des colonnes
        ecrivain_csv.writerow(["reel", "imaginaire"])

        # ajout des données
        for lignes in data:
            ecrivain_csv.writerow(lignes)





json_to_csv("fichier/data.json", "fichier/data.csv")