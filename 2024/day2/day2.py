# https://adventofcode.com/2024/day/2

def isReportSafe(r: list):
  isInc = r[1] - r[0] > 0
  for i in range(len(r) - 1):
    diff = r[i+1] - r[i]
    if not (abs(diff) >= 1 and abs(diff) <= 3 and ((diff > 0 != isInc) or (diff < 0 == isInc))):
      return False
    isInc = diff > 0
  return True

def isReportSafeAfterRemoval(r: list):
  for i in range(len(r)):
    temp = r[:]
    temp.pop(i)
    if isReportSafe(temp):
      return True
  return False

def readFile():
  with open("2024/day2/input.txt", "r") as f:
    reports = list()
    for l in f.readlines():
      reports.append(list(map(int, l.strip().split())))
    return reports
  
def part1():
  reports = readFile()
  print(sum([1 for r in reports if isReportSafe(r)]))

def part2():
  reports = readFile()
  print(sum([1 for r in reports if isReportSafe(r) or isReportSafeAfterRemoval(r)]))

part1()
part2()