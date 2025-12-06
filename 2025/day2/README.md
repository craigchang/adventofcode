# Day 2: Repeated Digit Patterns

[Problem Link](https://adventofcode.com/2025/day/2)

## Problem Description

Given a comma-separated list of number ranges, find all numbers within those ranges that match specific repeated digit patterns and sum them up.

### Input Format

The input is a single line containing comma-separated ranges in the format `start-end`:

```
11-22,95-115,998-1012,1188511880-1188511890
```

Each range represents an inclusive interval `[start, end]` to search.

### Part 1: Two-Part Repeated Patterns

Find all numbers that consist of **exactly two identical halves**.

**Pattern:** The number must be formed by repeating a sequence of digits exactly twice.

**Examples of valid numbers:**
- `1212` → "12" repeated twice ✓
- `123123` → "123" repeated twice ✓
- `9999` → "99" repeated twice ✓
- `11` → "1" repeated twice ✓

**Examples of invalid numbers:**
- `123` → cannot be split into two equal halves ✗
- `1213` → halves don't match ("12" ≠ "13") ✗
- `121212` → three repetitions, not two ✗

**Regex pattern:** `^(\d+)\1$`
- `(\d+)` captures the first half (one or more digits)
- `\1` matches exactly the same digits again
- `^` and `$` ensure the entire number matches (no extra digits)

### Part 2: Multi-Part Repeated Patterns

Find all numbers that consist of **two or more identical repetitions** of a digit sequence.

**Pattern:** The number must be formed by repeating a sequence of digits at least twice (can be more).

**Examples of valid numbers:**
- `11` → "1" repeated 2 times ✓
- `1212` → "12" repeated 2 times ✓
- `121212` → "12" repeated 3 times ✓
- `999999` → "9" repeated 6 times (or "99" × 3, or "999" × 2) ✓
- `123123123` → "123" repeated 3 times ✓

**Examples of invalid numbers:**
- `123` → no repetition ✗
- `1213` → pattern doesn't repeat ✗

**Regex pattern:** `^(\d+)\1+$`
- `(\d+)` captures the repeating unit
- `\1+` matches one or more additional repetitions of the same unit
- `^` and `$` ensure the entire number matches

**Key difference from Part 1:** Part 2 accepts numbers with 2+ repetitions, while Part 1 requires exactly 2.

## Solution Approach

### Part 1 Implementation

```python
def part1():
    ranges = read_input().split(",")
    result = 0
    
    for r in ranges:
        # Parse range endpoints
        firstID, lastID = r.split("-")
        
        # Check every number in range [firstID, lastID]
        for id in range(int(firstID), int(lastID) + 1):
            # Check if number has exactly two identical halves
            if re.match(r"^(\d+)\1$", str(id)):
                result += id
    
    return result
```

**Key points:**
- Split input by commas to get individual ranges
- For each range, iterate through all integers inclusively
- Use regex `^(\d+)\1$` to match numbers with exactly 2 repetitions
- Sum all matching numbers

**Example with sample range `11-22`:**
- Check 11: `"11"` → matches `^(\d+)\1$` as "1" repeated twice → add 11
- Check 12-21: none match the pattern
- Check 22: `"22"` → matches as "2" repeated twice → add 22
- Subtotal: 11 + 22 = 33

### Part 2 Implementation

```python
def part2():
    ranges = read_input().split(",")
    result = 0
    
    for r in ranges:
        firstID, lastID = r.split("-")
        
        for id in range(int(firstID), int(lastID) + 1):
            # Check if number has 2+ identical repetitions
            if re.match(r"^(\d+)\1+$", str(id)):
                result += id
    
    return result
```

**Key points:**
- Same structure as Part 1
- Use regex `^(\d+)\1+$` to match numbers with 2 or more repetitions
- The `+` after `\1` allows multiple additional repetitions (not just one)

**Example with sample range `11-22`:**
- Check 11: `"11"` → matches → add 11
- Check 22: `"22"` → matches → add 22
- Subtotal: 11 + 22 = 33 (same as Part 1 since no 3+ repetitions exist)

**Example with range `95-115`:**
- 101: `"101"` → "1" appears 3 times, but not consecutive: 1-0-1 ✗
- 111: `"111"` → matches as "1" repeated 3 times ✓ → add 111

### Understanding the Regex Patterns

**Part 1: `^(\d+)\1$`**
```
For "1212":
  (\d+) captures "12"
  \1 matches "12" again
  Result: full match ✓

For "121212":
  (\d+) captures "12"
  \1 matches the next "12"
  But "12" remains unmatched
  Result: no match ✗
```

**Part 2: `^(\d+)\1+$`**
```
For "1212":
  (\d+) captures "12"
  \1+ matches one more "12"
  Result: full match ✓

For "121212":
  (\d+) captures "12"
  \1+ matches "12" twice more
  Result: full match ✓
```

## Complexity

- **Time:** O(N × M) where N = total numbers across all ranges, M = average digit length
  - Regex matching on a string of length M
- **Space:** O(M) for converting numbers to strings

For large ranges (like `8989806846-8989985017`), this can be slow but works for the problem constraints.

## Running the Solution

```bash
python 2025/day2/day2.py
```

This will execute both Part 1 and Part 2 using the `input.txt` file.

## Dependencies

This solution uses Python's standard `re` module for regular expressions - no additional packages required.

## Notes

- Numbers are converted to strings for regex matching
- Ranges are inclusive on both ends: `[start, end]`
- The solution iterates through potentially large ranges, which may take time for billion-scale ranges
