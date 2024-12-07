# https://adventofcode.com/2024/day/7

def ternary(n):
  if n == 0:
    return '0'
  res = ''
  while n > 0:
    res = str(n % 3) + res
    n //= 3
  return res

def generate_operations(num_ops, nums_len, binary=True):
  ops_list = list()
  if binary:
    for i in range(num_ops):
      ops_list.append(bin(i)[2:].zfill(nums_len))
  else:
    for i in range(num_ops):        
      op = ternary(i).zfill(nums_len)
      if '2' in op:
        ops_list.append(op)
  return ops_list

def evaluate_equation(eq, val, ops_list, valid_eqs):
  for ops in ops_list:
    res = eq[0]
    i = 1
    for op in ops:
      if op == '0':
        res += eq[i]
      elif op == '1':
        res *= eq[i]
      else:
        res = int(str(res) + str(eq[i]))
      i += 1
    if val == res:
      valid_eqs.append(val)
      return val
  return 0

def read_file():
  eqs = list()
  with open("2024/day7/input.txt", "r") as f:
    for l in f.readlines():
      val, eq = l.strip().split(": ")
      val, eq = int(val), list(map(int, eq.split(" ")))
      eqs.append((val,eq))
  return eqs

def main():
  eqs = read_file()
  total = 0
  valid_eqs = list()

  # part 1
  for val, nums in eqs:
    nums_len = len(nums) - 1
    ops = generate_operations(pow(2, nums_len), nums_len)
    total += evaluate_equation(nums, val, ops, valid_eqs)
  print(total)

  # part 2
  for val, nums in eqs:
    if val in valid_eqs: # already true
      continue
    nums_len = len(nums) - 1
    ops = generate_operations(pow(3, nums_len), nums_len, False)
    total += evaluate_equation(nums, val, ops, valid_eqs)
  print(total)

main()