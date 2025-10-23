# Read in the file
with open('../transliterationFiles/ZL3b-n/ZL3b-n_ENCODING.txt', 'r') as file:
  filedata = file.read()

# Write the file out again
with open('../transliterationFiles/ZL3b-n/ZL3b-n_ENCODING.txt', 'w', encoding='utf-8') as file:
  file.write(filedata)