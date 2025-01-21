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
        cursor.connection.commit()
    else:
        print(f"Nessuna {potion_name} disponibile.")