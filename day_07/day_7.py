from pprint import pprint

input_file = open('./day_7/input.txt')
lines = input_file.readlines()

filesystem = {}

def check_folder(folder):
  return folder in filesystem.keys()

def add_folder(folder):  
  filesystem.update({
    folder: {}
  })

def add_file(current_folder, name, size):
  folder = filesystem.get(current_folder)
  folder.update(
    {name: size}
  )


current_folder = ""
ls_mode = False
for line in lines:
  l = line.strip().split(" ")

  if l[0] == "$":
      ls_mode = False

  if ls_mode:
    if l[0] == "dir":
      if not check_folder(current_folder + "-" + l[1]):
        add_folder(current_folder + "-" + l[1])
    else:
      add_file(current_folder, l[1], l[0])
      

  if l[0] == "$":
    ls_mode = False
    
    if l[1] == "cd":
      if l[2] == "..":
        current_folder = current_folder[:current_folder.rfind("-")]
      else:
        if not current_folder:
          current_folder = l[2]
        else:
          current_folder += "-" + l[2]
        
        if not check_folder(current_folder):
          add_folder(current_folder)

    if l[1] == "ls":
      ls_mode = True


sizes = {}
for dir_name, dir in filesystem.items():
  dir_size = 0
  for file_name, file_size in dir.items():
    dir_size += int(file_size)
  sizes.update(
    {dir_name: dir_size}
  )

sum = 0
for dir_name in sizes.keys():
  total_size = 0
  for d, size in sizes.items():
    if dir_name in d:
      total_size += size
  print(f"{dir_name}: {total_size}")
  if total_size > 532_950: # 70_000_000 - 30_000_000 - size of folder "/"
    print("Adept") # I find the smallest by hand
  
  if total_size < 100_000:
    sum += total_size

print(f"{sum}")
