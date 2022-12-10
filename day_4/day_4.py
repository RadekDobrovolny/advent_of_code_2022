input_file = open('./day_4/input.txt')
lines = input_file.readlines()

def create_set(rng):
  i, j = rng.split("-")
  s = set(range(int(i), int(j) + 1))
  return s

count = 0
overlap = 0

for line in lines:
  range1, range2 = line.split(",")
  set1 = create_set(range1)
  set2 = create_set(range2)

  if set2.issubset(set1):
    count += 1
  elif set1.issubset(set2):
    count += 1

  if set1.intersection(set2):
    overlap += 1

print(f"{count}")
print(f"{overlap}")