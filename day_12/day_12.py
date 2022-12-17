from pprint import pprint


def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        # print("".join(data[c[0]][c[1]] for c in current_path))
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []


input_file = open('./day_12/input.txt')
lines = input_file.readlines()

start = ()
goal = ()
lowest = []
data = [ [""] * len(lines[0].strip()) for _ in range(len(lines)) ]
for i, line in enumerate(lines):
  for j, chr in enumerate(line.strip()):
    if chr == "S":
      start = (i, j)
      chr = "a"
    if chr == "E":
      goal = (i, j)
      chr = "z"
    if chr == "a":
      lowest.append((i,j))
    data[i][j] = chr

graph = {}
for i, row in enumerate(data):
  for j, point in enumerate(data[i]):
    value = data[i][j]
    neighbours = []
    
    # Check right
    if j < len(row)-1:
      if ord(data[i][j+1]) - ord(value) <= 1:
        neighbours.append((i, j+1))

    # Check left
    if j > 0:
      if ord(data[i][j-1]) - ord(value) <= 1:
        neighbours.append((i, j-1))

    # Check down
    if i < len(data)-1:
      if ord(data[i+1][j]) - ord(value) <= 1:
        neighbours.append((i+1, j))

    # Check up
    if i > 0:
      if ord(data[i-1][j]) - ord(value) <= 1:
        neighbours.append((i-1, j))
    
    graph.update({(i,j): neighbours})

# pprint(data)
# pprint(graph)

# sp = shortest_path(graph, start, goal)
# print(len(sp)-1)

pathes = []
for low in lowest:
  sp = shortest_path(graph, low, goal)
  print(f"{low}: {len(sp)}")
  if len(sp):
    pathes.append(len(sp)-1)

print(pathes)
print(min(pathes))
