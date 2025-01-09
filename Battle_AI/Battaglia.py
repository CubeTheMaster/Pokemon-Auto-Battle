


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