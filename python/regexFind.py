import re

with open('../transliterationFiles/ZL3b-n/ZL3b-n_CHANGED.txt', 'r', encoding="utf-8") as file:
  filedata = file.read()
  x = re.findall(r"<!\d\d:\d\d>", filedata)
  res = []

  for item in x:
      if item not in res:
          res.append(item) # unique items only
          res.sort() # alphabetical
  print(res)