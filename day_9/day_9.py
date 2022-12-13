from os import system
from time import sleep

global line

matrix_footprints = [ ["."] * 26 for _ in range(26) ]
# matrix_footprints = [["."] * 1000 for _ in range(1000)]

input_file = open('./day_9/input_small_2.txt')
lines = input_file.readlines()

# Short rope
# rope = [[8, 0] for _ in range(2)]

# Long rope
rope = [[15, 11] for _ in range(10)]

def print_matrix(matrix):
  for row in matrix: 
    print(" ".join(row))

def draw():
  system('clear')
  matrix = [ ["."] * 26 for _ in range(26) ]

  # Draw long rope
  matrix[15][11] = "s"
  for i in range(len(rope)-1, -1, -1):
    matrix[rope[i][0]][rope[i][1]] = str(i)

  print_matrix(matrix)
  print("")
  print_matrix(matrix_footprints)
  sleep(0.2)

def move_head(head, direction):
  if direction == "R":
    head = (head[0], head[1] + 1)

  if direction == "U":
    head = (head[0] - 1, head[1]) 

  if direction == "L":
    head = (head[0], head[1] - 1)

  if direction == "D":
    head = (head[0] + 1, head[1])

  return head
  

def follow_head(head, tail):
  # Up & Right
  if abs(head[0] - tail[0]) == 2 and abs(head[1] - tail[1]) == 2:
    tail = [(tail[0] + head[0]) // 2, (tail[1] + head[1]) // 2]
    return tail

  # Right
  if head[1] - tail[1] > 1:
    tail[1] += 1
    if tail[0] != head[0]:
      tail[0] = head[0]
    return tail

  # Up
  if head[0] - tail[0] < -1:
    tail[0] -= 1
    if tail[1] != head[1]:
      tail[1] = head[1]
    return tail

  # Left
  if head[1] - tail[1] < -1:
    tail[1] -= 1
    if tail[0] != head[0]:
      tail[0] = head[0]
    return tail

  # Down
  if head[0] - tail[0] > 1:
    tail[0] += 1
    if tail[1] != head[1]:
      tail[1] = head[1]
    return tail

  return tail
  

for line in lines:
  direction, steps = line.split(" ")
  for _ in range(int(steps)):

    rope[0] = move_head(rope[0], direction)

    for i in range(1, len(rope)):
      rope[i] = follow_head(rope[i-1], rope[i])    
    
    matrix_footprints[rope[-1][0]][rope[-1][1]] = "#"
    draw()

total_footprints = 0
for row in matrix_footprints:
  total_footprints += row.count("#")
print(total_footprints)
