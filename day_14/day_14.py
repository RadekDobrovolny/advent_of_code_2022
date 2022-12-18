from pprint import pprint

input_file = open('./day_14/input.txt')
lines = input_file.readlines()

data = []
max_x = 0
min_x = 1000
max_y = 0

for line in lines:
  shape = []
  for coord in line.strip().split(" -> "):
    x, y = coord.split(",")
    x = int(x)
    y = int(y)
    if x > max_x:
      max_x = x
    if x < min_x:
      min_x = x
    if y > max_y:
      max_y = y
    shape.append((x, y))
  data.append(shape)

pprint(max_x)
pprint(min_x)
pprint(max_y)

min_x -= 1

world = [[" "] * (max_x - min_x + 3) for _ in range(max_y + 1)]

def draw(coord, symbol):
  world[coord[1]][coord[0] - min_x] = symbol

def get(coord):
  return world[coord[1]][coord[0] - min_x]

for shape in data:
  for i in range(len(shape) - 1):
    coord_f = shape[i]
    coord_t = shape[i+1]

    if coord_f[0] == coord_t[0]:
      for i in range(min(coord_f[1], coord_t[1]), max(coord_f[1], coord_t[1]) + 1):
        draw((coord_f[0], i), "█")

    if coord_f[1] == coord_t[1]:
      for i in range(min(coord_f[0], coord_t[0]), max(coord_f[0], coord_t[0]) + 1):
        draw((i, coord_f[1]), "█")


def add_sand():
  if get((500, 0)) == "o":
      return False
  sand = (500, 0)
  end = False
  while not end:
    draw(sand, ".")
    if not (sand[1] < max_y and sand[0] >= min_x and sand[0] <= max_x):
      return False
  
    if get((sand[0], sand[1]+1)) in [".", " "]:
      sand = (sand[0], sand[1]+1)
    elif get((sand[0]-1, sand[1]+1)) in [".", " "]:
      sand = (sand[0]-1, sand[1]+1)
    elif get((sand[0]+1, sand[1]+1)) in [".", " "]:
      sand = (sand[0]+1, sand[1]+1)
    else:
      end = True

  draw(sand, "o")
  return True

i = 0
while add_sand():
  print(i := i + 1)

# with open('./day_14/output.txt', 'a') as the_file:
  # for line in world:
    # print("".join(line))
    # the_file.write("".join(line) + '\n')
