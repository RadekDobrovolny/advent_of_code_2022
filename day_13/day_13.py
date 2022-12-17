from pprint import pprint


def compare_packets_verbose(p1, p2, level):
  print(f"{level}Compare {p1} vs {p2}")
  for i in range(max(len(p1), len(p2))):
  
    if i > len(p1)-1:
      print(f"{level}Left side ran out of items, so inputs are in the right order")
      return True
    if i > len(p2)-1:
      print(f"{level}Right side ran out of items, so inputs are not in the right order")
      return False
      
    print(f"{level}Compare {p1[i]} vs {p2[i]}")
    
    if type(p1[i]) == type(p2[i]):

      if isinstance(p1[i], int):
        if p1[i] < p2[i]:
          print(f"  {level}Left side is smaller, so inputs are in the right order")
          return True
        if p1[i] > p2[i]:
          print(f"  {level}Right side is smaller, so inputs are not in the right order")
          return False

      if isinstance(p1[i], list):
        res = compare_packets_verbose(p1[i], p2[i], "  "+level)
        if res != "continue":
          return res

    else:
      if isinstance(p1[i], int):
        print(f"{level}Mixed types; convert left to [{p1[i]}] and retry comparison")
        res = compare_packets_verbose([p1[i]], p2[i], "  "+level)
        if res != "continue":
          return res
      if isinstance(p2[i], int):
        print(f"{level}Mixed types; convert right to [{p2[i]}] and retry comparison")
        res = compare_packets_verbose(p1[i], [p2[i]], "  "+level)
        if res != "continue":
          return res
  
  return "continue"


def compare_packets(p1, p2):
  for i in range(max(len(p1), len(p2))):
    if i > len(p1)-1:
      return True
    if i > len(p2)-1:
      return False
    
    if type(p1[i]) == type(p2[i]):
      if isinstance(p1[i], int):
        if p1[i] < p2[i]:
          return True
        if p1[i] > p2[i]:
          return False

      if isinstance(p1[i], list):
        res = compare_packets(p1[i], p2[i])
        if res != "continue":
          return res

    else:
      if isinstance(p1[i], int):
        res = compare_packets([p1[i]], p2[i])
        if res != "continue":
          return res
      if isinstance(p2[i], int):
        res = compare_packets(p1[i], [p2[i]])
        if res != "continue":
          return res
  
  return "continue"


def first_part(lines):
  pair_index = 0
  sum = 0
  while lines:
    pair_index += 1
    packets_1 = eval(lines.pop(0).strip())
    packets_2 = eval(lines.pop(0).strip())
    if len(lines) > 1:
      lines.pop(0)
  
    print(f"== Pair {pair_index} ==")
    if compare_packets_verbose(packets_1, packets_2, "  - "):
      sum += pair_index
    print(f"sum: {sum}")
    print("")

def second_part(lines):
  data = []
  for line in lines:
    if line.strip():
      data.append(eval(line.strip()))
  data.append([[2]])
  data.append([[6]])

  for j in range(len(data)):
    # print(j)
    for i in range(len(data))[j:]:
      if not compare_packets(data[j], data[i]):
        swap = data[j]
        data[j] = data[i]
        data[i] = swap
  # pprint(data)

  product = 1
  for i in range(len(data)):
    if data[i] in [ [[2]], [[6]] ]:
      product *= i+1
  print(product)

input_file = open('./day_13/input.txt')
lines = input_file.readlines()

# first_part(lines)
second_part(lines)

