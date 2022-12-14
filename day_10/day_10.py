input_file = open('./day_10/input.txt')
lines = input_file.readlines()

register = 1
working = False
instruction = ""

crt_line0 = [["_" for _ in range(40)] for _ in range(6)]
for tick in range(1, 241):
  # print(f"{tick}")
  sprite_pos = [" " for _ in range(41)]
  sprite_pos[register-1] = "O"
  sprite_pos[register+0] = "O"
  sprite_pos[register+1] = "O"
  # print("".join(sprite_pos))

  if abs(((tick-1) % 40) - register) <= 1:
    crt_line0[(tick-1) // 40][(tick-1) % 40] = "#"
  else:
    crt_line0[(tick-1) // 40][(tick-1) % 40] = " "
  # print("".join(crt_line0[(tick-1) // 40]))
  
  if not working:
    instruction = lines.pop(0)

    if instruction.strip() != "noop":
      working = True
  else:
    _, number = instruction.split(" ")
    register += int(number)
    working = False

for l in crt_line0:
  print("".join(l))