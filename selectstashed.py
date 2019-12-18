import sys
program_name = sys.argv[0]
filenames = sys.argv[1:]

subA = ("<<<<<<< Updated upstream\n")
subB = ("=======\n")
subC = (">>>>>>> Stashed changes\n")

for filename in filenames:    
    with open(filename, 'r+') as f:
      data = f.read()
      count = 0
      # Iterate starts
      while True:
          # Find indexes
          start, end = data.index(subA), data.index(subB)
          # Slice string
          data = data[:start] + data[end:]
          data = data.replace(subB,"", 1).replace(subC,"", 1)
          # Iterate ends
          count += 1
          if(data.find(subA) < 0):
          # if(count > 4):
            break
      # return pointer to top of file so we can re-write the content with replaced string
      f.seek(0)
      # Deletes
      f.truncate()
      # re-write the content with the updated content
      f.write(data)
      # close file
      f.close()
