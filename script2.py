import csv



def charger_pokémons_csv(fichier1):
    # dictionnaire qui contient la liste des pokemons et ses stats
    pokemons = {}

    # lecture du fichier csv
    with open(fichier1, 'r', encoding = "utf-8" ) as f:
        lecteur_csv = csv.reader(f)
        for ligne in lecteur_csv:
            nom = ligne[0]
            stats = ligne[1:]

            stats_entier = []

            for stat in stats:
                stats_entier.append(int(stat))

            pokemons[nom] = stats_entier
        return pokemons





pkmn = charger_pokémons_csv("fichier/pokemon.csv")
for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")


pkmn = charger_pokémons_csv("fichier/pokemon.csv")
print(isinstance(pkmn, dict))
print(isinstance(pkmn["Pikachu"], list))
print(isinstance(pkmn["Pikachu"][0], int))





