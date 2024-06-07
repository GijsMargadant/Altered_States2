#Altered states

#Make the 5x5 grid by getting the input
import numpy as np
from collections import Counter
#list of states
state_populations = {
    "california": 39538223,
    "texas": 29145505,
    "florida": 21538187,
    "newyork": 20201249,
    "pennsylvania": 13002700,
    "illinois": 12812508,
    "ohio": 11799448,
    "georgia": 10711908,
    "northcarolina": 10439388,
    "michigan": 10077331,
    "newjersey": 9288994,
    "virginia": 8631393,
    "washington": 7693612,
    "arizona": 7151502,
    "massachusetts": 7029917,
    "tennessee": 6910840,
    "indiana": 6785528,
    "missouri": 6154913,
    "maryland": 6177224,
    "wisconsin": 5893718,
    "colorado": 5773714,
    "minnesota": 5706494,
    "southcarolina": 5118425,
    "alabama": 5024279,
    "louisiana": 4657757,
    "kentucky": 4505836,
    "oregon": 4237256,
    "oklahoma": 3959353,
    "connecticut": 3605944,
    "utah": 3271616,
    "iowa": 3190369,
    "nevada": 3104614,
    "arkansas": 3011524,
    "mississippi": 2961279,
    "kansas": 2937880,
    "newmexico": 2117522,
    "nebraska": 1961504,
    "westvirginia": 1793716,
    "idaho": 1839106,
    "hawaii": 1455271,
    "maine": 1362359,
    "newhampshire": 1377529,
    "montana": 1084225,
    "rhodeisland": 1097379,
    "delaware": 989948,
    "southdakota": 886667,
    "northdakota": 779094,
    "alaska": 733391,
    "vermont": 643077,
    "wyoming": 576851
}


def string_to_2d_array(s):
    if len(s) != 25:
        raise ValueError("The string must be exactly 25 characters long.")
    
    # Create the 2D array
    array_2d = []
    for i in range(0, 25, 5):
        row = list(s[i:i+5])
        array_2d.append(row)
    
    return array_2d


def all_or_all_but_one_letters_in_string(short_string, long_string):
    short_counter = Counter(short_string)
    long_counter = Counter(long_string)
    
    missing_count = 0
    
    for char, count in short_counter.items():
        if long_counter[char] < 1: #if not in long string add one to count
            missing_count += 1
        if missing_count > 1:
            return False
    
    return True


#checks the 
def possible_states_in_grid(grid):
    states = []
    for state in state_populations.keys():
        if(all_or_all_but_one_letters_in_string(state, grid)):
            states.append(state)
    return states


def get_total_population(states):
    sum = 0
    for state in states:
        sum += state_populations.get(state)

    return sum


def states_in_grid(grid):
    grid_matrix = string_to_2d_array(grid)
    for state in possible_states_in_grid(grid):
        return

# def state_in_grid(grid, state):
#     i = 0
#     route = []
#     for coordinate in get_start_position(grid,list(state)[0]):
#         print(coordinate)
#         print(coordinate[0], coordinate[1])
#         for c in range(1, len(state)):
#             if king_move(grid, coordinate[0], coordinate[1], list(state)[i]) == False:
#                 return False
        
#             route.append(coordinate)
#             i += 1
#             print("list state i:",list(state)[i] )
#             print(king_move(grid, coordinate[0], coordinate[1], list(state)[i]))
#             for cord in king_move(grid, coordinate[0], coordinate[1], list(state)[i]):
                                  
            
#             if(coordinate == False):
#                 return False
#             if i == len(state)-1:
#                 return route       
#     return False    

def get_start_position(grid, target):
    start_pos = []
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] == target:
                start_pos.append([x,y])
    return start_pos

def king_move(grid, x, y, target):
    moves = []
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i>= 0 and i<len(grid) and j>=0 and j<len(grid) and (not (i==0 and j ==0)):
                if grid[i][j] == target:
                    moves.append([i,j])
    return moves                
        
def recursiontest(grid, state, start_coordinate, i, start_string):
    print("start string: ", start_string)
    if start_string == state:
        return True
    
    else:
        print("target letter:",state[i])
        print("kingmove, grid, x, y, target", grid, start_coordinate[0], start_coordinate[1], state[i], king_move(grid,start_coordinate[0],start_coordinate[1],state[i]))
        for cord in king_move(grid, start_coordinate[0], start_coordinate[1], state[i]):
            start_string = start_string + state[i]
        
                
            print("Kingmove true", king_move(grid, start_coordinate[0], start_coordinate[1], state[i]))
            i += 1
            
            return recursiontest(grid,state,cord,i, start_string)



def find_all_states(grid):
    possible_states = possible_states_in_grid(grid)
    grid = string_to_2d_array(grid)
    all_states = []
    for state in possible_states:
        for coords in get_start_position(grid, state[0]):
            if recursiontest(grid, state, coords,1, state[0]):
                all_states.append(state)

    return all_states
           
st = 'aaska'
print(find_all_states('codhclutaniorkssnabodietl'))
#print("test the recursion:", recursiontest(string_to_2d_array(), 'alaska',[0,0],1, 'a'))
print(possible_states_in_grid('pennsylvanagdeflkjndfhkjljfdghbg'), get_total_population(possible_states_in_grid('pennsylvanagfdghbg')))
