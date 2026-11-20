import random
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

# Look Ma, no random import!

# class Player:
#     # ... __init__ stays exactly the same ...

#     # We add a 'move_index' parameter so the user can choose the direction
#     def make_move(self, move_index: int) -> tuple[int, int]:
#         # 1. YOU manually pull the exact move from the list using an index
#         dx, dy = self.moves[move_index]
        
#         # 2. YOU do the math (exactly as you did before)
#         x, y = self.position
#         new_x = x + dx
#         new_y = y + dy
        
#         # 3. Update state
#         self.position = (new_x, new_y)
#         self.path.append(self.position)
#         return self.position


    def make_move(self):
        dx, dy = random.choice(self.moves)
        x, y = self.position
        new_x = x + dx
        new_y = y + dy
        self.position = (new_x, new_y)
        self.path.append(self.position)
        return self.position


    @abstractmethod
    def level_up(self)-> None:
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()

        self.moves = [
            (0,1),
            (0,-1),
            (1, 0),
            (-1, 0)
        ]

    def level_up(self)-> None:
        diagonal_moves = [
            (1, 1),
            (-1, 1),
            (1, -1),
            (-1, -1)
        ]
        self.moves.extend(diagonal_moves)

# if __name__ == '__main__':
#     print("--- Test Case 1: Initializing the Pawn ---")
#     pawn = Pawn()
#     print(f"Initial Position: {pawn.position}")  # Expected: (0, 0)
#     print(f"Initial Path: {pawn.path}")          # Expected: [(0, 0)]
#     print(f"Starting Move Count: {len(pawn.moves)} moves available.") # Expected: 4 moves

#     print("\n--- Test Case 2: Making Initial Moves (Cardinal Directions) ---")
#     # Make 3 moves to see the position change dynamically
#     for i in range(1, 4):
#         new_pos = pawn.make_move()
#         print(f"Move #{i} landed on: {new_pos}")
    
#     print(f"Updated Tracking Path: {pawn.path}") 
#     # Expected: A list of 4 total tuples starting with (0,0)

#     print("\n--- Test Case 3: Leveling Up (Unlocking Diagonal Moves) ---")
#     print(f"Moves before level up: {pawn.moves}")
#     pawn.level_up()
#     print(f"Moves after level up: {pawn.moves}")
#     print(f"New Move Count: {len(pawn.moves)} moves available.") # Expected: 8 moves

#     print("\n--- Test Case 4: Testing Post-Level Up Movement ---")
#     # Make a few more moves to ensure the new diagonal math works smoothly
#     for i in range(4, 7):
#         print(f"Move #{i} landed on: {pawn.make_move()}")

#     print(f"\nFinal Complete Tracking Path: {pawn.path}")

if __name__ == '__main__':
    print("--- Test Case 1: Initializing the Pawn ---")
    pawn = Pawn()
    print(f"Initial Position: {pawn.position}")  # Expected: (0, 0)
    print(f"Initial Path: {pawn.path}")          # Expected: [(0, 0)]
    print(f"Starting Move Count: {len(pawn.moves)} moves available.") # Expected: 4 moves

    print("\n--- Test Case 2: Making Initial Moves (Cardinal Directions) ---")
    # Make 3 moves to see the position change dynamically
    for i in range(1, 4):
        new_pos = pawn.make_move()
        print(f"Move #{i} landed on: {new_pos}")
    
    print(f"Updated Tracking Path: {pawn.path}") 
    # Expected: A list of 4 total tuples starting with (0,0)

    print("\n--- Test Case 3: Leveling Up (Unlocking Diagonal Moves) ---")
    print(f"Moves before level up: {pawn.moves}")
    pawn.level_up()
    print(f"Moves after level up: {pawn.moves}")
    print(f"New Move Count: {len(pawn.moves)} moves available.") # Expected: 8 moves

    print("\n--- Test Case 4: Testing Post-Level Up Movement ---")
    # Make a few more moves to ensure the new diagonal math works smoothly
    for i in range(4, 7):
        print(f"Move #{i} landed on: {pawn.make_move()}")

    print(f"\nFinal Complete Tracking Path: {pawn.path}")
