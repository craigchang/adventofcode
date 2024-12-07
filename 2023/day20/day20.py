# https://adventofcode.com/2023/day/20

import re

op_map = dict()
modules_map = dict()

def read_file(filepath) -> dict:
  configs = dict()
  with open(filepath, 'r') as f:
    for l in f.readlines():
      m, dest = re.findall("(.*) -> (.*)", l.strip())[0]
      if '%' in m or '&' in m:
        op_map[m[1:]] = m[0]
        modules_map[m[1:]] = False
        configs[m[1:]] = [m[0]] + dest.split(", ")
      else:
        configs[m] = dest.split(", ")
  return configs

def send_pulse(configs, module, pulse):
  print(module, pulse)
  next_module = configs[module][1]
  op = op_map[next_module]

  if op == "%":
    if pulse == 'H':
      return
    else: # pulse == 'L'
      pulse = 'H' if pulse == 'L' else 'L'
      modules_map[next_module] = not modules_map[next_module]
      send_pulse(configs, configs[next_module][1], pulse)
  elif op == "&":
    if pulse == 'H':
      send_pulse(configs, next_module, 'L')
    else:
      send_pulse(configs, next_module, 'H')
  

  # if next_op == "%":
  #   if pulse == 'H' and configs[next_module][0] == '%': # do nothing
  #     return
  #   elif configs[next_module][0] == '&':
  #     send_pulse(configs, modules_dict, configs[next_module][1], configs[next_module][0], pulse)
  #   else: # if low pulse
  #     pulse = 'H' if pulse == 'L' else 'L'
  #     modules_dict[module] = not modules_dict[module]
  #     send_pulse(configs, modules_dict, next_module, next_op, pulse)
  # elif op == "&":
  #   if pulse == 'H':
  #     send_pulse(configs, modules_dict, next_module, next_op, 'L')
  #   else:
  #     send_pulse(configs, modules_dict, next_module, next_op, 'H')
  
  return

def main():
  configs = read_file("day20/sample.txt")
  init = "broadcaster"
  modules_dict = dict()
  print(configs)
  print(op_map)


  pulse = "L"
  for module in configs["broadcaster"]:
    if pulse == "L":
      modules_dict[module] = True
      send_pulse(configs, module, 'H')




  # while(True):
  #   dest = configs[init]
  #   for d in dest[1:]:
  #     op = dest[0]
  #     modules[d] = d





  


main()