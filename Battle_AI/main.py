import mysql.connector
from Pokemon import *
from Mosse import *
from Battaglia import *


#Database connection
def connect_to_database(password):
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password= password,
        database="lotta"
    )

#Main function
def main():
    password = input("Inserisci la password del database: ")
    db = connect_to_database(password)
    cursor = db.cursor()

    #Ask the user how many pokemons he wants in his team
    while True:
        try:
            team_size = int(input("Quanti Pokémon vuoi nel tuo team? (1-6): "))
            if 1 <= team_size <= 6:
                break
            else:
                print("Valore non accettato. Ricorda: un team può essere composto da 1-6 Pokémon.")
        except ValueError:
            print("Inserisci un numero valido.")

    #Generates a random team for the user and the AI
    user_team = get_random_pokemons(cursor, team_size)
    user_team_with_moves = assign_random_moves(cursor, user_team)

    ai_team_1 = get_random_pokemons(cursor, team_size)
    ai_team_with_moves_1 = assign_random_moves(cursor, ai_team_1)

    user_vs_ai_battle(user_team_with_moves, ai_team_with_moves_1, cursor, team_size)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()



