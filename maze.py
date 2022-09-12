from cgitb import small
from operator import ne
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

robot_move = wavemat

"""Place robot at start"""
robotpos = start

m = 0

"""Find shortest path"""
def shortest_path():

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

        elif (smallest_num[0] == -1):
            """Check if robot is next to a wall (-1 represents a wall)"""
            check_wall = smallest_num[1]
            i = 1
            while check_wall == -1:
                check_wall = smallest_num[i+1]
                i+=1
                if(i == 3) & (check_wall == -1):
                    print("Boxed in! No way out!")
                    break
            last_val = check_wall

            if (l == 0):
                for i in lst_str:
                    if check_wall in lst_str:
                        next_ind = []
                        next_ind = next_ind.append(lst_str.index(check_wall))
                        len = len(next_ind)

            """Checking if multiple of the same smallest cell values"""
            if (len>1) & (l == 0):
                move_robot(next_ind[m])
                m+1
                l += 1
                pos_vals_rob(l)
                len -= 1
            elif (len>1) & (l>0) & (next_val > last_val):
                reverse_robot(next_ind[m-1])
                move_robot(next_ind[m])
                len -= 1
                m+1
                l += 1
                pos_vals_rob(l)
            else:
                move_robot(next_ind[0])
        
        
        else:
            """If smallest value is not a wall or robot is not next to the goal, then move to the smallest value cell"""


            """Checking if there are multiple of the same smallest value"""
            for i in smallest:
                if i not in 

            robotpos



    pos_vals_rob(0)