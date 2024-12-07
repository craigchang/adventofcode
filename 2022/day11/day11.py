# https://adventofcode.com/2022/day/11

import re

operator_dict = {
  '+': lambda x,y: x + y,
  '*': lambda x,y: x * y
}

class Monkey:
  def __init__(self) -> None:
    self.items = []
    self.op = lambda: None
    self.operator = ''
    self.val = 0
    self.test = lambda: None
    self.test_true = 0
    self.test_false = 0
    self.num_inspected = 0
  def __lt__(self, other):
    return self.num_inspected < other.num_inspected

def create_op_lambda(op, val):
  if op == "+":
    if val != "old":
      return lambda old: old + val
    else:
      return lambda old: old + old
  else:
    if val != "old":
      return lambda old: old * val
    else:
      return lambda old: old * old

def create_test_lambda(val):
  return lambda x: x % int(val) == 0

def parse_file():
  monkeys = []
  monkey = None

  with open("day11/sample.txt", "r") as f:
    for line in f:
      line = line.strip()
      if line.startswith("Monkey"):
        monkey = Monkey()
        continue
      elif line.startswith("Starting items:"):
        items = [int(num) for num in re.search("Starting items: (.*)", line).groups()[0].split(", ")]
        monkey.items = items
        continue
      elif line.startswith("Operation:"):
        oper = re.search("Operation: new = old (\*|\+) (.+)", line).groups()
        val = "old" if oper[1] == "old" else int(oper[1])
        monkey.operator = oper[0]
        monkey.val = int(val) if val != "old" else "old"
        monkey.op = create_op_lambda(oper[0], val)
      elif line.startswith("Test:"):
        div = re.search("Test: divisible by (\d+)", line).groups()[0]
        monkey.test = create_test_lambda(div)
      elif line.startswith("If true"):
        test_true = re.search("If true: throw to monkey (\d+)", line).groups()[0]
        monkey.test_true = int(test_true)
      elif line.startswith("If false"):
        test_false = re.search("If false: throw to monkey (\d+)", line).groups()[0]
        monkey.test_false = int(test_false)
      else:
        monkeys.append(monkey)
        continue
    monkeys.append(monkey)
  return monkeys

def calculate_monkey_business(monkeys: list, rounds: int, part1: bool):
  for round in range(1, rounds):
    for monkey in monkeys:
      for item in monkey.items:
        worry_level = 0
        if part1:
          worry_level = monkey.op(item) // 3
        else:
          worry_level = monkey.op(item)

          # if monkey.val == "old":
          #   val = item
          # else:
          #   val = monkey.val

          # if not (monkey.operator == "*" and item / val % val == 0):
          #   worry_level = monkey.op(item)
          # else:
          #   worry_level = item


        if monkey.test(worry_level):
          monkeys[monkey.test_true].items.append(worry_level)
        else:
          monkeys[monkey.test_false].items.append(worry_level)
        monkey.num_inspected += 1
      monkey.items = []
    
    print("Round", round)
    for monkey in monkeys:
        print(monkey.items, monkey.num_inspected)
    # if round in [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]:
    #   for monkey in monkeys:
    #     print(monkey.items, monkey.num_inspected)

  monkeys.sort(reverse=True)

  return monkeys[0].num_inspected * monkeys[1].num_inspected

def main():
  # part 1
  # monkeys = parse_file()
  # print(calculate_monkey_business(monkeys.copy(), 21, True))

  # part 2
  monkeys = parse_file()
  print(calculate_monkey_business(monkeys.copy(), 21, False))


  
main()