# AI Vacuum Cleaner Simulator





https://github.com/user-attachments/assets/a09277fd-90c1-4f1b-b0de-3a761d8b83fe



## Overview
The **AI Vacuum Cleaner Simulator** is a simulation project that demonstrates the use of artificial intelligence to control a virtual vacuum cleaner. The goal is for the AI agent to clean a grid-based environment efficiently by navigating obstacles, detecting dirt, and optimising its path. This project showcases techniques in AI, pathfinding, and environment interaction.

---

## Controls
- `Set Grid Size`: Initialises a new environment size based on the user's width/height input.
- `Reset`: Initialises a new environment and restarts the simulation.
- `Next`: Advances the vacuum cleaner to the next step in its path.
- `Manual Vacuum Placement`: Hold the `V` button and click on the desired grid location to place the vacuum cleaner.
- `Run`: Automates the cleaning process with a one-second step interval.
- `Search Type Dropdown`: Chooses the algorithm for path planning.


---

## Features
- **Grid-based Environment**: A simulated space with dirt and obstacles.
- **Customisable Settings**: Adjust the size of the grid, dirt location, and obstacle placement.
- **Manual Vacuum Placement**: Hold the `V` button and click on the desired grid location to place the vacuum cleaner.
- **AI Algorithms**: Implementations of various search and decision-making algorithms, including:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Uniform Cost Search (UCS)
  - Greedy Best-First Search
  - A* Search
- **Dynamic Environment**: Obstacles and dirt positions can be randomised.
- **Visualisation**: A graphical representation of the environment and the vacuum cleaner's movement.
  - **Colour Key**:
    - **Red squares**: Obstacles that the vacuum cleaner must navigate around.
    - **Grey squares**: Dirt that requires cleaning.
    - **Green square**: Vacuum cleaner.
    - **Orange path**: The planned path taken by the vacuum cleaner, based on the selected search algorithm.
    - **Pink squares**: Explored areas during pathfinding process.
    - **White squares**: Clean areas in the environment.
- **Steps Counter**: Counts and displays the number of steps the vacuum performs.
- **Complete Error Handling**: Ensures no invalid user inputs for grid size, the vacuum cleaner cannot be placed on a red grid (obstacle). 



---


## Usage
- **Start**: Launch the simulator.
- **Customise grid size**: Modify the grid size at the top of GUI window.
- **Customise environment**: Add/remove dirt and obstacles by clicking on the grids.
- **Vacuum Placement**: Hold the `V` button and click on the desired location within the grid.
- **Select Algorithm**: Select an AI algorithm via the dropdown menu at the bottom of the GUI window.
- **Experiment**: Click the `Run` button to start the vacuum cleaner movement.

---

## File Structure
```
AI-Vacuum-Cleaner-Simulator/
├── vacuum_cleaner_main.py     # Grid-based vacuum search
├── utilities.py               # Provides utility functions
├── search_algorithms.py       # Implements search algorithms
├── agents_and_environments.py # Defines vacuum agent behavior
├── vacuum_icon.ico            # Vacuum icon for GUI window
├── README.md                  # Documentation

```

---








