from Pokemon import choose_pokemon
from Accuracy import does_move_hit
from Cura import *
import random

def calculate_damage_and_hit(move, attacker, defender):
    if does_move_hit(move[4]):
        type_effectiveness = calculate_type_advantage(move[2], defender[2], defender[3])
        attack_stat = attacker[5] if move[5] == 'fisica' else attacker[7]
        defense_stat = defender[6] if move[5] == 'fisica' else defender[8]
        damage = ((2 * 50 / 5 + 2) * move[3] * (attack_stat / defense_stat) / 50 + 2) * type_effectiveness
        return damage, True
    return 0, False

def execute_move(attacker, move, defender):
    print(f"{attacker[1]} usa {move[1]}!")
    damage, hit = calculate_damage_and_hit(move, attacker, defender)
    if hit:
        defender[4] = max(defender[4] - damage, 0)
        print(f"{defender[1]} subisce {damage:.2f} danni! Rimangono {defender[4]:.2f} HP.")
    else:
        print(f"{attacker[1]} ha mancato!")
    return defender[4] <= 0

def use_ai_potion(cursor, ai_pokemon, ai_token):
    cursor.execute("SELECT hp FROM pokemon WHERE id = %s", (ai_pokemon[0],))
    pokemon_maxHP = cursor.fetchone()
    pokemon_maxHP = 0.8 * pokemon_maxHP[0]
    if ai_pokemon[4] <= pokemon_maxHP and ai_token > 0:
        potion = 'iperpozione' if ai_token == 3 else 'superpozione'
        print(f"{ai_pokemon[1]} usa una {potion}!")
        ai_use_potion(ai_pokemon, potion)
        return ai_token - 1
    return ai_token

def use_potion_menu(cursor, pokemon):
    print(f"\nScegli una pozione da usare:")
    
    # Recupera le pozioni disponibili con quantità maggiore di zero
    cursor.execute("SELECT nome FROM pozione WHERE quatità > 0")
    potions = [row[0] for row in cursor.fetchall()]
    
    if not potions:
        print("Non hai pozioni disponibili.")
        return
    
    for idx, potion in enumerate(potions):
        # Recupera la quantità disponibile per ogni pozione
        cursor.execute("SELECT quatità FROM pozione WHERE nome = %s", (potion,))
        quantity = cursor.fetchone()[0]
        print(f"[{idx + 1}] {potion.capitalize()} (Disponibili: {quantity})")
    
    while True:
        try:
            choice = int(input("Seleziona una pozione: "))
            if 1 <= choice <= len(potions):
                selected_potion = potions[choice - 1]
                use_potion(cursor, pokemon, selected_potion)
                break
            else:
                print("Scelta non valida. Riprova.")
        except ValueError:
            print("Inserisci un numero valido.")

def select_best_ai_pokemon(ai_team, user_active_pokemon):
    """
    Seleziona il Pokémon dell'IA con la massima efficacia contro il Pokémon attivo dell'utente.
    
    Args:
        ai_team (list): Lista dei Pokémon dell'IA.
        user_active_pokemon (tuple): Pokémon attivo dell'utente.
    
    Returns:
        tuple: (Pokémon selezionato, Mosse del Pokémon selezionato)
    """
    best_pokemon = None
    best_moves = None
    highest_advantage = -1

    for ai_pokemon, ai_moves in ai_team:
        advantage = calculate_type_advantage(ai_pokemon[2], user_active_pokemon[2], user_active_pokemon[3], ai_pokemon[3])
        if advantage > highest_advantage:
            highest_advantage = advantage
            best_pokemon = ai_pokemon
            best_moves = ai_moves
    
    return best_pokemon, best_moves

def still_best_pokemon(ai_pokemon, user_active_pokemon, ai_team):
    best_pokemon = None
    highest_advantage = -1

    for pokemon in ai_team:
        advantage = calculate_type_advantage(pokemon[2], user_active_pokemon[2], user_active_pokemon[3], pokemon[3])
        if advantage > highest_advantage:
            highest_advantage = advantage
            best_pokemon = pokemon
    if ai_pokemon == best_pokemon:
        return True
    else:
        return False

