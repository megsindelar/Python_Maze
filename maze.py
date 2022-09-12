import numpy as np

### FUNCTIONS ### 

def update_wallmat():

    wallmat[robotPos[0],robotPos[1]] = robotVal # Update wall matrix to display robot current pos


def breadth_first_search():
    




# Wall matrix and wave matrix
wallmat = np.array([[-1, -1, -1, -1, -1, -1], [-1, 0, 0, 0, -1, -1], [-1, -1, 0, -1, -1, -1], [-1, 0, 0, 0, 0, -1], [-1, 0, -1, 0, 0, -1], [-1, -1, -1, -1, -1, -1]])
wavemat = np.zeros((6,6))

print(wallmat)
print(wavemat)


### Robot variables ###
robotVal = 7 # Robot value for display on wallmat matrix
Rstartpos = [4,4] # Robot start position
robotPos = [0,0] # Holds robot position
# Update Robot start pos
robotPos[0] = Rstartpos[0]
robotPos[1] = Rstartpos[1]
>>>>>>> 6d9f747 (Added Robot variables and robot position update)


### Algorithm variables ###
# Fringe - Contains robot start position at the beginning then after that it has the next nodes to be visited
fringe = [robotPos]  
# Visited - contains the nodes already visited
visited = []

print(fringe)
>>>>>>> 6d9f747 (Added Robot variables and robot position update)

# add to wave's fringe, into an array of its indices
# pushes out wave fringe and removes old visited indices
fringe.append([robotPos[0]+1, robotPos[1]])
fringe.append([robotPos[0]-1, robotPos[1]])
fringe.append([robotPos[0], robotPos[1]+1])
fringe.append([robotPos[0], robotPos[1]-1])
visited.insert(0, fringe[0])
fringe.remove(visited[0])

print(fringe)

