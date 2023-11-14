# Solar Sys Simulation

#### Video Demo: <https://youtu.be/zC4H-ZG-vbM>

#### Description: This project explore the dynamic orbital motion of planets in the Solar System with this captivating Python project using Pygame. Gain insights into gravitational forces governing planetary orbits.

## Overview

Welcome to Solar Sys Simulation, an interactive Python project utilizing the Pygame library to simulate the dynamic orbital motion of planets in my Solar System. This visually engaging application allows users to explore the cosmic dance of celestial bodies, providing insights into the gravitational forces that govern planetary orbits.

The project consists of a main script, `project.py`, serving as the core simulation engine. This script defines the `Planet` class, encapsulating the properties and behaviors of individual planets. Planets are initialized with their positions, radii, colors, masses, and initial velocities. Gravitational interactions and orbital calculations are handled within the `Planet` class.

## Files

### `project.py`

- **Description:** The main script orchestrating the Solar System simulation.
- **Contents:**
  - `Planet` class: Defines the properties and behaviors of planets, including their gravitational interactions and orbital calculations.
  - `main` function: Initializes key celestial bodies, such as the Sun, Earth, Mars, Mercury, and Venus, and orchestrates the simulation loop.

### `test_project.py`

- **Description:** Unit tests for the `Planet` class.
- **Contents:**
  - `test_distance_calculation`: Tests the calculation of the distance between Earth and the Sun.
  - `test_attraction_calculation`: Tests the calculation of gravitational attraction between Earth and the Sun.
  - Add more tests as needed.

## Inspiration

[Gravity Example](https://fiftyexamples.readthedocs.io/en/latest/gravity.html)

## Usage

1. **Install Dependencies:**
   ```bash
   pip install pygame
   pip install pytest
   ```
2. **Run Simulation:**
   ```bash
   py project.py
   ```
