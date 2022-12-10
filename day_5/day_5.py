import re

def init_setup(cargo_crane):
  cargo_crane.append(["F", "L", "M", "W"])
  cargo_crane.append(["F", "M", "V", "Z", "B"])
  cargo_crane.append(["Q", "L", "S", "R", "V", "H"])
  cargo_crane.append(["J", "T", "M", "P", "Q", "V", "S", "F"])
  cargo_crane.append(["W", "L", "S"])
  cargo_crane.append(["W", "J", "R", "M", "P", "V", "F"])
  cargo_crane.append(["F", "R", "N", "P", "C", "Q", "J"])
  cargo_crane.append(["B", "R", "W", "Z", "S", "P", "H", "V"])
  cargo_crane.append(["W", "Z", "H", "G", "C", "J", "M", "B"])

def get_tops(cargo_crane):
  s = []
  for line in cargo_crane:
    if len(line):
      s.append(line[0])
    else:
      s.append(" ")
  return "".join(s)

def move(cargo_crane, count, frm, to):
  for _ in range(count):
    if cargo_crane[frm - 1]:
      crane = cargo_crane[frm - 1].pop(0)
      cargo_crane[to - 1].insert(0, crane)

def move_9001(cargo_crane, count, frm, to):
  stack = []
  for _ in range(count):
    if cargo_crane[frm - 1]:
      stack += cargo_crane[frm - 1].pop(0)
  cargo_crane[to - 1] = stack + cargo_crane[to - 1]

cargo_crane = []
init_setup(cargo_crane)

input_file = open('./day_5/input.txt')
lines = input_file.readlines()

for line in lines[10:]:
  count, frm, to = re.findall(r'\d+', line)
  move_9001(cargo_crane, int(count), int(frm), int(to))

print(get_tops(cargo_crane))
