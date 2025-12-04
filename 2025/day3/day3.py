# https://adventofcode.com/2025/day/3

def read_lines(filename="input.txt"):
    with open(f"2025/day3/{filename}", "r") as f:
        return [line.strip() for line in f.readlines()]

def calculate_largest_joltage(data, num_batteries):
    result = 0
    for bank in data:
        largest = []
        curr_pos = 0
        for max_length in range(num_batteries,0,-1):
            max_digit = 0
            for i in range(curr_pos,len(bank)+1-max_length):
                curr_digit = int(bank[i])
                if bank[i] == '9':
                    max_digit = 9
                    curr_pos = i+1
                    break
                if max_digit < curr_digit:
                    max_digit = curr_digit
                    curr_pos = i+1
            largest.append(str(max_digit))
        result += int("".join(largest))
    return result

def part1():
    data = read_lines()
    print(f"Part 1: {calculate_largest_joltage(data, 2)}")

def part2():
    data = read_lines()
    print(f"Part 2: {calculate_largest_joltage(data, 12)}")

if __name__ == "__main__":
    part1()
    part2()