# Funzione per scegliere la mossa migliore
def select_best_move(moves, opponent):
    best_move = None
    best_score = 0

    for move in moves:
        damage = move[3]
        accuracy = move[4]
        type_effectiveness = calculate_type_advantage(move[2], opponent[2], opponent[3])

        # Se l'avversario ha pochi HP, privilegia precisione
        if opponent[4] <= damage:
            score = accuracy * type_effectiveness
        else:
            score = damage * (accuracy / 100) * type_effectiveness

        if score > best_score:
            best_score = score
            best_move = move

    return best_move

def show_moves(pokemon):
    print(f"\nLe mosse di {pokemon[0]}:")
    for move in pokemon[1]:
        print(f"- {move[0]} (Potenza: {move[3]}, Precisione: {move[4]})")

def show_team(user_team):
    print(f"\nIl tuo team attuale:")
    display_team(user_team)

def compare_speed(pokemon1, pokemon2):
    if pokemon1[9] > pokemon2[9]:
        return pokemon1
    elif pokemon1[9] < pokemon2[9]:
        return pokemon2
    else:
        return random.choice([pokemon1, pokemon2])
    
def choose_move(pokemon_moves):
    print(f"\nScegli una mossa per {pokemon_moves[0][1]}:")
    for idx, move in enumerate(pokemon_moves[1]):
        print(f"[{idx + 1}] {move[1]} (Danno: {move[3]}, Precisione: {move[4]})")

    while True:
        try:
            choice = int(input("Seleziona una mossa: "))
            if 1 <= choice <= len(pokemon_moves[1]):
                return pokemon_moves[1][choice - 1]
            else:
                print("Scelta non valida. Riprova.")
        except ValueError:
            print("Inserisci un numero valido.")

