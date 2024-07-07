import config
import numpy as np

def generate_random_movements(n):
    rotation_queue = []
    for _ in range(n):
        action = np.random.choice(list(config.rubiks_moves.keys()))
        rotation_queue.append(config.rubiks_moves[action])
    return rotation_queue
