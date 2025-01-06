import random

class VacuumCleaner:
    def __init__(self):
        self.location = random.choice([(0, 0), (0, 1), (1, 0), (1, 1)])
        self.cleaned_cells = set()

    def clean(self, cell):
        print(f"Cleaning cell {cell}")
        self.cleaned_cells.add(cell)

    def move(self, new_location):
        print(f"Moving to {new_location}")
        self.location = new_location

def run_simulation():
    vacuum = VacuumCleaner()
    grid = [(0, 0), (0, 1), (1, 0), (1, 1)]

    while len(vacuum.cleaned_cells) < len(grid):
        dirty_cells = [cell for cell in grid if cell not in vacuum.cleaned_cells]

        if not dirty_cells:
            print("All cells cleaned. Simulation complete.")
            break

        next_cell = random.choice(dirty_cells)
        vacuum.move(next_cell)
        vacuum.clean(next_cell)
        

if __name__ == "__main__":
    run_simulation()

