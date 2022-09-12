from copy import deepcopy
from cgitb import small
from operator import ne
import re
from shutil import move
from tabnanny import check
import wave
import numpy as np





















wallmat = np.array([[-1, -1, -1, -1, -1, -1], [-1, 0, 0, 0, -1, -1], [-1, -1, 0, -1, -1, -1], [-1, 0, 0, 0, 0, -1], [-1, 0, -1, 0, 0, -1]])
wavemat = np.zeros((6,6))

wallmat = np.array([[-1, -1, -1, -1, -1, -1], [-1, 0, 2, 0, -1, -1], [-1, -1, 0, -1, -1, -1], [-1, 0, 0, 0, 0, -1], [-1, 0, -1, 0, 3, -1], [-2, -2, -2, -2, -2, -2]])
wavemat = np.array([[-2, -2, -2, -2, -2, -2], [-2, 6, 5, 6, -1, -2], [-2, -1, 4, -1, -1, -2], [-2, 4, 3, 2, 1, -2], [-2, 5, -1, 1, 0, -2], [-2, -2, -2, -2, -2, -2]])
print(wavemat)



#robotpos = wallmat[0, 0]
#robotpos = 2



#print(wavemat)

#robotpos = [0,0]
#robotval = 7

#wallmat[robotpos[0],robotpos[1]] = robotval
print(wallmat)



#keep track of what index goal is at and what index the robot is at and if it's at goal then it's done


###################################################
#backtracking - Meg
###################################################

"""Find shortest path"""
def shortest_path():
    """Determine where the robot should move"""
    def move_robot(ind):
        global i,j, robotpos
        print(robotpos)
        print(i)
        #print(j)
        if ind == 0:
            """Robot position movement north"""
            robotpos = [(i+1),j]
            i+=1
        elif ind == 1:
            """Robot position movement east"""
            robotpos = [i,(j+1)]
            j+=1
        elif ind == 2:
            """Robot position movement south"""
            robotpos = [(i-1), j]
            i-=1
        else:
            """Robot position movement west"""
            robotpos = [i, (j-1)]
            j-=1

    def reverse_robot(ind):
        global i,j
        if ind == 0:
            """Reverse robot position movement from north"""
            robotpos = [(i-1),j]
            i-=1
        elif ind == 1:
            """Reverse robot position movement from east"""
            robotpos = [i,(j-1)]
            j-=1
        elif ind == 2:
            """Reverse robot position movement from south"""
            robotpos = [(i+1), j]
            i+=1
        else:
            """Reverse robot position movement from west"""
            robotpos = [i, (j+1)]
            j+=1

    def check_goal():
        global robotpos
        close = np.subtract(robotpos,goal)
        if (abs(close[0] < 2) and close[1] == 0) or (close[0] == 0 and abs(close[1] < 2)):
            """If next to goal, move to goal"""
            robotpos = goal
            ifgoal = 1
            return ifgoal
        else:
            ifgoal = 0
            return ifgoal

    def pos_vals_rob(l):
        global length, last_val, next_val, next_ind, reached_goal
        """Checking position values"""
        ifgoal = check_goal()
        if (ifgoal == 1):
            print("Reached goal!")
            reached_goal = 1

        elif (smallest_num[0] == -1) or (smallest_num[0] == -2):
            """Check if robot is next to a wall (-1 represents a wall)"""
            check_wall = smallest_num[1]
            c = 1
            while check_wall == -1 or check_wall == -2:
                c+=1
                check_wall = smallest_num[c]
                if(c == 3) & (check_wall == -1 or check_wall == -2):
                    print("Boxed in! No way out!")
                    break
            next_val = check_wall

            if (l == 0):
                next_ind = []
                index_pos = 0
                m = 0
                for a in lst:
                    if check_wall in lst:
                        next_index = lst.index(check_wall, index_pos)
                        next_ind.append(next_index)
                        length = len(next_ind)
                    
            """Checking if multiple of the same smallest cell values"""
            if (length>1) & (l == 0):
                move_robot(next_ind[m])
                m+=1
                l+=1
                length -= 1
                last_val = check_wall
                pos_vals_rob(l)
            elif (length>1) & (l>0) & (next_val > last_val):
                reverse_robot(next_ind[m-1])
                move_robot(next_ind[m])
                length-=1
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
                next_ind = []
                index_pos = 0
                m = 0
                for i in lst:
                    if check_wall in lst:
                        next_index = lst.index(check_wall, index_pos)
                        next_ind.append(next_index)
                        length = len(next_ind)
            
            if (length>1) & (l == 0):
                move_robot(next_ind[m])
                m+=1
                l+=1
                last_val = check_wall
                length-=1
                pos_vals_rob(l)
            elif (length>1) & (l>0) & (next_val>last_val):
                reverse_robot(next_ind[m-1])
                move_robot(next_ind[m])
                length-=1
                m+=1
                l+=1
                last_val = check_wall
                pos_vals_rob(l)
            else:
                move_robot(next_ind[0])
    

    """Code for shortest path"""
    robot_move = wavemat

    """Place robot at start"""
    pos_robot = np.where(wallmat == 2)
    robotpos_0 = pos_robot[0]
    robotpos_1 = pos_robot[1]
    global robotpos
    robotpos = [robotpos_0[0], robotpos_1[0]]
    global i
    global j
    i = robotpos[0]
    j = robotpos[1]
    print(i)

    global length
    length = 0
    global next_val, last_val
    next_val = 0
    last_val = 0
    global next_ind
    next_ind = []

    """Check if robot is next to the goal (3 represents goal)"""
    posr = np.where(wallmat == 3)
    posr_0 = posr[0]
    posr_1 = posr[1]
    goal = [posr_0[0], posr_1[0]]

    """Directions robot can move"""
    north = robot_move[(i+1), j]
    east = robot_move[i, (j+1)]
    south = robot_move[(i-1), j]
    west = robot_move[i, (j-1)]


    """Finding the smallest numeric value for robot path"""
    lst = [north, east, south, west]
    #lst = [5,2,7,4]
    lst_str = [str(x) for x in lst]
    lst.sort()
    lst_str.sort()
    smallest_num = np.copy(lst)
    smallest = np.copy(lst_str)
    #print(smallest_num)


    pos_vals_rob(0)
    global reached_goal
    reached_goal = 0 
    pos_vals_rob(0)

    


"""Run Robot Path"""
shortest_path()


































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


