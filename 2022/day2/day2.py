# https://adventofcode.com/2022/day/2

hand_pts_dict = {"A": 1, "B": 2, "C": 3}
losing_hand = {"A": "B", "B": "C", "C": "A"}
winning_hand = {"A": "C", "B": "A", "C": "B"}
winning_hand_combos = [["C", "A"],["A", "B"],["B", "C"]]
decrypt_hand = {"X": "A", "Y": "B", "Z": "C"}
file = "day2/input.txt"

def calc_outcome(h1, h2):
    if [h1,h2] in winning_hand_combos: return 6
    elif h1 == h2: return 3
    else: return 0

def decrypt_outcome(h1, h2):
    if h2 == "X": return winning_hand[h1]  # lose
    elif h2 == "Z": return losing_hand[h1] # win
    else: return h1 # tie

def part1():
    with open(file, "r") as f:
        score = 0
        for l in f:
            h1, h2 = l.strip().split(" ")
            h2 = decrypt_hand[h2]
            score += hand_pts_dict[h2] + calc_outcome(h1,h2)
    print(score)

def part2():
    with open(file, "r") as f:
        score = 0
        for l in f:
            h1, h2 = l.strip().split(" ")
            h2 = decrypt_outcome(h1, h2)
            score += hand_pts_dict[h2] + calc_outcome(h1,h2)
    print(score)

part1()
part2()