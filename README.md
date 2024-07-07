# Rubik's Cube Simulation

This project is a 3D Rubik's Cube simulation built using Python and the PyRay library. The simulation can generate random movements for the Rubik's Cube and visually display the rotations in a window.



## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)


## Installation

To run this project, you'll need Python 3.x installed on your machine. Follow these steps to set up the environment:

1. **Clone the repository:**
   `git clone https://github.com/Varun-Ajith/Rubik-s-cube-.git`
   `cd Rubik-s-cube-`

2.Create a virtual environment:
  `python -m venv venv`
  `venv\Scripts\activate`

3.Install required dependencies

## Usages
To start the Rubik's Cube simulation, run the following command:
`python dev.py`

This will open a window displaying a 3D Rubik's Cube that performs random movements.

## Project Structure
The project consists of the following files:

`config.py`: Configuration settings for the simulation, including camera settings and predefined Rubik's Cube moves.
`utils.py`: Utility functions used in the project, such as generating random movements.
`rubik.py`: Core classes for the Rubik's Cube (Cube and Rubik), including methods for generating the cube and handling rotations.
`dev.py`: The main script that initializes the PyRay window, sets up the Rubik's Cube, and handles the drawing and updates.
Detailed Breakdown
config.py
Contains configuration settings for the PyRay window, camera, and predefined Rubik's Cube moves. The `rubiks_moves` dictionary maps each move to its corresponding rotation angle, axis, and level.

utils.py
Provides utility functions, including `generate_random_movements(n)`, which generates a queue of random Rubik's Cube movements.

rubik.py
Defines the `Cube` and `Rubik` classes. The `Cube` class represents an individual cube piece with methods for creating its mesh and handling rotations. The `Rubik` class manages a collection of cubes, generates the Rubik's Cube structure, and handles rotations based on the movement queue.

dev.py
The main script that initializes the PyRay window, sets the target FPS, generates random movements, and continuously updates and draws the Rubik's Cube in the window.

## Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
PyRay - Python bindings for raylib, the library used for rendering.
Numpy - Library used for numerical operations and matrix calculations.

