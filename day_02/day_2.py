def check_game(a, b):
  score = 0
  if b == "X":
    score += 1
  elif b == "Y":
    score += 2
  else:
    score += 3

  if a == "A":
    if b == "X":
      score +=3
    elif b == "Y":
      score += 6

  if a == "B":
    if b == "Y":
      score +=3
    elif b == "Z":
      score += 6

  if a == "C":
    if b == "Z":
      score +=3
    elif b == "X":
      score += 6

  return score

def get_strategy(a, b):
  # Lose
  if b == "X":
    if a == "A":
      return "Z"
    if a == "B":
      return "X"
    if a == "C":
      return "Y"
  
  # Draw
  if b == "Y":
    if a == "A":
      return "X"
    if a == "B":
      return "Y"
    if a == "C":
      return "Z"

  # Win
  if b == "Z":
    if a == "A":
      return "Y"
    if a == "B":
      return "Z"
    if a == "C":
      return "X"    

input_file = open('./day_2/input.txt')
lines = input_file.readlines()

score = 0
score_with_strategy = 0
for line in lines:
  p1, p2 = line.strip().split()
  score += check_game(p1, p2)
  # res = check_game(tuple(line.strip().split(" ")))

  score_with_strategy += check_game(p1, get_strategy(p1, p2))

print(f"First part sum is: {score}")
print(f"Second part sum is: {score_with_strategy}")
  
