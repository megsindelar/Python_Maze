import numpy as np

wallmat = np.array([[0, 0, 0, -1], [-1, 0, -1, -1], [0, 0, 0, 0], [0, -1, 0, 0]])
wavemat = np.zeros((4,4))
print(wavemat)

#robotpos = wallmat[0, 0]
#robotpos = 2

#print(wavemat)

robotpos = [0,0]
robotval = 7

wallmat[robotpos[0],robotpos[1]] = robotval
print(wallmat)






