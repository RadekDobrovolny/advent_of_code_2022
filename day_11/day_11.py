from pprint import pprint

monkeys = {}
product = 1

def read_data():
  input_file = open('./day_11/input.txt')
  lines = input_file.readlines()

  monkey = 0
  for line in lines:
    line = line.strip()

    # Read monkey number
    if "Monkey" in line:
      monkey = int(line[-2])
      monkeys.update({monkey: {}})

    # Read items
    if "Starting items" in line:
      _, item_row = line.split(": ")
      items = [int(i) for i in item_row.split(", ")]
      monkeys.get(monkey).update({"items": items})

    # Read operation
    if "Operation" in line:
      _, operation = line.split(": new = ")
      monkeys.get(monkey).update({"operation": operation})

    # Read test divisible
    if "Test: divisible by" in line:
      test_div = int(line.split(" ")[-1])
      monkeys.get(monkey).update({"divisible": test_div})

    # Read test true
    if "If true" in line:
      if_true = int(line.split(" ")[-1])
      monkeys.get(monkey).update({"true": if_true})

    # Read test false
    if "If false" in line:
      if_false = int(line.split(" ")[-1])
      monkeys.get(monkey).update({"false": if_false})

    # Add counter
    monkeys.get(monkey).update({"counter": 0})


def monkey_business():
  for m in range(len(monkeys)):
    monkey = monkeys.get(m)
    while monkey.get("items"):
      monkey.update({"counter": monkey.get("counter") + 1})
      old = monkey.get("items").pop(0)
      worry = eval(monkey.get("operation")) % product
      # worry = worry // 3

      divisible = not worry % monkey.get("divisible")

      if divisible:
        monkeys.get(monkey.get("true")).get("items").append(worry)
      else:
        monkeys.get(monkey.get("false")).get("items").append(worry)
  

read_data()

product_list = []
for m in monkeys.items():
  product_list.append(m[1].get("divisible"))

for p in product_list:
  product *= p

for i in range(10_000):
  # print(i)
  monkey_business()

pprint("")
pprint(monkeys)

counters = []
for m in monkeys.items():
  counters.append(m[1].get("counter"))
print(counters)

l1 = max(counters)
counters.remove(l1)
l2 = max(counters)
print(f"{l1 * l2}")
