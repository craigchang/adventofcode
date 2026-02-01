# Advent of Code 2016 - Day 3: Squares With Three Sides

## Problem Overview

You're given a list of triangles specified by their three side lengths. You need to determine how many of these triangles are valid. A triangle is valid if the sum of any two sides is greater than the third side.

## Part 1

**Goal:** Count how many triangles are valid when reading the data horizontally (each line is a triangle).

### Solution Approach

The solution checks each line of input as a separate triangle:

- **Triangle Validation**: A triangle with sides (a, b, c) is valid if:
  - a + b > c
  - a + c > b
  - b + c > a
  
  However, if we sort the sides so that a ≤ b ≤ c, we only need to check: **a + b > c**

- **Algorithm**:
  1. Read each line and parse the three side lengths
  2. For each triangle, sort the sides
  3. Check if the sum of the two smallest sides is greater than the largest side
  4. Count how many triangles pass this test

### Example

For the sample input:
```
101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
```

- Triangle 1: (101, 301, 501) → sorted: (101, 301, 501) → 101 + 301 = 402 < 501 → **Invalid**
- Triangle 2: (102, 302, 502) → sorted: (102, 302, 502) → 102 + 302 = 404 < 502 → **Invalid**
- Triangle 3: (103, 303, 503) → sorted: (103, 303, 503) → 103 + 303 = 406 < 503 → **Invalid**
- Triangle 4: (201, 401, 601) → sorted: (201, 401, 601) → 201 + 401 = 602 > 601 → **Valid**
- Triangle 5: (202, 402, 602) → sorted: (202, 402, 602) → 202 + 402 = 604 > 602 → **Valid**
- Triangle 6: (203, 403, 603) → sorted: (203, 403, 603) → 203 + 403 = 606 > 603 → **Valid**

Result: **3** valid triangles

## Part 2

**Goal:** Count how many triangles are valid when reading the data vertically in groups of 3 rows (each column forms a triangle).

### Solution Approach

The solution reads the data vertically instead of horizontally:

- **Vertical Reading**: Process the input in groups of 3 rows:
  - Group 1: Rows 1-3 → Column 0, Column 1, Column 2 each form a triangle
  - Group 2: Rows 4-6 → Column 0, Column 1, Column 2 each form a triangle
  - And so on...

- **Algorithm**:
  1. Read all lines into a 2D array (preserving original order, not sorted)
  2. Process in groups of 3 rows
  3. For each group, extract the three columns:
     - Column 0: values from row i, row i+1, row i+2
     - Column 1: values from row i, row i+1, row i+2
     - Column 2: values from row i, row i+1, row i+2
  4. Check each column triplet as a triangle using the same validation logic
  5. Count how many triangles pass the test

### Example

For the sample input:
```
101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
```

**Group 1 (rows 1-3):**
- Column 0: (101, 102, 103) → sorted: (101, 102, 103) → 101 + 102 = 203 > 103 → **Valid**
- Column 1: (301, 302, 303) → sorted: (301, 302, 303) → 301 + 302 = 603 > 303 → **Valid**
- Column 2: (501, 502, 503) → sorted: (501, 502, 503) → 501 + 502 = 1003 > 503 → **Valid**

**Group 2 (rows 4-6):**
- Column 0: (201, 202, 203) → sorted: (201, 202, 203) → 201 + 202 = 403 > 203 → **Valid**
- Column 1: (401, 402, 403) → sorted: (401, 402, 403) → 401 + 402 = 803 > 403 → **Valid**
- Column 2: (601, 602, 603) → sorted: (601, 602, 603) → 601 + 602 = 1203 > 603 → **Valid**

Result: **6** valid triangles

## Implementation Details

### Data Structures

- **Input Format**: Each line contains three space-separated integers representing side lengths
- **Triangle Validation**: Uses sorted sides to simplify the check (only need to verify smallest + middle > largest)

### Key Functions

- **`read_lines()`**: Reads input file and parses each line into a list of three integers
- **`isTriangle(s1, s2, s3)`**: 
  - Sorts the three sides
  - Returns 1 if valid triangle (smallest + middle > largest), 0 otherwise

### Code Flow

1. **Part 1**: 
   - Read each line as a triangle
   - Validate each triangle and sum the results

2. **Part 2**: 
   - Read all lines into a 2D array
   - Process in groups of 3 rows
   - For each group, extract columns and validate each column as a triangle
   - Sum all valid triangles

## Notes

- The triangle inequality theorem states: for sides a, b, c, all three conditions must hold:
  - a + b > c
  - a + c > b
  - b + c > a
- However, if we sort the sides, we only need to check the smallest two sum to more than the largest
- Part 2 requires reading the original unsorted data to correctly extract columns vertically
- The solution uses list comprehensions for concise code
