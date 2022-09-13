import numpy as np
import random

### CONNECT THE DOTS MAZEGEN ###

# Make blankmaze, add border of -1

randsizex = random.randint(3,10)
randsizey = random.randint(3,10)
blankmaze = np.zeros((randsizex, randsizey))
padmaze = np.pad(blankmaze, pad_width = 1, constant_values = -1)
print(padmaze)

# Generate index pairs

indices = []

for p in range(10):
    randx = random.randint(1,randsizex-1)
    randy = random.randint(1,randsizey-1)
    indices.append([randx,randy])
print(indices)

# Connect the dots