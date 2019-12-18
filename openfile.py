filename = "CCaseScene.unity"
with open(filename, 'r') as myfile:
  data = myfile.read()
  subA = ("<<<<<<< Updated upstream\n")
  subB = ("=======\n")
  subC = (">>>>>>> Stashed changes\n")
  print "Longitud: " + str(len(subA))
  print "Longitud: " + str(len(subB))
  print "Longitud: " + str(len(subC))
  resA = [i for i in range(len(data)) if data.startswith(subA, i)]
  resB = [i for i in range(len(data)) if data.startswith(subB, i)]
  resC = [i for i in range(len(data)) if data.startswith(subC, i)]
  print "Coincidencias: " + str(len(resA))
  print "Coincidencias: " + str(len(resB))
  print "Coincidencias: " + str(len(resC))
