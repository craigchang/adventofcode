#!/usr/bin/env python3
"""
Script to create a new day folder structure for Advent of Code 2025.

Usage:
    python create_day.py <day_number>
    
Example:
    python create_day.py 1
"""

import os
import sys

def create_day_structure(day_num):
    """Create folder structure for a new day."""
    day_folder = f"day{day_num}"
    base_path = os.path.join("2025", day_folder)
    
    # Create day folder
    os.makedirs(base_path, exist_ok=True)
    
    # Create dayX.py from template
    template_content = f"""# https://adventofcode.com/2025/day/{day_num}

def read_input(filename="input.txt"):
    \"\"\"Read and parse the input file.\"\"\"
    with open(f"2025/{day_folder}/{{filename}}", "r") as f:
        return f.read().strip()

def read_lines(filename="input.txt"):
    \"\"\"Read input file as list of lines.\"\"\"
    with open(f"2025/{day_folder}/{{filename}}", "r") as f:
        return [line.strip() for line in f.readlines()]

def part1():
    \"\"\"Solve part 1.\"\"\"
    data = read_input()
    # TODO: Implement solution
    result = 0
    print(f"Part 1: {{result}}")
    return result

def part2():
    \"\"\"Solve part 2.\"\"\"
    data = read_input()
    # TODO: Implement solution
    result = 0
    print(f"Part 2: {{result}}")
    return result

if __name__ == "__main__":
    part1()
    part2()
"""
    
    # Write the Python file
    py_file = os.path.join(base_path, f"day{day_num}.py")
    with open(py_file, "w") as f:
        f.write(template_content)
    
    # Create empty input.txt
    input_file = os.path.join(base_path, "input.txt")
    with open(input_file, "w") as f:
        f.write("")
    
    # Create empty sample.txt
    sample_file = os.path.join(base_path, "sample.txt")
    with open(sample_file, "w") as f:
        f.write("")
    
    print(f"✅ Created structure for Day {day_num}")
    print(f"   📁 {base_path}/")
    print(f"   📄 {py_file}")
    print(f"   📄 {input_file}")
    print(f"   📄 {sample_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_day.py <day_number>")
        print("Example: python create_day.py 1")
        sys.exit(1)
    
    try:
        day = int(sys.argv[1])
        if day < 1 or day > 25:
            print("Day must be between 1 and 25")
            sys.exit(1)
        create_day_structure(day)
    except ValueError:
        print("Day must be a valid number")
        sys.exit(1)
