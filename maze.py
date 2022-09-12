import numpy as np

# make matrix

wallmat = np.array([[-1, -1, -1, -1, -1, -1], [-1, 0, 0, 0, -1, -1], [-1, -1, 0, -1, -1, -1], [-1, 0, 0, 0, 0, -1], [-1, 0, -1, 0, 0, -1], [-1, -1, -1, -1, -1, -1,]])
wavemat = np.zeros((6,6))

# initialize variables

i=4
j=4

fringe = [[i,j]]
visited = []

# add to wave's fringe, into an array of its indices
# pushes out wave fringe and removes old visited indices

fringe.append([i+1, j])
fringe.append([i-1, j])
fringe.append([i, j+1])
fringe.append([i, j-1])
visited.insert(0, fringe[0])
fringe.remove(visited[0])

print(fringe)