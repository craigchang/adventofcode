# Day 4: Toilet Paper Roll Removal

[Problem Link](https://adventofcode.com/2025/day/4)

## Problem Description

Given a grid containing toilet paper rolls (represented by `@`) and empty spaces (`.`), remove rolls based on their neighboring roll count.

### Input Format

A grid where:
- `@` = toilet paper roll
- `.` = empty space

```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
```

### Part 1: Single Removal Pass

Remove all rolls that have **fewer than 4 adjacent rolls** (in any of the 8 directions: up, down, left, right, and 4 diagonals). Count how many rolls are removed in this single pass.

**Adjacent directions (8 total):**
```
(-1,-1)  (-1,0)  (-1,1)
( 0,-1)    @     ( 0,1)
( 1,-1)  ( 1,0)  ( 1,1)
```

**Example:**
```
..@@.
@@@.@
```

For the roll at position (0,2) marked with `*`:
```
..@*.
@@@.@
```
- Check all 8 adjacent positions
- Count adjacent `@` symbols:
  - Position (0,3): `@` ✓
  - Position (1,2): `@` ✓
  - Position (1,3): `.` ✗
  - Other positions: out of bounds or empty
- Total: 2 adjacent rolls
- Since 2 < 4, this roll would be removed

**Rule:** Only rolls with **4 or more** adjacent rolls survive.

### Part 2: Iterative Removal

Repeatedly apply the removal process until no more rolls can be removed. Count the total number of rolls removed across all iterations.

**Process:**
1. Apply Part 1 removal logic (remove rolls with < 4 neighbors)
2. Update the grid by replacing removed rolls with `.`
3. Repeat until no rolls are removed in a pass
4. Sum all removed rolls across all iterations

**Key insight:** Removing rolls changes the neighbor counts for remaining rolls, potentially causing more rolls to become removable in subsequent iterations.

**Example cascade:**
```
Initial:
@@@@@
@@@@@
@@@@@

Iteration 1: Corner and edge rolls have < 4 neighbors, removed
..@..
.@@@.
..@..

Iteration 2: All remaining rolls now have < 4 neighbors, removed
.....
.....
.....
```

## Solution Approach

### Core Function: `remove_rolls(grid)`

```python
def remove_rolls(grid):
    col_len, row_len = len(grid[0]), len(grid)
    result = 0
    removed_rolls = []
    
    # Check every position in the grid
    for y in range(row_len):
        for x in range(col_len):
            if grid[y][x] == '@':
                rolls = 0
                
                # Count adjacent rolls in all 8 directions
                for dx, dy in ADJ:
                    if is_within_boundary(x, dx, y, dy, col_len, row_len):
                        if grid[y+dy][x+dx] == '@':
                            rolls += 1
                
                # Mark for removal if < 4 neighbors
                if rolls < 4:
                    result += 1
                    removed_rolls.append((y, x))
    
    # Actually remove the rolls from grid
    for (y, x) in removed_rolls:
        grid[y][x] = '.'
    
    return result
```

**Key points:**
- Two-pass approach: first identify removable rolls, then remove them
- This prevents the removal of one roll from affecting the neighbor count of others in the same pass
- Returns the count of removed rolls
- Modifies the grid in-place

### Helper Function: `is_within_boundary(x, dx, y, dy, col_len, row_len)`

```python
def is_within_boundary(x, dx, y, dy, col_len, row_len):
    """Check if position (x+dx, y+dy) is within grid bounds."""
    return 0 <= x+dx and x+dx < col_len and 0 <= y+dy and y+dy < row_len
```

Prevents out-of-bounds access when checking neighbors near grid edges.

### Part 1 Implementation

```python
def part1():
    # Create a mutable copy of the grid
    grid = [list(row) for row in read_lines()]
    
    # Single removal pass
    print(f"Part 1: {remove_rolls(grid)}")
```

**Key point:** Converts strings to lists of characters for in-place modification.

### Part 2 Implementation

```python
def part2():
    grid = [list(row) for row in read_lines()]
    result = 0
    
    # Keep removing until no more rolls can be removed
    while True:
        rolls = remove_rolls(grid)
        if rolls == 0:
            break
        result += rolls
    
    print(f"Part 2: {result}")
```

**Key points:**
- Loop until `remove_rolls` returns 0 (no removals)
- Accumulate total removed rolls across all iterations
- Grid state is updated after each iteration

## Example Walkthrough

**Sample (simplified):**
```
@@@
@@@
@@@
```

**Part 1:**
- Center roll (1,1): 8 neighbors → keep
- Edge rolls (e.g., 0,1): 5 neighbors → keep
- Corner rolls (e.g., 0,0): 3 neighbors → remove (3 < 4)
- Result: 4 corner rolls removed

**Part 2:**
```
Iteration 1: Remove 4 corner rolls
.@.
@@@
.@.

Iteration 2: All remaining rolls now have < 4 neighbors
- Roll (0,1): 2 neighbors → remove
- Roll (1,0): 2 neighbors → remove
- Roll (1,1): 4 neighbors → keep (but only temporarily)
- Roll (1,2): 2 neighbors → remove
- Roll (2,1): 2 neighbors → remove
Result so far: 4 + 4 = 8

Iteration 3: Only center roll remains
...
.@.
...
- Roll (1,1): 0 neighbors → remove
Final result: 4 + 4 + 1 = 9 (all rolls removed)
```

## Complexity

- **Time:** 
  - Part 1: O(R × C) where R = rows, C = columns (single pass)
  - Part 2: O(K × R × C) where K = number of iterations until stable
- **Space:** O(R × C) for storing the grid

In worst case, Part 2 could require O(R × C) iterations if rolls are removed one at a time from the outside in.

## Running the Solution

```bash
python 2025/day4/day4.py
```

This will execute both Part 1 and Part 2 using the `input.txt` file.

## Dependencies

This solution uses only Python standard library - no additional packages required.

## Notes

- The two-pass approach in `remove_rolls` ensures all removals in an iteration are based on the same grid state
- Rolls are identified by coordinates `(y, x)` where y is row and x is column
- The grid is modified in-place for efficiency
- Part 2's iterative nature simulates a "cascading" removal effect
