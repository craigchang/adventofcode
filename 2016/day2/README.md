# Advent of Code 2016 - Day 2: Bathroom Security

## Problem Overview

You're trying to unlock a bathroom door by following instructions on a keypad. Each line of instructions tells you how to move (U/D/L/R) from your current position, and you need to press the button you end up on after each line.

## Part 1

**Goal:** Find the bathroom code using a standard 3×3 numeric keypad.

### Keypad Layout (Part 1)
```
1 2 3
4 5 6
7 8 9
```

### Solution Approach

The solution uses a coordinate-based navigation system on a 3×3 grid:

- **Starting Position**: (1, 1) which corresponds to button '5' on the keypad
- **Keypad Representation**: 2D array `keypad[y][x]` where:
  - y=0: row with buttons 1,2,3
  - y=1: row with buttons 4,5,6
  - y=2: row with buttons 7,8,9

- **Movement Constraints**: 
  - Can only move if the new position stays within bounds (0 ≤ x ≤ 2, 0 ≤ y ≤ 2)
  - Each direction (U/D/L/R) is checked independently

- **Algorithm**:
  1. Start at position (1, 1) - button '5'
  2. For each line of instructions:
     - For each direction character (U/D/L/R):
       - Calculate the new position
       - If the new x-coordinate is valid (0-2), update x
       - If the new y-coordinate is valid (0-2), update y
     - After processing all directions in the line, append the button at current position to result
  3. Return the concatenated sequence of buttons

### Example

For the sample input:
```
ULL
RRDDD
LURDL
UUUUD
```

- Start at (1,1) = '5'
- ULL: U → (1,0) = '2', L → (0,0) = '1', L → (0,0) = '1' (can't go left) → **'1'**
- RRDDD: R → (1,0) = '2', R → (2,0) = '3', D → (2,1) = '6', D → (2,2) = '9', D → (2,2) = '9' (can't go down) → **'9'**
- LURDL: L → (1,2) = '8', U → (1,1) = '5', R → (2,1) = '6', D → (2,2) = '9', L → (1,2) = '8' → **'8'**
- UUUUD: U → (1,1) = '5', U → (1,0) = '2', U → (1,0) = '2' (can't go up), U → (1,0) = '2', D → (1,1) = '5' → **'5'**

Result: **1985**

## Part 2

**Goal:** Find the bathroom code using a diamond-shaped keypad layout.

### Keypad Layout (Part 2)
```
    1
  2 3 4
5 6 7 8 9
  A B C
    D
```

### Solution Approach

The solution uses a similar coordinate-based system but with a 5×5 grid and special handling:

- **Starting Position**: (0, 2) which corresponds to button '5'
- **Keypad Representation**: 5×5 array `keypad2[y][x]` where:
  - Invalid positions are marked with '0'
  - Valid buttons are: 1,2,3,4,5,6,7,8,9,A,B,C,D

- **Movement Constraints**: 
  - Can only move if the new position is within bounds (0 ≤ x ≤ 4, 0 ≤ y ≤ 4)
  - **AND** the target position must not be '0' (invalid keypad position)
  - Each direction (U/D/L/R) is checked independently

- **Algorithm**:
  1. Start at position (0, 2) - button '5'
  2. For each line of instructions:
     - For each direction character (U/D/L/R):
       - Calculate the new x position
       - If new x is valid AND the target keypad position is not '0', update x
       - Calculate the new y position  
       - If new y is valid AND the target keypad position is not '0', update y
     - After processing all directions in the line, append the button at current position to result
  3. Return the concatenated sequence of buttons

### Example

For the sample input:
```
ULL
RRDDD
LURDL
UUUUD
```

- Start at (0,2) = '5'
- ULL: U → (0,1) = '2', L → (0,1) = '2' (can't go left, would hit '0'), L → (0,1) = '2' → **'2'**
- RRDDD: R → (1,1) = '3', R → (2,1) = '4', D → (2,2) = '8', D → (2,3) = 'C', D → (2,3) = 'C' (can't go down) → **'C'**
- LURDL: L → (1,3) = 'B', U → (1,2) = '7', R → (2,2) = '8', D → (2,3) = 'C', L → (1,3) = 'B' → **'B'**
- UUUUD: U → (1,2) = '7', U → (1,1) = '3', U → (1,0) = '1', U → (1,0) = '1' (can't go up), D → (1,1) = '3' → **'3'**

Result: **5DB3**

## Implementation Details

### Data Structures

- **STEPS**: Dictionary mapping direction characters to coordinate deltas
  ```python
  STEPS = {
      "U": (0, -1),  # Move up (decrease y)
      "R": (1, 0),   # Move right (increase x)
      "D": (0, 1),   # Move down (increase y)
      "L": (-1, 0)   # Move left (decrease x)
  }
  ```

- **keypad**: 3×3 array for Part 1
- **keypad2**: 5×5 array for Part 2 (with '0' for invalid positions)

### Code Flow

1. **Input Parsing**: Reads lines from file, each line is a sequence of direction instructions
2. **Part 1**: Navigate on 3×3 keypad starting at (1,1)
3. **Part 2**: Navigate on 5×5 diamond keypad starting at (0,2), checking for '0' invalid positions

## Notes

- The solution checks x and y movements independently, which means you can move in one direction even if you can't move in the other
- Part 2 uses '0' as a sentinel value to mark invalid keypad positions
- The coordinate system uses (x, y) where x is the column and y is the row, matching array indexing `keypad[y][x]`
