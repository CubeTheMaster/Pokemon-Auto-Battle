#Function to heal user's pokemon
def use_potion(cursor, pokemon, potion_name):
    healing_amounts = {
        'pozione': 25,
        'superpozione': 50,
        'iperpozione': 75
    }

    cursor.execute("SELECT quatità FROM pozione WHERE nome = %s", (potion_name,))
    result = cursor.fetchone()

    if result and result[0] > 0:
        healing_amount = healing_amounts[potion_name]
        pokemon[4] += healing_amount
        print(f"{pokemon[1]} è stato curato di {healing_amount} HP!")

        cursor.execute("UPDATE pozione SET quatità = quatità - 1 WHERE nome = %s", (potion_name,))
        cursor._connection.commit()
    else:
        print(f"Nessuna {potion_name} disponibile.")

#Function to heal Ai's pokemon
def ai_use_potion(pokemon, potion_name):
    healing_amounts = {
        'pozione': 25,
        'superpozione': 50,
        'iperpozione': 75
    }
    healing_amount = healing_amounts[potion_name]
    pokemon[4] += healing_amount
    print(f"{pokemon[1]} è stato curato di {healing_amount} HP!")

#Function to reset potions
def reset_potions(cursor):
    initial_quantities = {
        'pozione': 3,
        'superpozione': 2,
        'iperpozione': 1
    }

    try:
        for potion, quantity in initial_quantities.items():
            cursor.execute("""
                UPDATE pozione
                SET quatità = %s
                WHERE nome = %s
            """, (quantity, potion))
        
        cursor._connection.commit()
    
    except Exception as e:
        print(f"Si è verificato un errore durante il ripristino delle pozioni: {e}")
        cursor._connection.rollback()