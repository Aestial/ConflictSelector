filename = "CCaseScene.unity"

subA = ("<<<<<<< Updated upstream\n")
subB = ("=======\n")
subC = (">>>>>>> Stashed changes\n")

with open(filename, 'r+') as f:
  data = f.read()
  # Iterate starts
  # while True:

  # Find indexes
  start, end = data.index(subA), data.index(subB)
  # Slice string
  data = data[:start] + data[end:]
  data = data.replace(subB,"", 1).replace(subC,"", 1)
  # Iterate ends
  # if(data.find(subA) < 0)
  #   break
  # return pointer to top of file so we can re-write the content with replaced string
  f.seek(0)
  # re-write the content with the updated content
  f.write(data)
  # close file
  f.close()
