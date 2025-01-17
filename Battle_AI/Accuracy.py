import random

def does_move_hit(accuracy):
    """
    Check if a move hits or not.
    
    :param accuracy: Move accuracy.
    :return: True if the move hits.
    """
    return random.randint(1, 100) <= accuracy