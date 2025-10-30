import re

with (open('../transliterationFiles/ZL3b-n/ZL3b-n_CHANGED.txt', 'r', encoding="utf-8") as file):
  filedata = file.read()
  x = (
      filedata.replace(re.findall(r"\d\d:\d\d", filedata), '‚'),
    re.findall(r"\d\d:\d\d", filedata), # ANGLES
    re.findall(r"<f\d\d?[a-z]>", filedata) # PAGE NAME
  )
  print(x)