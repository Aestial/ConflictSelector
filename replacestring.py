filename = "CCaseScene.unity"
with open(filename, 'w') as f:
  data = f.read()
  subA = ("<<<<<<< Updated upstream\n")
  subB = ("=======\n")
  subC = (">>>>>>> Stashed changes\n")
  print "Longitud: " + str(len(subA))
  print "Longitud: " + str(len(subB))
  print "Longitud: " + str(len(subC))
  start = data.index(subA)
  end = data.index(subB)
  print start, end
  newData = data[:start] + data[end:]
  # resA = [i for i in range(len(data)) if data.startswith(subA, i)]
  # return pointer to top of file so we can re-write the content with replaced string
  f.seek(0)
  # clear file content
  f.truncate()
  # re-write the content with the updated content
  f.write(newData)
  # close file
  f.close()
