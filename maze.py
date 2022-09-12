from cgitb import small
from operator import ne
from shutil import move
from tabnanny import check
import wave
import numpy as np

wallmat = np.array([[-1, -1, -1, -1, -1, -1], [-1, 0, 0, 0, -1, -1], [-1, -1, 0, -1, -1, -1], [-1, 0, 0, 0, 0, -1], [-1, 0, -1, 0, 0, -1]])
wavemat = np.zeros((6,6))
print(wavemat)

#robotpos = wallmat[0, 0]
#robotpos = 2

#print(wavemat)

robotpos = [0,0]
robotval = 7

wallmat[robotpos[0],robotpos[1]] = robotval
print(wallmat)





###################################################
#backtracking - Meg
###################################################

"""Find shortest path"""
def shortest_path():
    robot_move = wavemat
    m = 0

    """Place robot at start"""
    #robotpos = [0,startc]
    #i = 0
    #j = startc

    """Directions robot can move"""
    north = robot_move[(i+1), j]
    east = robot_move[i, (j+1)]
    south = robot_move[(i-1), j]
    west = robot_move[i, (j-1)]


    """Finding the smallest numeric value for robot path"""
    lst = [north, east, south, west]
    lst_str = [str(x) for x in lst]
    smallest_num = lst.sort()
    smallest = [str(x) for x in smallest_num]


    """Determine where the robot should move"""
    def move_robot(ind):
        if ind == 0:
            """Robot position movement north"""
            robotpos = wavemat[(i+1),j]
            i+=1
        elif ind == 1:
            """Robot position movement east"""
            robotpos = wavemat[i,(j+1)]
            j+=1
        elif ind == 2:
            """Robot position movement south"""
            robotpos = wavemat[(i-1), j]
            i-=1
        else:
            """Robot position movement west"""
            robotpos = wavemat[i, (j-1)]
            j-=1

    def reverse_robot(ind):
        if ind == 0:
            """Reverse robot position movement from north"""
            robotpos = wavemat[(i-1),j]
            i-=1
        elif ind == 1:
            """Reverse robot position movement from east"""
            robotpos = wavemat[i,(j-1)]
            j-=1
        elif ind == 2:
            """Reverse robot position movement from south"""
            robotpos = wavemat[(i+1), j]
            i+=1
        else:
            """Reverse robot position movement from west"""
            robotpos = wavemat[i, (j+1)]
            j+=1

    
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
                next_ind = []
                index_pos = 0
                for i in lst:
                    if check_wall in lst:
                        next_index = lst.index(check_wall, index_pos)
                        next_ind.append(next_index)
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
                next_ind = []
                index_pos = 0
                for i in lst:
                    if check_wall in lst:
                        next_index = lst.index(check_wall, index_pos)
                        next_ind.append(next_index)
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