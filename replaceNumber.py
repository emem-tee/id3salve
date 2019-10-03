# import os

# os.chdir("C:/seniorFD/Python/id3salve")

import eyed3
import os
import re

folder = 'C:/Users/michael/Music/Asher Roth/Rawth'

# Goes to the directory of the music you want to modify
os.chdir(folder)

# Prints the working directory to confirm
print(os.getcwd())

# Creates a list of all the entries at the directory location you indicated
files = os.listdir(os.getcwd())

# Makes sure that you only import the .mp3 files
r = re.compile('.*\.mp3')

# Subsets the list to only include the .mp3 files
musicfiles = list(filter(r.match, files))

# Prints the vector
#print(files)

# Creates an empty list 
filesrep = []

# Substitutes the number information at the beginning of the list
# Also removes the "DatPiff Exclusive" from the front
for i in range(len(musicfiles)):  
  x = re.sub('^[0-9 \_]* | \(DatPiff Exclusive\)|^_', '', musicfiles[i])
  # x = i.title()
  # (x)
  fn = folder + '/' + musicfiles[i] 
  song = eyed3.load(fn)
  song.tag.title = x
  # Saves the new tag 
  song.tag.save()
  os.rename(folder + '/' + musicfiles[i], folder + '/' + x)
  print(musicfiles[i] + "-- Became -->" + x)

# Writes the new filename
# song = eyed3.load(folder + '/' + files[1])
# song.tag.title = files[1]
# Saves the new tag 
# song.tag.save()
  

# song.tag.
# print(filesrep[1])
#def printsongs(x):
#  for i in x:
#    print(i)

# printsongs(filesrep)
	
# print(filesrep, sep = '\n', end = '\n')

