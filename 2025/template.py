# https://adventofcode.com/2025/day/X

def read_input(filename="input.txt"):
    """Read and parse the input file."""
    with open(f"2025/dayX/{filename}", "r") as f:
        return f.read().strip()

def read_lines(filename="input.txt"):
    """Read input file as list of lines."""
    with open(f"2025/dayX/{filename}", "r") as f:
        return [line.strip() for line in f.readlines()]

def part1():
    """Solve part 1."""
    data = read_input()
    # TODO: Implement solution
    result = 0
    print(f"Part 1: {result}")
    return result

def part2():
    """Solve part 2."""
    data = read_input()
    # TODO: Implement solution
    result = 0
    print(f"Part 2: {result}")
    return result

if __name__ == "__main__":
    part1()
    part2()
