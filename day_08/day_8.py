input_file = open('./day_8/input.txt')
lines = input_file.readlines()

forest = []
for line in lines:
  forest.append(line.strip())

visible_trees = 0
scenic_max = 0
for i in range(len(forest)):
  for j in range(len(forest[i])):
    # print(f"Solving tree [{i}][{j}] with height {forest[i][j]}")
    tree_height = forest[i][j]

    # check from right
    vis_from_right = True
    scenic_right = 0
    for k in range(j-1, -1, -1):
      if vis_from_right:
        scenic_right += 1
      if forest[i][k] >= tree_height:
        vis_from_right = False
      
    # check from left
    vis_from_left = True
    scenic_left = 0
    for k in range(j+1, len(forest[i])):
      if vis_from_left:
        scenic_left += 1
      if forest[i][k] >= tree_height:
        vis_from_left = False
      

    # check from top
    vis_from_top = True
    scenic_top = 0
    for k in range(i-1, -1, -1):
      if vis_from_top:
        scenic_top += 1
      if forest[k][j] >= tree_height:
        vis_from_top = False

    # check from bot
    vis_from_bot = True
    scenic_bot = 0
    for k in range(i+1, len(forest)):
      if vis_from_bot:
        scenic_bot += 1
      if forest[k][j] >= tree_height:
        vis_from_bot = False

    scenic_score = scenic_right * scenic_left * scenic_top * scenic_bot
    if scenic_score > scenic_max:
      scenic_max = scenic_score

    if vis_from_right or vis_from_left or vis_from_top or vis_from_bot:
      visible_trees += 1

print(visible_trees)
print(scenic_max)
  