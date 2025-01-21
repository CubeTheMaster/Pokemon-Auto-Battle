
# Funzione per ottenere dei Pokémon casuali
def get_random_pokemons(cursor, team_size):
    query = "SELECT * FROM pokemon ORDER BY RAND() LIMIT %s"
    cursor.execute(query, [team_size,])
    return [list(pokemon) for pokemon in cursor.fetchall()]

# Funzione per scegliere un Pokémon iniziale
def choose_pokemon(team, team_size):
    if team_size == 1:
        return team[0][0], team[0][1]
    else:
        while True:
            try:
                choice = int(input("Seleziona il numero del Pokémon che vuoi mandare in campo: "))
                if 1 <= choice <= len(team):
                    return team[choice - 1][0], team[choice - 1][1]
                else:
                    print(f"Scelta non valida. Riprova.")
            except ValueError:
                print(f"Inserisci un numero valido.")