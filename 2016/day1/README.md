# Advent of Code 2016 - Day 1: No Time for a Taxicab

## Problem Overview

You're following a series of instructions to navigate a grid. Each instruction consists of a turn direction (L for left, R for right) followed by a number of blocks to move in that direction.

## Part 1

**Goal:** After following all instructions, calculate the Manhattan distance from the starting point (0, 0).

### Solution Approach

The solution uses a direction-based navigation system:

- **Direction Index System**: Uses an index (0-3) to represent the four cardinal directions:
  - 0 = North (0, 1)
  - 1 = East (1, 0)
  - 2 = South (0, -1)
  - 3 = West (-1, 0)

- **Key Functions**:
  - `calcDirection(dir, dir_index)`: Updates the direction index based on L/R turn
    - R (right): increment index (wraps around with modulo 4)
    - L (left): decrement index (wraps around with modulo 4)
  - `calcDistance(distance, dir_index, coords)`: Moves the specified distance in the current direction

- **Algorithm**:
  1. Start at (0, 0) facing North (direction index 0)
  2. For each instruction:
     - Extract the turn direction (L or R) and distance
     - Update direction based on the turn
     - Move the specified distance in the new direction
  3. Calculate Manhattan distance: `|x| + |y|`

### Example

For the sample input `R8, R4, R4, R8`:
- Start: (0, 0), facing North
- R8: Turn right (now East), move 8 blocks → (8, 0)
- R4: Turn right (now South), move 4 blocks → (8, -4)
- R4: Turn right (now West), move 4 blocks → (4, -4)
- R8: Turn right (now North), move 8 blocks → (4, 4)
- Distance: |4| + |4| = 8

## Part 2

**Goal:** Find the first location visited twice and return its Manhattan distance from the starting point.

### Solution Approach

The solution tracks all visited locations during the path:

- **Key Function**: `calcPath(distance, dir_index, coords, locations)`
  - Tracks each intermediate step along the path (not just the final destination)
  - Checks if any location has been visited before
  - Returns `(True, location)` if a duplicate is found, otherwise `(False, new_coords)`

- **Algorithm**:
  1. Start at (0, 0) with a set containing the starting location
  2. For each instruction:
     - Update direction based on the turn
     - Step through each block one at a time, checking if that location was visited before
     - If a duplicate is found, immediately return its Manhattan distance
     - Otherwise, add each new location to the visited set

### Example

For the sample input `R8, R4, R4, R8`:
- The path visits: (0,0) → (8,0) → (8,-4) → (4,-4) → (4,4)
- When moving R8 from (4,-4) to (4,4), the path goes through (4,-3), (4,-2), (4,-1), (4,0), (4,1), (4,2), (4,3), (4,4)
- Location (4,0) was already visited during the first R8 move, so the answer is |4| + |0| = 4

## Implementation Details

### Data Structures

- **STEPS**: Tuple of tuples representing direction vectors
  ```python
  STEPS = ((0,1), (1,0), (0,-1), (-1,0))  # N, E, S, W
  ```

- **locations**: Set of visited coordinates (x, y) tuples

### Code Flow

1. **Input Parsing**: Reads instructions from file, splits by comma and space
2. **Part 1**: Simple navigation without tracking visited locations
3. **Part 2**: Enhanced navigation that tracks and checks for duplicate visits

## Notes

- The solution uses modular arithmetic to handle direction wrapping (turning right from West wraps to North)
- Part 2 checks intermediate steps, not just final destinations, to find the first duplicate visit
- Manhattan distance is calculated as the sum of absolute x and y coordinates
