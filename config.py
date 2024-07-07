import pyray as pr
import numpy as np

rubiks_moves = {
    'U': (np.radians(90), np.array([0, 1, 0]), 2),
    'U\'': (np.radians(-90), np.array([0, 1, 0]), 2),
    'D': (np.radians(90), np.array([0, 1, 0]), 0),
    'D\'': (np.radians(-90), np.array([0, 1, 0]), 0),
    'L': (np.radians(90), np.array([1, 0, 0]), 0),
    'L\'': (np.radians(-90), np.array([1, 0, 0]), 0),
    'R': (np.radians(90), np.array([1, 0, 0]), 2),
    'R\'': (np.radians(-90), np.array([1, 0, 0]), 2),
    'F': (np.radians(90), np.array([0, 0, 1]), 2),
    'F\'': (np.radians(-90), np.array([0, 0, 1]), 2),
    'B': (np.radians(90), np.array([0, 0, 1]), 0),
    'B\'': (np.radians(-90), np.array([0, 0, 1]), 0)
}

window_w, window_h = 600, 450
fps = 60

camera = pr.Camera3D(
    [18.0, 16.0, 18.0],  # Position of the camera
    [0.0, 0.0, 0.0],     # Target it looks at
    [0.0, 1.0, 0.0],     # Up vector (rotation towards target)
    45.0,                # Field-of-view Y
    0                    # Camera type
)
