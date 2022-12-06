max_cal = 0

input_file = open('./day_1/input_a.txt')
lines = input_file.readlines()

current_cal = 0
for line in lines:
  if line.strip():
    current_cal += int(line)
  else:
    if current_cal > max_cal:
      max_cal = current_cal
    current_cal = 0

print(f"Top elf has: {max_cal}")

top_three = [0, 0, 0]
current_cal = 0
for line in lines:
  if line.strip():
    current_cal += int(line)
  else:
    if current_cal > min(top_three):
      top_three.remove(min(top_three))
      top_three.append(current_cal)
    current_cal = 0

print(f"Top three elves have: {sum(top_three)}")
