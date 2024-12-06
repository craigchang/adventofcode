# https://adventofcode.com/2024/day/5

def sort_comparator(x,y, ord_rules, rev_rules):
  if y in ord_rules and x in ord_rules[y] and x in rev_rules and y in rev_rules[x]:
    return 1
  elif x in ord_rules and y in ord_rules[x] and y in rev_rules and x in rev_rules[y]:
    return -1
  return 0

def is_update_ordered(update, in_ord_rules, rev_ord_rules):
  for i in range(len(update)):
    curr = update[i]
    for j in range(len(update)):
      if i == j:
        continue
      elif i < j:
        if curr in in_ord_rules and update[j] not in in_ord_rules[curr]: # check curr num in order
          return False
      elif j < i:
        if curr in rev_ord_rules and update[j] not in rev_ord_rules[curr]: # check curr num in rev order
          return False
  return True

def main():
  ord_rules = dict()
  rev_rules = dict()
  updates = []
  with open("2024/day5/sample.txt", "r") as f:
    for line in f.readlines():
      line = line.strip()
      if '|' in line:
        before, after = map(int, line.split('|'))
        if before not in ord_rules:
          ord_rules[before] = [after]
        else:
          ord_rules[before].append(after)
        if after not in rev_rules:
          rev_rules[after] = [before]
        else:
          rev_rules[after].append(before)
      elif not line:
        continue
      else:
        updates.append(list(map(int,line.split(','))))

  unordered_updates = []
  total = 0
  for u in updates:
    if is_update_ordered(u, ord_rules, rev_rules):
      total += u[len(u)//2]
    else:
      unordered_updates.append(u)
  print("Part 1:", total)

  total = 0
  for u in unordered_updates:
    for i in range(len(u)):
      for j in range(len(u)):
        if i == j:
          continue
        elif i < j:
          if u[j] in ord_rules and u[i] in ord_rules[u[j]] and u[i] in rev_rules and u[j] in rev_rules[u[i]]:
            u[i], u[j] = u[j], u[i]
        elif j < i:
          if u[i] in ord_rules and u[j] in ord_rules[u[i]] and u[j] in rev_rules and u[i] in rev_rules[u[j]]:
            u[i], u[j] = u[j], u[i]
    total += u[len(u)//2]

  print("Part 2:", total)

main()