import numpy as np
import random

### CONNECT THE DOTS MAZEGEN ###

# Make blankmaze, add border of -1

randcolumns = random.randint(3,10)
randrows = random.randint(3,10)
blankmaze = np.zeros((randrows, randcolumns))
padmaze = np.pad(blankmaze, pad_width = 1, constant_values = -1)
print(padmaze)

# Generate index pairs

indices = []

for p in range(10):
    # generates indices inside matrix borders
    randx = random.randint(1,randcolumns-1)
    randy = random.randint(1,randrows-1)
    indices.append([randx,randy])

for q in indices:
    print(q[0],q[1])
    padmaze[q[0], q[1]] = 1


print(indices)
print(padmaze)


# Connect the dots