import mysql.connector
from Pokemon import *
from Mosse import *
from Battaglia import *

# cambiare la connection in modo da renderla automatizzata
# database connection
def connect_to_database(password):
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password= password,
        database="lotta"
    )

# Main function
def main():
    password = input("Inserisci la password del database: ")
    db = connect_to_database(password)
    cursor = db.cursor()

    # Chiedi all'utente la dimensione del team
    while True:
        try:
            team_size = int(input("Quanti Pokémon vuoi nel tuo team? (1-6): "))
            if 1 <= team_size <= 6:
                break
            else:
                print("Valore non accettato. Ricorda: un team può essere composto da 1-6 Pokémon.")
        except ValueError:
            print("Inserisci un numero valido.")

    # Genera i team
    user_team = get_random_pokemons(cursor, team_size)
    user_team_with_moves = assign_random_moves(cursor, user_team)

    ai_team_1 = get_random_pokemons(cursor, team_size)
    ai_team_with_moves_1 = assign_random_moves(cursor, ai_team_1)

    ai_team_2 = get_random_pokemons(cursor, team_size)
    ai_team_with_moves_2 = assign_random_moves(cursor, ai_team_2)

    # Chiedi all'utente l'azione da intraprendere
    print("\nVuoi partecipare alla battaglia o guardare una sfida tra IA?")
    print("1. Partecipa alla battaglia")
    print("2. Sfida tra IA")

    while True:
        try:
            choice = int(input("Seleziona un'opzione (1 o 2): "))
            if choice == 1:
                user_vs_ai_battle(user_team_with_moves, ai_team_with_moves_1, cursor, team_size)
                break
            elif choice == 2:
                ai_vs_ai_battle(ai_team_with_moves_1, ai_team_with_moves_2, cursor)
                break
            else:
                print("Scelta non valida. Riprova.")
        except ValueError:
            print("Inserisci un numero valido.")

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()