def user_vs_ai_battle(user_team, ai_team, cursor, team_size):
    print(f"\nInizia la battaglia!")

    #varaiables neeeded to make battle logic work
    ai_token = 3
    defeated = False
    user_defeated = False

    show_team(user_team)

    user_active_pokemon, user_active_moves = choose_pokemon(user_team, team_size)
    print(f"\nVai {user_active_pokemon[1]}! Io credo in te!")
    ai_active_pokemon, ai_active_moves = select_best_ai_pokemon(ai_team, user_active_pokemon)
    user_hp = user_active_pokemon[4]
    ai_hp = ai_active_pokemon[4]
    max_hp = ai_active_pokemon[4]
    print(f"\nGennaro (Bullo) manda in campo {ai_active_pokemon[1]}")



    while user_team and ai_team:
            
        while user_hp > 0 and ai_hp > 0:
            
            print(f"\nCosa deve fare {user_active_pokemon[1]}?")
            print("\n[1] Attaccare")
            print("\n[2] Usare strumenti")
            print("\n[3] Cambiare Pokémon")

            while True:
                try:
                    user_choice = int(input("Seleziona un'opzione (1, 2 o 3): "))
                    if user_choice in [1, 2, 3]:
                        break
                    else:
                        print("Scelta non valida. Riprova.")
                except ValueError:
                    print("Inserisci un numero valido.")


            if user_choice == 1:
                user_move = choose_move([user_active_pokemon, user_active_moves])
            elif user_choice == 2:
                use_potion_menu(cursor, user_active_pokemon)
                user_hp = user_active_pokemon[4]
            elif user_choice == 3:
                show_team(user_team)
                user_active_pokemon, user_active_moves = choose_pokemon(user_team, team_size)
                print(f"\nVai {user_active_pokemon[1]}! Io credo in te!")
                user_hp = user_active_pokemon[4]


            if compare_speed(user_active_pokemon, ai_active_pokemon) == user_active_pokemon:

            
            
                #attacco
                if user_choice == 1:
                    defeated = execute_move(user_active_pokemon, user_move, ai_active_pokemon)
                    if user_hp > 0 and defeated:
                        print(f"\nIl {ai_active_pokemon[1]} di Gennaro (Bullo) non è più in grado di lottare!")
                        ai_team.remove([ai_active_pokemon, ai_active_moves])
                        if ai_team:
                            ai_active_pokemon, ai_active_moves = select_best_ai_pokemon(ai_team, user_active_pokemon)
                            ai_hp = ai_active_pokemon[4]
                            max_hp = ai_active_pokemon[4]
                            print(f"\nGennaro (Bullo) manda in campo {ai_active_pokemon[1]}. Gennaro è pronto a vendicarsi!")
                        else:
                            print(f"\nHai vinto la battaglia. Ti senti fiero di rapinare un bambino?")
                            reset_potions(cursor)
                            break
                    
            
                #turno ia
                if not defeated:
                    use_heal = max_hp * 0.2
                    if ai_active_pokemon[4] <= use_heal and ai_token > 0:
                        ai_token = use_ai_potion(cursor, ai_active_pokemon, ai_token)
                    elif ai_active_pokemon == select_best_ai_pokemon(ai_team, user_active_pokemon)[0]:
                        ai_move = select_best_move(ai_active_moves, user_active_pokemon)
                        user_defeated = execute_move(ai_active_pokemon, ai_move, user_active_pokemon)
                        if ai_hp > 0 and user_defeated:
                            print(f"\nIl tuo {user_active_pokemon[1]} non è più in grado di lottare!")
                            user_team.remove([user_active_pokemon, user_active_moves])
                            user_defeated = False
                            if user_team:
                                show_team(user_team)
                                while True:
                                    try:
                                        print(f"\nScegli il tuo Pokémon successivo")
                                        user_active_pokemon, user_active_moves = choose_pokemon(user_team, team_size)
                                        user_hp = user_active_pokemon[4]
                                        print(f"\nVai {user_active_pokemon[1]}, vendica il tuo compagno!")
                                        break
                                    except ValueError:
                                        print(f"Scelta non valida. Riprova.")
                                break
                            else:
                                print(f"\nHai perso la battaglia. Sborsa i soldi!")
                                reset_potions(cursor)
                                break
                    else:
                        ai_active_pokemon, ai_active_moves = select_best_ai_pokemon(ai_team, user_active_pokemon)
                        ai_hp = ai_active_pokemon[4]
                        max_hp = ai_active_pokemon[4]
                        print(f"\nGennaro (Bullo) manda in campo {ai_active_pokemon[1]}. Gennaro è pronto a vendicarsi!")
                else:
                    defeated = False

            else:
                
                #turno ia
                use_heal = max_hp * 0.2
                if ai_active_pokemon[4] <= use_heal and ai_token > 0:
                    ai_token = use_ai_potion(cursor, ai_active_pokemon, ai_token) #da controllare
                elif ai_active_pokemon == select_best_ai_pokemon(ai_team, user_active_pokemon)[0]:
                    ai_move = select_best_move(ai_active_moves, user_active_pokemon)
                    user_defeated = execute_move(ai_active_pokemon, ai_move, user_active_pokemon)
                    if ai_hp > 0 and user_defeated:
                        print(f"\nIl tuo {user_active_pokemon[1]} non è più in grado di lottare!")
                        user_team.remove([user_active_pokemon, user_active_moves])
                        user_defeated = False
                        if user_team:
                            show_team(user_team)
                            while True:
                                try:
                                    print(f"\nScegli il tuo Pokémon successivo")
                                    user_active_pokemon, user_active_moves = choose_pokemon(user_team, team_size)
                                    user_hp = user_active_pokemon[4]
                                    print(f"\nVai {user_active_pokemon[1]}, vendica il tuo compagno!")
                                    break
                                except ValueError:
                                    print(f"Scelta non valida. Riprova.")
                        else:
                            print(f"\nHai perso la battaglia. Sborsa i soldi!")
                            reset_potions(cursor)
                            break
                else:
                    ai_active_pokemon, ai_active_moves = select_best_ai_pokemon(ai_team, user_active_pokemon)
                    ai_hp = ai_active_pokemon[4]
                    max_hp = ai_active_pokemon[4]
                    print(f"\nGennaro (Bullo) manda in campo {ai_active_pokemon[1]}. Gennaro è pronto a vendicarsi!")    

                #attacco
                if user_choice == 1:
                    defeated = execute_move(user_active_pokemon, user_move, ai_active_pokemon)
                    if user_hp > 0 and defeated:
                        print(f"\nIl {ai_active_pokemon[1]} di Gennaro (Bullo) non è più in grado di lottare!")
                        ai_team.remove([ai_active_pokemon, ai_active_moves])
                        defeated = False   
                        if ai_team:
                            ai_active_pokemon, ai_active_moves = select_best_ai_pokemon(ai_team, user_active_pokemon)
                            ai_hp = ai_active_pokemon[4]
                            max_hp = ai_active_pokemon[4]
                            print(f"\nGennaro (Bullo) manda in campo {ai_active_pokemon[1]}. Gennaro è pronto a vendicarsi!")
                            break
                        else:
                            print(f"\nHai vinto la battaglia. Ti senti fiero di rapinare un bambino?")
                            reset_potions(cursor)
                            break




