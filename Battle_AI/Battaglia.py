from Pokemon import choose_pokemon
from Accuracy import does_move_hit

# Funzione per simulare una battaglia utente vs IA
# Riscrivere alcune parti del codice per renderlo più facile da leggere e mantenere la funzionalità
def user_vs_ai_battle(user_team, ai_team):
    print("\nInizia la battaglia!")

    while user_team and ai_team:
        # Seleziona il Pokémon dell'utente
        print("\nIl tuo team attuale:")
        display_team(user_team)
        print("\nScegli il tuo Pokémon iniziale o successivo")
        user_active_pokemon, user_active_moves = choose_pokemon(user_team)

        # Seleziona il Pokémon dell'IA
        ai_active_pokemon, ai_active_moves = max(ai_team, key=lambda p: calculate_type_advantage(p[0][2], user_active_pokemon[2], user_active_pokemon[3]))

        print(f"\nHai scelto {user_active_pokemon[1]}! L'IA ha scelto {ai_active_pokemon[1]}!")

        user_hp = user_active_pokemon[4]
        ai_hp = ai_active_pokemon[4]

        while user_hp > 0 and ai_hp > 0:
            print("\nLe tue mosse disponibili:")
            for idx, move in enumerate(user_active_moves):
                print(f"[{idx + 1}] {move[1]} (Danno: {move[3]}, Precisione: {move[4]})")

            while True:
                try:
                    user_move_idx = int(input("Seleziona il numero della mossa da usare: ")) - 1
                    if 0 <= user_move_idx < len(user_active_moves):
                        user_move = user_active_moves[user_move_idx]
                        break
                    else:
                        print("Scelta non valida. Riprova.")
                except ValueError:
                    print("Inserisci un numero valido.")

            if user_active_pokemon[9] >= ai_active_pokemon[9]:
                print(f"Il tuo {user_active_pokemon[1]} usa {user_move[1]}! ")

                type_effectiveness = calculate_type_advantage(user_move[2], ai_active_pokemon[2], ai_active_pokemon[3])
                attack_stat = user_active_pokemon[5] if user_move[5] == 'fisica' else user_active_pokemon[7]
                defense_stat = ai_active_pokemon[6] if user_move[5] == 'fisica' else ai_active_pokemon[8]

                damage = ((2 * 50 / 5 + 2) * user_move[3] * (attack_stat / defense_stat) / 50 + 2) * type_effectiveness
                ai_hp -= damage
                ai_active_pokemon[4] = max(ai_hp, 0)

                print(f"{ai_active_pokemon[1]} subisce {damage:.2f} danni! Rimangono {ai_hp:.2f} HP.")

                if ai_hp <= 0:
                    print(f"Il {ai_active_pokemon[1]} avversario è stato sconfitto!")
                    ai_team.remove([ai_active_pokemon, ai_active_moves])
                    break

                ai_move = select_best_move(ai_active_moves, user_active_pokemon)
                print(f"Il {ai_active_pokemon[1]} avversario usa {ai_move[1]}!")
                type_effectiveness = calculate_type_advantage(ai_move[2], user_active_pokemon[2], user_active_pokemon[3])
                attack_stat = ai_active_pokemon[5] if ai_move[5] == 'fisica' else ai_active_pokemon[7]
                defense_stat = user_active_pokemon[6] if ai_move[5] == 'fisica' else user_active_pokemon[8]

                damage = ((2 * 50 / 5 + 2) * ai_move[3] * (attack_stat / defense_stat) / 50 + 2) * type_effectiveness
                user_hp -= damage
                user_active_pokemon[4] = max(user_hp, 0)

                print(f"{user_active_pokemon[1]} subisce {damage:.2f} danni! Rimangono {user_hp:.2f} HP.")

                if user_hp <= 0:
                    print(f"Il tuo {user_active_pokemon[1]} è stato sconfitto!")
                    user_team.remove([user_active_pokemon, user_active_moves])
                    break

            else:
                ai_move = select_best_move(ai_active_moves, user_active_pokemon)
                print(f"Il {ai_active_pokemon[1]} avversario usa {ai_move[1]}!")
                type_effectiveness = calculate_type_advantage(ai_move[2], user_active_pokemon[2], user_active_pokemon[3])
                attack_stat = ai_active_pokemon[5] if ai_move[5] == 'fisica' else ai_active_pokemon[7]
                defense_stat = user_active_pokemon[6] if ai_move[5] == 'fisica' else user_active_pokemon[8]

                damage = ((2 * 50 / 5 + 2) * ai_move[3] * (attack_stat / defense_stat) / 50 + 2) * type_effectiveness
                user_hp -= damage
                user_active_pokemon[4] = max(user_hp, 0)

                print(f"{user_active_pokemon[1]} subisce {damage:.2f} danni! Rimangono {user_hp:.2f} HP.")

                if user_hp <= 0:
                    print(f"Il tuo {user_active_pokemon[1]} è stato sconfitto!")
                    user_team.remove([user_active_pokemon, user_active_moves])
                    break

                print(f"Il tuo {user_active_pokemon[1]} usa {user_move[1]}! ")
                type_effectiveness = calculate_type_advantage(user_move[2], ai_active_pokemon[2], ai_active_pokemon[3])
                attack_stat = user_active_pokemon[5] if user_move[5] == 'fisica' else user_active_pokemon[7]
                defense_stat = ai_active_pokemon[6] if user_move[5] == 'fisica' else ai_active_pokemon[8]

                damage = ((2 * 50 / 5 + 2) * user_move[3] * (attack_stat / defense_stat) / 50 + 2) * type_effectiveness
                ai_hp -= damage
                ai_active_pokemon[4] = max(ai_hp, 0)

                print(f"{ai_active_pokemon[1]} subisce {damage:.2f} danni! Rimangono {ai_hp:.2f} HP.")

                if ai_hp <= 0:
                    print(f"{ai_active_pokemon[1]} è stato sconfitto!")
                    ai_team.remove([ai_active_pokemon, ai_active_moves])
                    break

    if not user_team:
        print("\nHai perso la battaglia!")
    elif not ai_team:
        print("\nHai vinto la battaglia!")


