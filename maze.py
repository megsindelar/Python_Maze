from copy import deepcopy
import numpy as np

### FUNCTIONS ### 

def update_wallmat_Robotpos():

    wallmat[robotPos[0],robotPos[1]] = robotVal # Update wall matrix to display robot current pos





def breadth_first_search(): 

    wavemat[fringe[0][0], fringe[0][1]] = 1 # Set starting position to 1

    while len(fringe) != 0: # While loop that will continue as long as fringe/next nodes to examine is not 0

        # add to wave's fringe, into an array of its indices
        # pushes out wave fringe and removes old visited indices
        # Find children function
        if wallmat[fringe[0][0]+1, fringe[0][1]] == 0 and wavemat[fringe[0][0]+1, fringe[0][1]] == 0:
            fringe.append([fringe[0][0]+1, fringe[0][1]])
            wavemat[fringe[0][0]+1, fringe[0][1]] = wavemat[fringe[0][0], fringe[0][1]] + 1
           
        if wallmat[fringe[0][0]-1, fringe[0][1]] == 0 and wavemat[fringe[0][0]-1, fringe[0][1]] == 0:
            fringe.append([fringe[0][0]-1, fringe[0][1]])
            wavemat[fringe[0][0]-1, fringe[0][1]] = wavemat[fringe[0][0], fringe[0][1]] + 1
            
        if wallmat[fringe[0][0], fringe[0][1]+1] == 0 and wavemat[fringe[0][0], fringe[0][1]+1] == 0:
            fringe.append([fringe[0][0], fringe[0][1]+1])
            wavemat[fringe[0][0], fringe[0][1]+1] = wavemat[fringe[0][0], fringe[0][1]] + 1
            
        if wallmat[fringe[0][0], fringe[0][1]-1] == 0 and wavemat[fringe[0][0], fringe[0][1]-1] == 0:
            fringe.append([fringe[0][0], fringe[0][1]-1])
            wavemat[fringe[0][0], fringe[0][1]-1] = wavemat[fringe[0][0], fringe[0][1]] + 1
           

        visited.insert(0, fringe[0])
        fringe.remove(visited[0])

        print('fringe = \n', fringe)
        print('\n')
        print('walmat = \n', wallmat)
        print('\n')
        print('wavemat = \n', wavemat)
        print('\n')




# Wall matrix and wave matrix
wallmat = np.array([[-1, -1, -1, -1, -1, -1], [-1, 0, 0, 0, -1, -1], [-1, -1, 0, -1, -1, -1], [-1, 0, 0, 0, 0, -1], [-1, 0, -1, 0, 0, -1], [-1, -1, -1, -1, -1, -1]])
wavemat = np.zeros((6,6))
wavemat = np.copy(wallmat) # DOES NOT MAKE WAVEMAT A POINTER!


### Robot variables ###
robotVal = 7 # Robot value for display on wallmat matrix
Rstartpos = [4,4] # Robot start position
robotPos = [0,0] # Holds robot position
# Update Robot start pos
robotPos[0] = Rstartpos[0]
robotPos[1] = Rstartpos[1]


### Algorithm variables ###
# Fringe - Contains robot start position at the beginning then after that it has the next nodes to be visited
fringe = [Rstartpos]  
# Visited - contains the nodes already visited
visited = []



# Call search function
breadth_first_search() 
