import random

# Funzione per recuperare le mosse di un Pokémon
def get_moves(cursor, pokemon_id):
    query = """
        SELECT m.* FROM mossa m
        JOIN conosce c ON m.id = c.id_mossa
        WHERE c.id_pk = %s
    """
    cursor.execute(query, [pokemon_id,])
    return cursor.fetchall()

# Funzione per assegnare mosse casuali ai Pokémon
def assign_random_moves(cursor, pokemons):
    team_with_moves = []
    for pokemon in pokemons:
        moves = get_moves(cursor, pokemon[0])
        if len(moves) > 4:
            moves = random.sample(moves, 4)  # Seleziona 4 mosse casuali se il Pokémon ne conosce più di 4
        team_with_moves.append([pokemon, moves])
    return team_with_moves