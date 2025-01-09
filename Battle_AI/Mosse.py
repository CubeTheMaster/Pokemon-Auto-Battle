


# Funzione per recuperare le mosse di un Pokémon
def get_moves(cursor, pokemon_id):
    query = """
        SELECT m.* FROM mossa m
        JOIN conosce c ON m.id = c.id_mossa
        WHERE c.id_pk = %s
    """
    cursor.execute(query, (pokemon_id,))
    return cursor.fetchall()