# Funzione per simulare una battaglia IA vs IA
# Funzione non ancora disponibile, manca una logica per far combattere due squadre IA
def user_vs_ai_battle(user_team, ai_team):
    print("\nInizia la battaglia!")

    while user_team and ai_team:
        # Seleziona il Pokémon dell'utente
        print("\nIl tuo team attuale:")
        display_team(user_team)
        print("\nScegli il tuo Pokémon iniziale o successivo")
        user_active_pokemon, user_active_moves = choose_pokemon(user_team)

        # Seleziona il Pokémon dell'IA
        ai_active_pokemon, ai_active_moves = max(ai_team, key=lambda p: calculate_type_advantage(p[0][2], user_active_pokemon[2], user_active_pokemon[3]))

        print(f"\nHai scelto {user_active_pokemon[1]}! L'IA ha scelto {ai_active_pokemon[1]}!")

        user_hp = user_active_pokemon[4]
        ai_hp = ai_active_pokemon[4]

        while user_hp > 0 and ai_hp > 0:
            print("\nLe tue mosse disponibili:")
            for idx, move in enumerate(user_active_moves):
                print(f"[{idx + 1}] {move[1]} (Danno: {move[3]}, Precisione: {move[4]})")

            while True:
                try:
                    user_move_idx = int(input("Seleziona il numero della mossa da usare: ")) - 1
                    if 0 <= user_move_idx < len(user_active_moves):
                        user_move = user_active_moves[user_move_idx]
                        break
                    else:
                        print("Scelta non valida. Riprova.")
                except ValueError:
                    print("Inserisci un numero valido.")

            if user_active_pokemon[9] >= ai_active_pokemon[9]:
                print(f"Il tuo {user_active_pokemon[1]} usa {user_move[1]}! ")

                if does_move_hit(user_move[4]):
                    type_effectiveness = calculate_type_advantage(user_move[2], ai_active_pokemon[2], ai_active_pokemon[3])
                    attack_stat = user_active_pokemon[5] if user_move[5] == 'fisica' else user_active_pokemon[7]
                    defense_stat = ai_active_pokemon[6] if user_move[5] == 'fisica' else ai_active_pokemon[8]

                    damage = ((2 * 50 / 5 + 2) * user_move[3] * (attack_stat / defense_stat) / 50 + 2) * type_effectiveness
                    ai_hp -= damage
                    ai_active_pokemon[4] = max(ai_hp, 0)

                    print(f"{ai_active_pokemon[1]} subisce {damage:.2f} danni! Rimangono {ai_hp:.2f} HP.")

                    if ai_hp <= 0:
                        print(f"Il {ai_active_pokemon[1]} avversario è stato sconfitto!")
                        ai_team.remove([ai_active_pokemon, ai_active_moves])
                        break
                else:
                    print(f"Il {user_active_pokemon[1]} ha mancato!")

                ai_move = select_best_move(ai_active_moves, user_active_pokemon)
                print(f"Il {ai_active_pokemon[1]} avversario usa {ai_move[1]}!")
                if does_move_hit(ai_move[4]):
                    type_effectiveness = calculate_type_advantage(ai_move[2], user_active_pokemon[2], user_active_pokemon[3])
                    attack_stat = ai_active_pokemon[5] if ai_move[5] == 'fisica' else ai_active_pokemon[7]
                    defense_stat = user_active_pokemon[6] if ai_move[5] == 'fisica' else user_active_pokemon[8]

                    damage = ((2 * 50 / 5 + 2) * ai_move[3] * (attack_stat / defense_stat) / 50 + 2) * type_effectiveness
                    user_hp -= damage
                    user_active_pokemon[4] = max(user_hp, 0)

                    print(f"{user_active_pokemon[1]} subisce {damage:.2f} danni! Rimangono {user_hp:.2f} HP.")

                    if user_hp <= 0:
                        print(f"Il tuo {user_active_pokemon[1]} è stato sconfitto!")
                        user_team.remove([user_active_pokemon, user_active_moves])
                        break
                else:
                    print(f"Il {ai_active_pokemon[1]} ha mancato!")

            else:
                ai_move = select_best_move(ai_active_moves, user_active_pokemon)
                print(f"Il {ai_active_pokemon[1]} avversario usa {ai_move[1]}!")
                if does_move_hit(ai_move[4]):
                    type_effectiveness = calculate_type_advantage(ai_move[2], user_active_pokemon[2], user_active_pokemon[3])
                    attack_stat = ai_active_pokemon[5] if ai_move[5] == 'fisica' else ai_active_pokemon[7]
                    defense_stat = user_active_pokemon[6] if ai_move[5] == 'fisica' else user_active_pokemon[8]

                    damage = ((2 * 50 / 5 + 2) * ai_move[3] * (attack_stat / defense_stat) / 50 + 2) * type_effectiveness
                    user_hp -= damage
                    user_active_pokemon[4] = max(user_hp, 0)

                    print(f"{user_active_pokemon[1]} subisce {damage:.2f} danni! Rimangono {user_hp:.2f} HP.")

                    if user_hp <= 0:
                        print(f"Il tuo {user_active_pokemon[1]} è stato sconfitto!")
                        user_team.remove([user_active_pokemon, user_active_moves])
                        break
                else:
                    print(f"Il {ai_active_pokemon[1]} ha mancato!")

                print(f"Il tuo {user_active_pokemon[1]} usa {user_move[1]}! ")
                if does_move_hit(user_move[4]):
                    type_effectiveness = calculate_type_advantage(user_move[2], ai_active_pokemon[2], ai_active_pokemon[3])
                    attack_stat = user_active_pokemon[5] if user_move[5] == 'fisica' else user_active_pokemon[7]
                    defense_stat = ai_active_pokemon[6] if user_move[5] == 'fisica' else ai_active_pokemon[8]

                    damage = ((2 * 50 / 5 + 2) * user_move[3] * (attack_stat / defense_stat) / 50 + 2) * type_effectiveness
                    ai_hp -= damage
                    ai_active_pokemon[4] = max(ai_hp, 0)

                    print(f"{ai_active_pokemon[1]} subisce {damage:.2f} danni! Rimangono {ai_hp:.2f} HP.")

                    if ai_hp <= 0:
                        print(f"{ai_active_pokemon[1]} è stato sconfitto!")
                        ai_team.remove([ai_active_pokemon, ai_active_moves])
                        break
                else:
                    print(f"Il {user_active_pokemon[1]} ha mancato!")

    if not user_team:
        print("\nHai perso la battaglia!")
    elif not ai_team:
        print("\nHai vinto la battaglia!")


