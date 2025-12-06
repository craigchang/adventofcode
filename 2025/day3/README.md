# Day 3: Maximum Joltage Battery Selection

[Problem Link](https://adventofcode.com/2025/day/3)

## Problem Description

Given rows of digits representing battery "banks," select a specific number of batteries from each bank to maximize the resulting joltage value. The batteries must be selected greedily from left to right to form the largest possible number.

### Input Format

Each line is a string of digits representing available batteries in a bank:

```
987654321111111
811111111111119
234234234234278
```

### Part 1: Select 2 Batteries Per Bank

From each bank, select exactly **2 batteries** to create the largest 2-digit number possible using a greedy left-to-right approach.

**Greedy Algorithm:**
1. For the first digit, scan left to right and pick the largest digit (prioritize `9` if found)
2. Once picked, continue from that position + 1
3. For the second digit, pick the largest from the remaining positions
4. Combine to form a 2-digit number

**Example with `987654321111111`:**
- First digit: scan from position 0, find `9` at index 0 → pick `9`, move to position 1
- Second digit: scan from position 1 onwards `87654321111111`, largest is `8` → pick `8`
- Result: `98`

**Example with `811111111111119`:**
- First digit: scan and find `9` at index 14 → pick `9`, move to position 15
- Second digit: only position 15 remains, digit is `9` → pick `9`
- Result: `99`

Sum all 2-digit numbers from all banks to get the final result.

### Part 2: Select 12 Batteries Per Bank

Same greedy approach, but select **12 batteries** from each bank to form a 12-digit number.

**Process:**
1. Repeat the greedy selection 12 times
2. For each iteration, pick the largest available digit from remaining positions
3. Update current position after each pick
4. Combine all 12 digits into a single number

**Key insight:** The algorithm prioritizes finding `9`s early because they maximize the leftmost (most significant) digits.

## Solution Approach

### Core Algorithm: `calculate_largest_joltage(data, num_batteries)`

```python
def calculate_largest_joltage(data, num_batteries):
    result = 0
    
    for bank in data:
        largest = []  # Store selected digits
        curr_pos = 0  # Track starting position for next search
        
        # Select num_batteries digits greedily
        for max_length in range(num_batteries, 0, -1):
            max_digit = 0
            
            # Search from curr_pos to ensure we have enough digits left
            for i in range(curr_pos, len(bank) + 1 - max_length):
                curr_digit = int(bank[i])
                
                # If we find a 9, take it immediately (best possible)
                if bank[i] == '9':
                    max_digit = 9
                    curr_pos = i + 1
                    break
                
                # Otherwise track the maximum digit
                if max_digit < curr_digit:
                    max_digit = curr_digit
                    curr_pos = i + 1
            
            largest.append(str(max_digit))
        
        # Convert selected digits to integer and add to result
        result += int("".join(largest))
    
    return result
```

**Key points:**
- `max_length` counts down from `num_batteries` to 1, tracking how many more digits we need
- `len(bank) + 1 - max_length` ensures we don't search too far (must leave enough digits for future picks)
- Short-circuit on `9`: since 9 is the maximum digit, we can stop searching immediately
- `curr_pos` advances after each pick to avoid reusing batteries

### Part 1 Implementation

```python
def part1():
    data = read_lines()
    # Select 2 batteries per bank
    print(f"Part 1: {calculate_largest_joltage(data, 2)}")
```

### Part 2 Implementation

```python
def part2():
    data = read_lines()
    # Select 12 batteries per bank
    print(f"Part 2: {calculate_largest_joltage(data, 12)}")
```

## Example Walkthrough

**Sample bank: `987654321111111`**

**Part 1 (2 batteries):**
1. First pick (need 2 more):
   - Search positions 0-14 (leave 1 for next pick)
   - Find `9` at position 0 → pick `9`, curr_pos = 1
2. Second pick (need 1 more):
   - Search positions 1-15 (leave 0 for next pick)
   - Largest is `8` at position 1 → pick `8`, curr_pos = 2
3. Result: `98`

**Part 2 (12 batteries):**
1. Pick #1: Find `9` at pos 0 → `9`
2. Pick #2: Find `8` at pos 1 → `8`
3. Pick #3: Find `7` at pos 2 → `7`
4. Pick #4: Find `6` at pos 3 → `6`
5. Pick #5: Find `5` at pos 4 → `5`
6. Pick #6: Find `4` at pos 5 → `4`
7. Pick #7: Find `3` at pos 6 → `3`
8. Pick #8: Find `2` at pos 7 → `2`
9. Pick #9: Find `1` at pos 8 → `1`
10. Pick #10: Find `1` at pos 9 → `1`
11. Pick #11: Find `1` at pos 10 → `1`
12. Pick #12: Find `1` at pos 11 → `1`
- Result: `987654321111`

## Complexity

- **Time:** O(N × B × L) where:
  - N = number of banks (rows)
  - B = batteries to select per bank
  - L = length of each bank string
  - For each battery pick, we scan up to L positions
- **Space:** O(B) for storing selected digits

For Part 1: O(N × 2 × L) = O(N × L)
For Part 2: O(N × 12 × L) = O(N × L)

## Running the Solution

```bash
python 2025/day3/day3.py
```

This will execute both Part 1 and Part 2 using the `input.txt` file.

## Dependencies

This solution uses only Python standard library - no additional packages required.

## Notes

- The greedy approach works because we prioritize the most significant (leftmost) digits
- Finding a `9` early is optimal since no digit can be larger
- The search range calculation `len(bank) + 1 - max_length` ensures we never "run out" of digits for future picks
- Each bank is processed independently, and results are summed