# Funzione per simulare una battaglia IA vs IA
def ai_vs_ai_battle(ai_team_1, ai_team_2, cursor):
    print(f"\nBattaglia tra due squadre IA!")

    ai1_token = 3  # Token per le pozioni della prima IA
    ai2_token = 3  # Token per le pozioni della seconda IA

    while ai_team_1 and ai_team_2:
        ai1_active_pokemon, ai1_active_moves = ai_team_1[0]
        ai2_active_pokemon, ai2_active_moves = ai_team_2[0]

        print(f"{ai1_active_pokemon[1]} VS {ai2_active_pokemon[1]}")

        ai1_hp = ai1_active_pokemon[4]
        ai2_hp = ai2_active_pokemon[4]

        while ai1_hp > 0 and ai2_hp > 0:
            if ai1_active_pokemon[9] >= ai2_active_pokemon[9]:
                print(f"Il {ai1_active_pokemon[1]} usa una mossa!")
                ai1_move = select_best_move(ai1_active_moves, ai2_active_pokemon)
                damage, hit = calculate_damage_and_hit(ai1_move, ai1_active_pokemon, ai2_active_pokemon)
                if hit:
                    ai2_hp -= damage
                    ai2_active_pokemon[4] = max(ai2_hp, 0)
                    print(f"{ai2_active_pokemon[1]} subisce {damage:.2f} danni! Rimangono {ai2_hp:.2f} HP.")

                    if ai2_hp <= 0:
                        print(f"{ai2_active_pokemon[1]} è stato sconfitto!")
                        ai_team_2.pop(0)
                        break
                else:
                    print(f"Il {ai1_active_pokemon[1]} ha mancato!")

                if ai2_hp > 0 and ai2_hp <= 0.1 * ai2_active_pokemon[4] and ai2_token > 0:
                    if ai2_token == 3:
                        print(f"Il {ai2_active_pokemon[1]} usa una iperpozione!")
                        use_potion(cursor, ai2_active_pokemon, 'iperpozione')
                    else:
                        print(f"Il {ai2_active_pokemon[1]} usa una superpozione!")
                        use_potion(cursor, ai2_active_pokemon, 'superpozione')
                    ai2_token -= 1

            else:
                print(f"Il {ai2_active_pokemon[1]} usa una mossa!")
                ai2_move = select_best_move(ai2_active_moves, ai1_active_pokemon)
                damage, hit = calculate_damage_and_hit(ai2_move, ai2_active_pokemon, ai1_active_pokemon)
                if hit:
                    ai1_hp -= damage
                    ai1_active_pokemon[4] = max(ai1_hp, 0)
                    print(f"{ai1_active_pokemon[1]} subisce {damage:.2f} danni! Rimangono {ai1_hp:.2f} HP.")

                    if ai1_hp <= 0:
                        print(f"{ai1_active_pokemon[1]} è stato sconfitto!")
                        ai_team_1.pop(0)
                        break
                else:
                    print(f"Il {ai2_active_pokemon[1]} ha mancato!")

                if ai1_hp > 0 and ai1_hp <= 0.1 * ai1_active_pokemon[4] and ai1_token > 0:
                    if ai1_token == 3:
                        print(f"Il {ai1_active_pokemon[1]} usa una iperpozione!")
                        use_potion(cursor, ai1_active_pokemon, 'iperpozione')
                    else:
                        print(f"Il {ai1_active_pokemon[1]} usa una superpozione!")
                        use_potion(cursor, ai1_active_pokemon, 'superpozione')
                    ai1_token -= 1

    if not ai_team_1:
        print(f"\nLa seconda squadra IA ha vinto!")
    elif not ai_team_2:
        print(f"\nLa prima squadra IA ha vinto!")
                    


