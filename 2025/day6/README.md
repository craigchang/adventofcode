# Day 6: Column Calculations

[Problem Link](https://adventofcode.com/2025/day/6)

## Problem Description

Given a grid of numbers and a row of operations at the bottom, perform column-wise arithmetic operations.

### Input Format

The input consists of:
- Multiple rows of space-separated numbers (possibly with varying spacing)
- A final row containing operation symbols (`+` or `*`)

Each column of numbers corresponds to one operation symbol in the same column position.

### Part 1: Simple Column Operations

For each column:
1. Extract all numbers in that column
2. Apply the corresponding operation (`+` for sum, `*` for product)
3. Add the result to the total

**Example (from sample.txt):**
```
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + 
```

- Column 0: `[123, 45, 6]` with `*` → `123 × 45 × 6 = 33,210`
- Column 1: `[328, 64, 98]` with `+` → `328 + 64 + 98 = 490`
- Column 2: `[51, 387, 215]` with `*` → `51 × 387 × 215 = 4,245,645`
- Column 3: `[64, 23, 314]` with `+` → `64 + 23 + 314 = 401`

Total: `33,210 + 490 + 4,245,645 + 401 = 4,279,746`

### Part 2: Multi-Digit Numbers Across Columns

In Part 2, numbers can span multiple columns. Spaces indicate column boundaries for multi-digit numbers.

For each group of non-space columns:
1. Concatenate the digits vertically to form complete numbers
2. When you hit a column of all spaces (or reach the end), apply the operation to all accumulated numbers
3. Move to the next operation for the next group

**Example interpretation:**
```
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + 
```

Reading column-by-column:
- Columns 0-2 form numbers: `"123"+"45"+"6"` → `[123, 45, 6]`
- Apply operation at index 0 (`*`): `123 × 45 × 6 = 33,210`
- Column 3 is spaces → separator
- Columns 4-6 form numbers: `"328"+"64"+"98"` → `[328, 64, 98]`
- Apply operation at index 1 (`+`): `328 + 64 + 98 = 490`
- And so on...

The key difference from Part 1 is recognizing when columns group together to form multi-digit numbers.

## Solution Approach

### Part 1 Implementation

```python
def part1():
    data = read_lines()
    # Parse rows as integers (space-separated)
    nums = [list(map(int, row.strip().split())) for row in data[:-1]]
    # Get operation symbols
    ops = data[-1].strip().split()
    
    result = 0
    for x in range(len(nums[0])):  # Iterate over columns
        col = [nums[y][x] for y in range(len(nums))]  # Extract column
        # Apply sum or product based on operation
        result += sum(col) if ops[x] == '+' else mult(col)
    
    return result
```

**Key points:**
- Parse each row by splitting on spaces and converting to integers
- Extract columns by iterating over the same index in each row
- Use a helper `mult()` function (via `functools.reduce`) for products
- Accumulate results based on operation type

### Part 2 Implementation

```python
def part2():
    data = read_lines()
    # Keep rows as character lists to detect spaces
    nums = [list(row) for row in data[:-1]]
    ops = data[-1].strip().split()
    
    result = 0
    op_index = 0
    num_list = []
    
    for x in range(len(nums[0])):  # Iterate over columns
        col = [nums[y][x] for y in range(len(nums))]
        
        # If column has digits, construct numbers vertically
        if col.count(" ") != len(col):
            num_list.append(int("".join(col)))
        
        # If column is all spaces OR end of line, apply operation
        if col.count(" ") == len(col) or x == len(nums[0]) - 1:
            result += sum(num_list) if ops[op_index] == '+' else mult(num_list)
            num_list = []
            op_index += 1
    
    return result
```

**Key points:**
- Keep input as character lists (not parsed as ints) to detect space columns
- Build multi-digit numbers by joining column characters vertically
- Detect group boundaries: columns of all spaces or end of input
- Accumulate numbers within a group, then apply operation when group ends
- Track operation index separately from column index

### Helper Functions

```python
def mult(iterable):
    """Compute product of all elements in iterable."""
    return reduce(lambda x, y: x * y, iterable)
```

## Complexity

- **Time:** O(R × C) where R = number of rows, C = number of columns
- **Space:** O(R × C) for storing the grid

Both parts scan the grid once with simple operations per cell.

## Running the Solution

```bash
python 2025/day6/day6.py
```

This will execute both Part 1 and Part 2 using the `input.txt` file.
