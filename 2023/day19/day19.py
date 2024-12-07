# https://adventofcode.com/2023/day/19

import re

def read_file(filepath):
  with open(filepath, 'r') as f:
    flow_map = dict()
    ratings = []
    for l in f.readlines():
      l = l.strip()
      if not l:
        continue
      if not l.startswith("{"):
        flow_id, expr = re.findall("(.+){(.+)}", l)[0]
        flow_map[flow_id] = expr.split(",")
      else:
        x, m, a, s = map(int, re.findall("{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", l)[0])
        ratings.append([x,m,a,s])
    return flow_map, ratings

def evaluate_expression(expr: str, vals: list):
  x,m,a,s = vals
  return expr.startswith('x') and eval(expr.replace('x', str(x))) or \
    expr.startswith('m') and eval(expr.replace('m', str(m))) or \
    expr.startswith('a') and eval(expr.replace('a', str(a))) or \
    expr.startswith('s') and eval(expr.replace('s', str(s)))

def evaluate_workflow(flow_map: dict, flow_id: str, vals: list):
  while True:
    for f in flow_map[flow_id]:
      if ":" in f:
        expr, dest = f.split(":")
        if evaluate_expression(expr, vals):
          if dest in ('A', 'R'):
            return sum(vals) if dest == 'A' else 0
          else:
            flow_id = dest
          break
      else:
        dest = f
        if dest in ('A', 'R'):
            return sum(vals) if dest == 'A' else 0
        else:
          flow_id = dest
        break

def part1():
  flow_map, ratings = read_file("day19/input.txt")
  result = 0
  for x,m,a,s in ratings:
    result += evaluate_workflow(flow_map, 'in', [x,m,a,s])
  print(result)

def part2():
  flow_map, ratings = read_file("day19/sample.txt")
  accepted = 0
  ll = []
  for i in range(1,4001):
    for j in range(1,4001):
      for k in range(1,4001):
        for l in range(1,4001):
          result = evaluate_workflow(flow_map, 'in', [i,j,k,l])
          if result:
            accepted += 1
            #print(i,j,k,l)
          else:
            print(i,j,k,l, 'R')
            return
  print(accepted)


part1()
part2()