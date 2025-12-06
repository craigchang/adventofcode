# Day 1: Circular Track Rotations

[Problem Link](https://adventofcode.com/2025/day/1)

## Problem Description

You're tracking positions on a circular track with 100 positions (0-99). Starting at position 50, you process a series of rotation instructions that move you around the circle.

### Input Format

Each line contains:
- A rotation direction: `L` (left/counterclockwise) or `R` (right/clockwise)
- A distance to move: a positive integer

**Example:**
```
L68  → Move left (counterclockwise) 68 positions
R30  → Move right (clockwise) 30 positions
L5   → Move left 5 positions
```

### Part 1: Count Passes Through Position 0

Starting at position 50:
1. Process each instruction to update your position
2. Handle wrapping: positions < 0 add 100, positions ≥ 100 subtract 100
3. Count how many times you land exactly on position 0

**Key insight:** The track is circular with 100 positions (0-99), so movement wraps around.

**Example walkthrough (sample.txt):**
```
Start: position 50

L68 → 50 - 68 = -18 → wrap: -18 + 100 = 82
R30 → 82 + 30 = 112 → wrap: 112 - 100 = 12
L5  → 12 - 5 = 7
R60 → 7 + 60 = 67
L55 → 67 - 55 = 12
L1  → 12 - 1 = 11
L99 → 11 - 99 = -88 → wrap: -88 + 100 = 12
R14 → 12 + 14 = 26
L82 → 26 - 82 = -56 → wrap: -56 + 100 = 44
```

Count how many times the position equals 0.

### Part 2: Count Full Revolutions

Track not just passes through position 0, but count **every full revolution** around the circle.

A revolution occurs when:
1. Your position goes through the 0/100 boundary (wrapping around)
2. You land exactly on position 0 or 100

**Key differences from Part 1:**
- Count every wrap operation (each time you add/subtract 100)
- Track the "current position" vs "final position" to detect boundary crossings
- Special handling when crossing from positive to negative side (checking if within one revolution)

**Example logic:**
- If you're at position 20 and move L68 → position becomes -48
  - This requires one wrap (+100) → 52
  - Count 1 revolution
- If you're at position 90 and move R30 → position becomes 120
  - This requires one wrap (-100) → 20
  - Count 1 revolution
- Landing exactly on 0 or 100 also counts as passing through the boundary

## Solution Approach

### Part 1 Implementation

```python
def part1():
    data = read_lines("input.txt")
    old_pos = 50  # Starting position
    result = 0
    
    for r in data:
        # Calculate movement distance (negative for L, positive for R)
        old_pos += calc_distance(r)
        
        # Wrap position to stay in range [0, 99]
        while old_pos < 0:
            old_pos += 100
        while old_pos >= 100:
            old_pos -= 100
        
        # Count if we land on position 0
        if old_pos == 0:
            result += 1
    
    return result
```

**Key points:**
- `calc_distance()` returns positive for `R` (right), negative for `L` (left)
- Simple wrapping: add 100 if negative, subtract 100 if >= 100
- Only count exact landings on position 0

### Part 2 Implementation

```python
def part2():
    data = read_lines()
    curr_pos = 50  # Track current position
    final_pos = 50  # Calculate final position after move
    result = 0
    
    for r in data:
        final_pos += calc_distance(r)
        
        # Handle negative wraps (counterclockwise revolutions)
        while final_pos < 0:
            # Check if we're within one revolution of original position
            if -99 <= final_pos < 0:
                final_pos += 100
                if curr_pos > 0:
                    result += 1
            else:
                # Multiple revolutions needed
                final_pos += 100
                result += 1
        
        # Handle positive wraps (clockwise revolutions)
        while final_pos > 100:
            result += 1
            final_pos -= 100
        
        # Landing on boundary (0 or 100) counts as crossing
        if final_pos == 0 or final_pos == 100:
            final_pos = 0
            result += 1
        
        curr_pos = final_pos  # Update current position
    
    return result
```

**Key points:**
- Track both current and final positions to detect boundary crossings
- Each wrap operation counts as one revolution
- Special case: when going negative, check if within one revolution (`-99 <= final_pos < 0`)
- Landing on 0 or 100 (boundary positions) counts as a crossing
- Update `curr_pos` after each instruction to maintain state

### Helper Function

```python
def calc_distance(data):
    """Parse instruction and return signed distance.
    
    Returns:
        Positive distance for R (right/clockwise)
        Negative distance for L (left/counterclockwise)
    """
    rotation, distance = re.findall(r"([LR])(\d+)", data)[0]
    distance = int(distance)
    return distance if rotation == "R" else -distance
```

## Complexity

- **Time:** O(N × M) where N = number of instructions, M = average wraps per instruction
  - In practice, M is small (usually 1-2 wraps per instruction)
- **Space:** O(N) for storing input lines

## Running the Solution

```bash
python 2025/day1/day1.py
```

This will execute both Part 1 and Part 2 using the `input.txt` file.

## Dependencies

This solution uses Python's standard `re` module for regular expressions - no additional packages required.
