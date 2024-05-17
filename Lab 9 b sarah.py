#Lab 9 b
#SARAH PANDIT
#sarah57codes

# Let's read the content of the files 'lecture 17.py' and 'lecture 18.py' to understand their contents and how they might relate to agent-based simulation.
file_path_17 = '/mnt/data/lecture 17.py'
file_path_18 = '/mnt/data/lecture 18.py'

with open(file_path_17, 'r') as file:
    content_17 = file.read()

with open(file_path_18, 'r') as file:
    content_18 = file.read()

content_17, content_18


import random

class Agent:
    def __init__(self, name):
        self.name = name

    def find_empty_patch(self, grid):
        """Find an empty patch in the grid."""
        empty_patches = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == 0]
        return random.choice(empty_patches) if empty_patches else None

    def move(self, grid, new_position):
        """Move the agent to a new position in the grid."""
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == self.name:
                    grid[i][j] = 0  # Clear the old position
        if new_position:
            grid[new_position[0]][new_position[1]] = self.name
        return grid

class World:
    def __init__(self, size=5, num_agents=2):
        self.grid = [[0]*size for _ in range(size)]  # Initialize a grid with zeros
        self.agents = [Agent(chr(65+i)) for i in range(num_agents)]  # Name agents as 'A', 'B', ...
        # Place each agent at a random initial position
        for agent in self.agents:
            while True:
                x, y = random.randint(0, size-1), random.randint(0, size-1)
                if self.grid[x][y] == 0:
                    self.grid[x][y] = agent.name
                    break

    def run_simulation(self, num_iterations=10):
        for _ in range(num_iterations):
            for agent in self.agents:
                new_position = agent.find_empty_patch(self.grid)
                self.grid = agent.move(self.grid, new_position)
            self.display_grid()

    def display_grid(self):
        for row in self.grid:
            print(" ".join(str(x) for x in row))
        print()

def main():
    world = World(size=5, num_agents=3)
    world.run_simulation(num_iterations=5)

if __name__ == "__main__":
    main()
