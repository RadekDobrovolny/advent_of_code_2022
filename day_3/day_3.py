input_file = open('./day_3/input.txt')
lines = input_file.readlines()

def get_value(s):
  if s.islower():
    return ord(s) - ord("a") + 1
  else:
    return ord(s) - ord("A") + 27
  

def get_priority(s):
  p1 = s[slice(0, len(s)//2)]
  p2 = s[slice(len(s)//2, len(s))]

  same = [v for v in p1 if v in p2]

  return get_value(same[0])

score = 0
for line in lines:
  score += get_priority(line.strip())

print(f"{score}")

i = 0
l0 = ""
l1 = ""
l2 = ""
score2 = 0
for line in lines:
  if i == 0:
    l0 = line
  elif i == 1:
    l1 = line
  else:
    l2 = line

    same = [v for v in l0 if (v in l1) and (v in l2)]
    score2 += get_value(same[0])
    
  i += 1
  if i > 2:
    i = 0

print(f"{score2}")