# Funzione per simulare una battaglia IA vs IA
def ai_vs_ai_battle(ai_team_1, ai_team_2):
    print("\nBattaglia tra due squadre IA!")

    while ai_team_1 and ai_team_2:
        ai1_active_pokemon, ai1_active_moves = ai_team_1[0]
        ai2_active_pokemon, ai2_active_moves = ai_team_2[0]

        print(f"{ai1_active_pokemon[1]} VS {ai2_active_pokemon[1]}")

        ai1_hp = ai1_active_pokemon[4]
        ai2_hp = ai2_active_pokemon[4]

        while ai1_hp > 0 and ai2_hp > 0:
            ai1_move = select_best_move(ai1_active_moves, ai2_active_pokemon)
            ai2_move = select_best_move(ai2_active_moves, ai1_active_pokemon)

            if ai1_active_pokemon[9] >= ai2_active_pokemon[9]:
                print(f"Il {ai1_active_pokemon[1]} usa {ai1_move[1]}!")
                if does_move_hit(ai1_move[4]):
                    type_effectiveness = calculate_type_advantage(ai1_move[2], ai2_active_pokemon[2], ai2_active_pokemon[3])
                    attack_stat = ai1_active_pokemon[5] if ai1_move[5] == 'fisica' else ai1_active_pokemon[7]
                    defense_stat = ai2_active_pokemon[6] if ai1_move[5] == 'fisica' else ai2_active_pokemon[8]

                    damage = ((2 * 50 / 5 + 2) * ai1_move[3] * (attack_stat / defense_stat) / 50 + 2) * type_effectiveness
                    ai2_hp -= damage
                    ai2_active_pokemon[4] = max(ai2_hp, 0)

                    print(f"{ai2_active_pokemon[1]} subisce {damage:.2f} danni! Rimangono {ai2_hp:.2f} HP.")

                    if ai2_hp <= 0:
                        print(f"{ai2_active_pokemon[1]} è stato sconfitto!")
                        ai_team_2.pop(0)
                        break
                else:
                    print(f"Il {ai1_active_pokemon[1]} ha mancato!")

                print(f"Il {ai2_active_pokemon[1]} usa {ai2_move[1]}!")
                if does_move_hit(ai2_move[4]):
                    type_effectiveness = calculate_type_advantage(ai2_move[2], ai1_active_pokemon[2], ai1_active_pokemon[3])
                    attack_stat = ai2_active_pokemon[5] if ai2_move[5] == 'fisica' else ai2_active_pokemon[7]
                    defense_stat = ai1_active_pokemon[6] if ai2_move[5] == 'fisica' else ai1_active_pokemon[8]

                    damage = ((2 * 50 / 5 + 2) * ai2_move[3] * (attack_stat / defense_stat) / 50 + 2) * type_effectiveness
                    ai1_hp -= damage
                    ai1_active_pokemon[4] = max(ai1_hp, 0)

                    print(f"{ai1_active_pokemon[1]} subisce {damage:.2f} danni! Rimangono {ai1_hp:.2f} HP.")

                    if ai1_hp <= 0:
                        print(f"{ai1_active_pokemon[1]} è stato sconfitto!")
                        ai_team_1.pop(0)
                        break
                else:
                    print(f"Il {ai2_active_pokemon[1]} ha mancato!")

            else:
                print(f"Il {ai2_active_pokemon[1]} usa {ai2_move[1]}!")
                if does_move_hit(ai2_move[4]):
                    type_effectiveness = calculate_type_advantage(ai2_move[2], ai1_active_pokemon[2], ai1_active_pokemon[3])
                    attack_stat = ai2_active_pokemon[5] if ai2_move[5] == 'fisica' else ai2_active_pokemon[7]
                    defense_stat = ai1_active_pokemon[6] if ai2_move[5] == 'fisica' else ai1_active_pokemon[8]

                    damage = ((2 * 50 / 5 + 2) * ai2_move[3] * (attack_stat / defense_stat) / 50 + 2) * type_effectiveness
                    ai1_hp -= damage
                    ai1_active_pokemon[4] = max(ai1_hp, 0)

                    print(f"{ai1_active_pokemon[1]} subisce {damage:.2f} danni! Rimangono {ai1_hp:.2f} HP.")

                    if ai1_hp <= 0:
                        print(f"{ai1_active_pokemon[1]} è stato sconfitto!")
                        ai_team_1.pop(0)
                        break
                else:
                    print(f"Il {ai2_active_pokemon[1]} ha mancato!")

                print(f"Il {ai1_active_pokemon[1]} usa {ai1_move[1]}!")
                if does_move_hit(ai1_move[4]):
                    type_effectiveness = calculate_type_advantage(ai1_move[2], ai2_active_pokemon[2], ai2_active_pokemon[3])
                    attack_stat = ai1_active_pokemon[5] if ai1_move[5] == 'fisica' else ai1_active_pokemon[7]
                    defense_stat = ai2_active_pokemon[6] if ai1_move[5] == 'fisica' else ai2_active_pokemon[8]

                    damage = ((2 * 50 / 5 + 2) * ai1_move[3] * (attack_stat / defense_stat) / 50 + 2) * type_effectiveness
                    ai2_hp -= damage
                    ai2_active_pokemon[4] = max(ai2_hp, 0)

                    print(f"{ai2_active_pokemon[1]} subisce {damage:.2f} danni! Rimangono {ai2_hp:.2f} HP.")

                    if ai2_hp <= 0:
                        print(f"{ai2_active_pokemon[1]} è stato sconfitto!")
                        ai_team_2.pop(0)
                        break
                else:
                    print(f"Il {ai1_active_pokemon[1]} ha mancato!")

    if not ai_team_1:
        print("\nLa seconda squadra IA ha vinto!")
    elif not ai_team_2:
        print("\nLa prima squadra IA ha vinto!")

                    


# Funzione per calcolare l'efficacia di tipo
def calculate_type_advantage(attacking_type, defender_type_1, defender_type_2=None):
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
    calculate_effect(attacking_type, defender_type_1)

    # Check against the second defender type if it exists
    if defender_type_2:
        calculate_effect(attacking_type, defender_type_2)

    return multiplier

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

# Funzione per stampare il team dell'utente
def display_team(team):
    for idx, (pokemon, moves) in enumerate(team):
        print(f"[{idx + 1}] {pokemon[1]} (HP: {pokemon[4]})")
        print("   Mosse:")
        for move in moves:
            print(f"      - {move[1]} (Danno: {move[3]}, Precisione: {move[4]})")

