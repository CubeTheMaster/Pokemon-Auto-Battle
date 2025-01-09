import mysql.connector
from Pokemon import *
from Mosse import *
from Battaglia import *

# cambiare la connection in modo da renderla automatizzata
# database connection
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Araki_1986",
        database="lotta"
    )

def battle(pokemon1, moves1, pokemon2, moves2):
    hp1 = pokemon1[4]
    hp2 = pokemon2[4]

    print(f"\nInizia la battaglia: {pokemon1[1]} VS {pokemon2[1]}\n")

    while hp1 > 0 and hp2 > 0:
        # Determina chi attacca per primo
        if pokemon1[9] >= pokemon2[9]:
            attacker, defender = pokemon1, pokemon2
            attacker_moves, defender_moves = moves1, moves2
            attacker_hp, defender_hp = hp1, hp2
        else:
            attacker, defender = pokemon2, pokemon1
            attacker_moves, defender_moves = moves2, moves1
            attacker_hp, defender_hp = hp2, hp1

        # Scegli la mossa dell'attaccante
        move = select_best_move(attacker_moves, defender)

        print(f"{attacker[1]} usa {move[1]}!")



        # Calcola l'efficacia di tipo
        type_effectiveness = calculate_type_advantage(move[2], defender[2], defender[3])

        # Determina se l'attacco è fisico o speciale
        if move[5] == 'fisica':
            attack_stat = attacker[5]
            defense_stat = defender[6]
        else:
            attack_stat = attacker[7]
            defense_stat = defender[8]

        # Calcola il danno
        damage = ((2 * 50 / 5 + 2) * move[3] * (attack_stat / defense_stat) / 50 + 2) * type_effectiveness
        defender_hp -= damage

        print(f"{defender[1]} subisce {damage:.2f} danni! Rimangono {max(defender_hp, 0):.2f} HP.")

        # Aggiorna gli HP
        if attacker == pokemon1:
            hp2 = defender_hp
        else:
            hp1 = defender_hp

        # Controlla se il difensore è stato sconfitto
        if defender_hp <= 0:
            print(f"{defender[1]} è stato sconfitto! {attacker[1]} vince la battaglia!\n")
            break


# Main function
def main():
    db = connect_to_database()
    cursor = db.cursor()

    # The player chooses a Pokémon
    user_pokemon_name = input("Seleziona un Pokémon per la battaglia: ")
    user_pokemon = get_pokemon(cursor, user_pokemon_name)

    if not user_pokemon:
        print("Pokémon non trovato nel database.")
        return

    user_moves = get_moves(cursor, user_pokemon[0])

    # The IA chooses a Pokémon
    ai_pokemon = select_best_pokemon(cursor, user_pokemon)
    ai_moves = get_moves(cursor, ai_pokemon[0])

    print(f"\nHai scelto {user_pokemon[1]}!")
    print(f"L'IA ha scelto {ai_pokemon[1]}!\n")

    # Start battle
    battle(user_pokemon, user_moves, ai_pokemon, ai_moves)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()






# Funcction for the battle



