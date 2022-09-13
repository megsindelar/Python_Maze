import numpy as np
import random

### CONNECT THE DOTS MAZEGEN ###

# Make blankmaze, add border of -1

randcolumns = random.randint(8,12)
randrows = random.randint(8,12)
blankmaze = np.zeros((randrows, randcolumns))
blankmaze.fill(1)
padmaze = np.pad(blankmaze, pad_width = 1, constant_values = -1)

# create alternating rows of zeros to connect random paths

m=0
while m < randrows:
    m += 3
    padmaze[m, 1:randcolumns+1] = 0

# Generate index pairs and branch 

indices = []

for p in range(15):
    # generates indices inside matrix borders
    randx = random.randint(1,randcolumns-1)
    randy = random.randint(1,randrows-1)
    indices.append([randx,randy])

for q in indices:
    print(q[0],q[1])
    padmaze[q[0], q[1]] = 0

    if padmaze[q[0]+1, q[1]] == 1 and padmaze[q[0]-1, q[1]] == 1 and padmaze[q[0], q[1]+1] == 1 and padmaze[q[0], q[1]-1] == 1:
        padmaze[q[0]+1, q[1]] = 0
        padmaze[q[0]-1, q[1]] = 0
    else:
        continue

    if padmaze[q[0]+2, q[1]] == 1 and padmaze[q[0]-2, q[1]] == 1 and padmaze[q[0], q[1]+2] == 1 and padmaze[q[0], q[1]-2] == 1:
        padmaze[q[0]+2, q[1]] = 0
        padmaze[q[0]-2, q[1]] = 0
    else:
        continue

print(indices)
print(padmaze)
