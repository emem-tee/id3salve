# os.chdir("C:/seniorFD/Python/id3salve")

from glob import glob # For isolating .mp3 files
import eyed3 # For manipulating ID3 tags
import os # For setting the work directory
import re # Regular Expressions

folder = 'C:Your/File/Path'
pattern =  '^[0-9]* \- ' # This is the regex for what you want removed
# pattern =  '^[0-9]{2} \- ' # This is the regex for what you want removed

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
  # x is the cleaned name of the song based off of the filename 
  x = re.sub(pattern, '', musicfiles[i])
  # fn is the full file name
  fn = folder + '/' + musicfiles[i]
  # Loads the file  
  song = eyed3.load(fn)
  # Modifies the "title" property of the song's id3 tag
  song.tag.title = x
  # Saves the tag with the new title
  song.tag.save()
  # Renames the file to match the new title
  # I decided this was unneccessary
  # os.rename(folder + '/' + musicfiles[i], folder + '/' + x)
  # Prints both names to show it worked
  print(musicfiles[i] + "-- Became -->" + song.tag.title)
