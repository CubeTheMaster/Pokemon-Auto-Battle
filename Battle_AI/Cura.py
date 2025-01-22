def use_potion(cursor, pokemon, potion_name):
    # Define the healing amounts for each potion type
    healing_amounts = {
        'pozione': 25,
        'superpozione': 50,
        'iperpozione': 75
    }

    # Check if the potion is available
    cursor.execute("SELECT quatità FROM pozione WHERE nome = %s", (potion_name,))
    result = cursor.fetchone()

    if result and result[0] > 0:
        # Heal the Pokémon
        healing_amount = healing_amounts[potion_name]
        pokemon[4] += healing_amount  # Assuming pokemon[4] is the HP
        print(f"{pokemon[1]} è stato curato di {healing_amount} HP!")

        # Decrease the potion count
        cursor.execute("UPDATE pozione SET quatità = quatità - 1 WHERE nome = %s", (potion_name,))
        cursor._connection.commit()
    else:
        print(f"Nessuna {potion_name} disponibile.")

def ai_use_potion(pokemon, potion_name):
    # Define the healing amounts for each potion type
    healing_amounts = {
        'pozione': 25,
        'superpozione': 50,
        'iperpozione': 75
    }
        # Heal the Pokémon
    healing_amount = healing_amounts[potion_name]
    pokemon[4] += healing_amount  # Assuming pokemon[4] is the HP
    print(f"{pokemon[1]} è stato curato di {healing_amount} HP!")


def reset_potions(cursor):
    """
    Ripristina le quantità delle pozioni nella tabella 'pozione' ai valori iniziali.
    
    Quantità iniziali:
        - pozione: 3
        - superpozione: 2
        - iperpozione: 1
    """
    # Definisci le quantità iniziali per ogni tipo di pozione
    initial_quantities = {
        'pozione': 3,
        'superpozione': 2,
        'iperpozione': 1
    }

    try:
        # Aggiorna le quantità delle pozioni nel database
        for potion, quantity in initial_quantities.items():
            cursor.execute("""
                UPDATE pozione
                SET quatità = %s
                WHERE nome = %s
            """, (quantity, potion))
        
        # Conferma le modifiche al database
        cursor._connection.commit()
        print("Le pozioni sono state ripristinate con successo!")
    
    except Exception as e:
        print(f"Si è verificato un errore durante il ripristino delle pozioni: {e}")
        cursor._connection.rollback()