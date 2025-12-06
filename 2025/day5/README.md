# Day 5: Fresh ID Ranges

[Problem Link](https://adventofcode.com/2025/day/5)

## Problem Description

Given a list of "fresh" ID ranges and individual available IDs, determine which IDs are fresh and calculate the total number of fresh IDs across all ranges.

### Input Format

The input contains two types of lines:
1. **Range lines**: `start-end` format (inclusive ranges of fresh IDs)
2. **Individual ID lines**: Single numbers (available IDs to check)

**Example:**
```
3-5
10-14
16-20
12-18

1
5
8
11
17
32
```

Fresh ID ranges: `[3-5]`, `[10-14]`, `[16-20]`, `[12-18]`
Available IDs to check: `1, 5, 8, 11, 17, 32`

### Part 1: Count Fresh Available IDs

Count how many of the available IDs fall within any of the fresh ID ranges.

**Example:**
- ID `1`: Not in any range ✗
- ID `5`: In range `[3-5]` ✓
- ID `8`: Not in any range ✗
- ID `11`: In range `[10-14]` ✓
- ID `17`: In ranges `[16-20]` and `[12-18]` (overlapping) ✓
- ID `32`: Not in any range ✗

Result: 3 fresh IDs (5, 11, 17)

### Part 2: Total Count of Fresh IDs

Calculate the total number of unique fresh IDs across all ranges, handling overlaps correctly.

**Key challenge:** Ranges may overlap, so we need to merge overlapping ranges to avoid counting IDs multiple times.

**Example with overlapping ranges:**
```
[3-5]    → IDs: 3, 4, 5 (count: 3)
[10-14]  → IDs: 10, 11, 12, 13, 14 (count: 5)
[16-20]  → IDs: 16, 17, 18, 19, 20 (count: 5)
[12-18]  → IDs: 12, 13, 14, 15, 16, 17, 18 (count: 7)
```

Ranges `[10-14]` and `[12-18]` overlap on IDs 12, 13, 14.
Ranges `[16-20]` and `[12-18]` overlap on IDs 16, 17, 18.

After merging overlaps:
- `[3-5]` → 3 IDs
- `[10-20]` (merged from `[10-14]`, `[12-18]`, `[16-20]`) → 11 IDs

Total: 3 + 11 = 14 unique fresh IDs

## Solution Approach

### Input Parsing: `read_file(filename)`

```python
def read_file(filename="input.txt"):
    fresh_ranges_IDs = []
    available_IDs = []
    
    with open(f"2025/day5/{filename}", "r") as f:
        for r in f.readlines():
            if not r.strip():
                continue
            
            # Lines with "-" are ranges
            if r and "-" in r:
                fresh_ranges_IDs.append(tuple(map(int, r.strip().split("-"))))
            # Lines without "-" are individual IDs
            elif r and "-" not in r:
                available_IDs.append(int(r.strip()))
    
    return fresh_ranges_IDs, available_IDs
```

**Key points:**
- Separates ranges from individual IDs based on presence of `-`
- Returns two lists: ranges (as tuples) and individual IDs

### Part 1: Check Individual IDs

```python
def is_id_fresh(fresh_ranges_IDs, current_id):
    """Check if an ID falls within any fresh range."""
    for start, end in fresh_ranges_IDs:
        if start <= current_id and current_id <= end:
            return True
    return False

def part1():
    fresh_IDs, available_IDs = read_file()
    # Count how many available IDs are fresh
    result = sum([1 for id in available_IDs if is_id_fresh(fresh_IDs, id)])
    print(f"Part 1: {result}")
```

**Key points:**
- Simple linear search through all ranges
- An ID is fresh if it falls within any range (inclusive bounds)
- Use list comprehension with sum to count matches

### Part 2: Merge Overlapping Ranges

```python
def calc_fresh_ids(fresh_IDs: list):
    merged_IDs = []
    
    for f_start, f_end in fresh_IDs:
        m_min, m_max = float('inf'), 0
        removed = set()
        overlapped = False
        
        for m_start, m_end in merged_IDs:
            # Case 1: Current range is completely contained in merged range
            if m_start <= f_start and f_end <= m_end:
                overlapped = True
                break
            
            # Case 2: Current range completely contains a merged range
            elif f_start <= m_start and m_end <= f_end:
                m_min, m_max = f_start, f_end
                removed.add((m_start, m_end))
            
            # Case 3: Partial overlap on the right
            elif m_start <= f_start and f_start <= m_end and f_end > m_end:
                m_min = min(m_start, m_min)
                m_max = max(f_end, m_max)
                removed.add((m_start, m_end))
            
            # Case 4: Partial overlap on the left
            elif m_start <= f_end and f_end <= m_end and f_start < m_start:
                m_min = min(f_start, m_min)
                m_max = max(m_end, m_max)
                removed.add((m_start, m_end))
        
        # Add new merged range or original range
        if len(removed) > 0:
            for r in removed:
                merged_IDs.remove(r)
            merged_IDs.append((m_min, m_max))
        elif not overlapped:
            merged_IDs.append((f_start, f_end))
    
    # Calculate total IDs in all merged ranges
    return sum([end - start + 1 for start, end in merged_IDs])
```

**Key points:**
- Iteratively merge ranges with the list of already-merged ranges
- Handle 4 overlap cases:
  1. **Completely contained**: Current range is already covered → skip
  2. **Completely contains**: Current range subsumes a merged range → replace
  3. **Partial right overlap**: Extend merged range to the right
  4. **Partial left overlap**: Extend merged range to the left
- Remove old ranges that were merged and add the new merged range
- Count total IDs: `end - start + 1` for each range (inclusive)

### Overlap Cases Illustrated

```
Case 1: Completely contained (skip)
  Merged:  [====10-20====]
  Current:    [12-15]
  Result:  [====10-20====]

Case 2: Completely contains (replace)
  Merged:     [12-15]
  Current: [====10-20====]
  Result:  [====10-20====]

Case 3: Partial right overlap (extend right)
  Merged:  [====10-15====]
  Current:      [====14-20====]
  Result:  [====10-20====]

Case 4: Partial left overlap (extend left)
  Merged:       [====15-20====]
  Current: [====10-16====]
  Result:  [====10-20====]
```

## Complexity

- **Part 1:** O(N × R) where N = number of available IDs, R = number of ranges
- **Part 2:** O(R²) where R = number of ranges (each range checks against all merged ranges)
  - In worst case with no overlaps: O(R²) comparisons
  - With many overlaps: fewer comparisons as ranges merge

## Running the Solution

```bash
python 2025/day5/day5.py
```

This will execute both Part 1 and Part 2 using the `input.txt` file.

## Dependencies

This solution uses only Python standard library - no additional packages required.

## Notes

- Ranges are inclusive on both ends: `[start, end]`
- The merge algorithm processes ranges one at a time, maintaining a list of non-overlapping merged ranges
- Part 2 doesn't need the individual available IDs - it counts all IDs in the ranges
- The solution handles edge cases like adjacent ranges (e.g., `[10-15]` and `[16-20]`) as separate non-overlapping ranges
