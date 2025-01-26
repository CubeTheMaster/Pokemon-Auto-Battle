import random

#Function to cheek if a move hits
def does_move_hit(accuracy):
    return random.randint(1, 100) <= accuracy