# Funzione per calcolare l'efficacia di tipo
def calculate_type_advantage(attacking_type_1, defender_type_1, defender_type_2=None, attacking_type_2=None):
    type_chart = {
        'Normal': {'weak_to': ['Fighting'], 'strong_against': [], 'immune_to': ['Ghost']},
        'Fire': {'weak_to': ['Water', 'Rock', 'Ground'], 'strong_against': ['Grass', 'Ice', 'Bug', 'Steel'], 'immune_to': []},
        'Water': {'weak_to': ['Electric', 'Grass'], 'strong_against': ['Fire', 'Rock', 'Ground'], 'immune_to': []},
        'Electric': {'weak_to': ['Ground'], 'strong_against': ['Water', 'Flying'], 'immune_to': []},
        'Grass': {'weak_to': ['Fire', 'Ice', 'Poison', 'Flying', 'Bug'], 'strong_against': ['Water', 'Ground', 'Rock'], 'immune_to': []},
        'Ice': {'weak_to': ['Fire', 'Fighting', 'Rock', 'Steel'], 'strong_against': ['Grass', 'Ground', 'Flying', 'Dragon'], 'immune_to': []},
        'Fighting': {'weak_to': ['Flying', 'Psychic', 'Fairy'], 'strong_against': ['Normal', 'Ice', 'Rock', 'Dark', 'Steel'], 'immune_to': []},
        'Poison': {'weak_to': ['Ground', 'Psychic'], 'strong_against': ['Grass', 'Fairy'], 'immune_to': []},
        'Ground': {'weak_to': ['Water', 'Ice', 'Grass'], 'strong_against': ['Fire', 'Electric', 'Poison', 'Rock', 'Steel'], 'immune_to': ['Electric']},
        'Flying': {'weak_to': ['Electric', 'Ice', 'Rock'], 'strong_against': ['Grass', 'Fighting', 'Bug'], 'immune_to': ['Ground']},
        'Psychic': {'weak_to': ['Bug', 'Ghost', 'Dark'], 'strong_against': ['Fighting', 'Poison'], 'immune_to': []},
        'Bug': {'weak_to': ['Fire', 'Flying', 'Rock'], 'strong_against': ['Grass', 'Psychic', 'Dark'], 'immune_to': []},
        'Rock': {'weak_to': ['Water', 'Grass', 'Fighting', 'Ground', 'Steel'], 'strong_against': ['Fire', 'Ice', 'Flying', 'Bug'], 'immune_to': []},
        'Ghost': {'weak_to': ['Ghost', 'Dark'], 'strong_against': ['Psychic', 'Ghost'], 'immune_to': ['Normal', 'Fighting']},
        'Dragon': {'weak_to': ['Ice', 'Dragon', 'Fairy'], 'strong_against': ['Dragon'], 'immune_to': []},
        'Dark': {'weak_to': ['Fighting', 'Bug', 'Fairy'], 'strong_against': ['Psychic', 'Ghost'], 'immune_to': ['Psychic']},
        'Steel': {'weak_to': ['Fire', 'Fighting', 'Ground'], 'strong_against': ['Ice', 'Rock', 'Fairy'], 'immune_to': ['Poison']},
        'Fairy': {'weak_to': ['Poison', 'Steel'], 'strong_against': ['Fighting', 'Dragon', 'Dark'], 'immune_to': ['Dragon']}
    }

    # Start with a neutral multiplier
    multiplier = 1.0

    # Helper function to calculate effect
    def calculate_effect(attacking, defending):
        nonlocal multiplier
        if defending in type_chart[attacking]['strong_against']:
            multiplier *= 2.0  # Super effective
        elif defending in type_chart[attacking]['weak_to']:
            multiplier *= 0.5  # Not very effective
        elif defending in type_chart[attacking]['immune_to']:
            multiplier *= 0.0  # No effect

    # Check against the first defender type
    calculate_effect(attacking_type_1, defender_type_1)
    if attacking_type_2:
        calculate_effect(attacking_type_2, defender_type_1)

    # Check against the second defender type if it exists
    if defender_type_2:
        calculate_effect(attacking_type_1, defender_type_2)
        if attacking_type_2:
            calculate_effect(attacking_type_2, defender_type_2)

    return multiplier

# Funzione per stampare il team dell'utente
def display_team(team):
    for idx, (pokemon, moves) in enumerate(team):
        print(f"[{idx + 1}] {pokemon[1]} (HP: {pokemon[4]})")
        print(f"   Mosse:")
        for move in moves:
            print(f"      - {move[1]} (Danno: {move[3]}, Precisione: {move[4]})")

