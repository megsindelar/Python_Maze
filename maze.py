from copy import deepcopy
from cgitb import small
from operator import ne
from shutil import move
from tabnanny import check
import wave
import numpy as np
























###################################################
#backtracking - Meg
###################################################

robot_move = wavemat

"""Place robot at start"""
robotpos = start

m = 0

"""Find shortest path"""
def shortest_path():

    m = 0

    """Directions robot can move"""
    north = robot_move[(i+1), i]
    east = robot_move[i, (i+1)]
    south = robot_move[(i-1), i]
    west = robot_move[i, (i-1)]


    """Finding the smallest numeric value for robot path"""
    lst = [north, east, south, west]
    lst_str = [str(x) for x in lst]
    smallest_num = lst.sort()
    smallest = [str(x) for x in smallest_num]


    """Determine where the robot should move"""
    def move_robot(ind):
        if ind == 0:
            """Robot position movement north"""
            robotpos = wavemat[(i+1),i]
        elif ind == 1:
            """Robot position movement east"""
            robotpos = wavemat[i,(i+1)]
        elif ind == 2:
            """Robot position movement south"""
            robotpos = wavemat[(i-1), i]
        else:
            """Robot position movement west"""
            robotpos = wavemat[i, (i-1)]

    def reverse_robot(ind):
        if ind == 0:
            """Reverse robot position movement from north"""
            robotpos = wavemat[(i-1),i]
        elif ind == 1:
            """Reverse robot position movement from east"""
            robotpos = wavemat[i,(i-1)]
        elif ind == 2:
            """Reverse robot position movement from south"""
            robotpos = wavemat[(i+1), i]
        else:
            """Reverse robot position movement from west"""
            robotpos = wavemat[i, (i+1)]

    
    def pos_vals_rob(l):
        """Checking position values"""
        if (lst_str.__contains__("3")):
            """Check if robot is next to the goal (3 represents goal)"""
            list_index = lst_str.index("3")
            move_robot(list_index)
            print("Reached goal!")

        elif (smallest_num[0] == -1):
            """Check if robot is next to a wall (-1 represents a wall)"""
            check_wall = smallest_num[1]
            i = 1
            while check_wall == -1:
                i+=1
                check_wall = smallest_num[i]
                if(i == 3) & (check_wall == -1):
                    print("Boxed in! No way out!")
                    break
            next_val = check_wall

            if (l == 0):
                for i in lst:
                    if check_wall in lst:
                        next_ind = []
                        next_ind = next_ind.append(lst.index(check_wall))
                        len = len(next_ind)
            
            """Checking if multiple of the same smallest cell values"""
            if (len>1) & (l == 0):
                move_robot(next_ind[m])
                m+=1
                l+=1
                len -= 1
                last_val = check_wall
                pos_vals_rob(l)
            elif (len>1) & (l>0) & (next_val > last_val):
                reverse_robot(next_ind[m-1])
                move_robot(next_ind[m])
                len-=1
                m+=1
                l+=1
                last_val = check_wall
                pos_vals_rob(l)
            else:
                move_robot(next_ind[0])

        
        else:
            """If smallest value is not a wall or robot is not next to the goal, then move to the smallest value cell"""
            check_wall = smallest_num[0]
            rob_ind = lst.index(check_wall)
            move_robot(rob_ind)
            next_val = check_wall

            """Checking if there are multiple of the same smallest value"""
            if (l == 0):
                for i in lst:
                    if check_wall in lst:
                        next_ind = []
                        next_ind = next_ind.append(lst.index(check_wall))
                        len = len(next_ind)
            
            if (len>1) & (l == 0):
                move_robot(next_ind[m])
                m+=1
                l+=1
                last_val = check_wall
                len-=1
                pos_vals_rob(l)
            elif (len>1) & (l>0) & (next_val>last_val):
                reverse_robot(next_ind[m-1])
                move_robot(next_ind[m])
                len-=1
                m+=1
                l+=1
                last_val = check_wall
                pos_vals_rob(l)
            else:
                move_robot(next_ind[0])

            



    pos_vals_rob(0)



































### FUNCTIONS ### 

def update_wallmat_Robotpos():

    wallmat[robotPos[0],robotPos[1]] = robotVal # Update wall matrix to display robot current pos



def displayMatrix():

        #print('fringe = \n', fringe)
        #print('\n')
        #print('walmat = \n', wallmat)
        #print('\n')
        print('wavemat = \n', wavemat)
        print('\n')






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

        displayMatrix()





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
