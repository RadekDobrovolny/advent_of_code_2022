input_file = open('./day_6/input.txt')
line = input_file.readlines()[0]

# line = "bvwbjplbgvbhsrlpgdmjqwftvncz"

def uni_checker(line, l):
  for i in range(len(line)):
    chunk = line[i:i+l]
    if len(set(chunk)) == l:
      return i + l
  return None

print(uni_checker(line, 4))
print(uni_checker(line, 14))
