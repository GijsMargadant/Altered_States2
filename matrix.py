import numpy as np
from collections import Counter
import math
import functools
import operator
import time


class Matrix:

    def __init__(self, str: str, states_population: dict[str, int]) -> None:
        if not self.is_valid_input(str):
            raise ValueError(f'Can not make matrix, string length not perfect square: {len(str)}')

        self.input = str
        self.states_population = states_population
        self.solution = None

    def is_valid_input(self, str):
        return math.floor(math.sqrt(len(str))) == math.ceil(math.sqrt(len(str)))

    def get_score(self):
        return functools.reduce(operator.add, map(lambda s: self.states_population[s], self.solution), 0)
    
    def get_states(self):
        return self.solution
    
    def find_all_present_states(self, alturations=1):
        self.solution = []
        for state in self.__get_possible_states(alturations):
            if self.__is_state_present(self.input, state, alturations):
                self.solution.append(state)
    
    def __get_possible_states(self, alturations):
        possible_states = []
        input_chars= set(self.input)
        for state in self.states_population.keys():
            state_chars = set(state)
            diff = state_chars.union(input_chars)
            if len(diff) >= len(state) - alturations:
                possible_states.append(state)
        return possible_states
    
    def __is_state_present(self, input: str, state: str, alterings: int) -> bool:
        result = False
        for i in range(0, len(input)):
            result = result or self.__is_state_present_helper(input, state, i, alterings)
        return result
    
    def __is_state_present_helper(self, input: str, state: str, cur_pos: int, alterings: int) -> bool:
        if input[cur_pos] != state[0] and alterings == 0:
            return False
        elif input[cur_pos] != state[0] and alterings > 0:
            alterings = alterings - 1
        elif input[cur_pos] == state:
            return True
        
        state = state[1:]
        for i in self.__get_neighbourin_cell_indices(cur_pos, len(input)):
            if (self.__is_state_present_helper(input, state, i, alterings)):
                return True
        return False


    def __get_neighbourin_cell_indices(self, idx, str_len) -> list[int]:
        mtrx_dim = (int) (math.sqrt(str_len))
        result = []
        m = math.floor(idx / mtrx_dim)
        n = idx % mtrx_dim
        for i in range(max(0, m - 1), min(m + 2, mtrx_dim)):
            for j in range(max(0, n - 1), min(n + 2, mtrx_dim)):
                if i == m and j == n:
                    continue
                result.append(i * mtrx_dim + j)
        return result


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
# input_str = 'alaskxmbxaxxxxxxxxxxxxxxx'
input_str = 'codhclutaniorkssnabodietl'
# input_str = 'thoainesl'
# state_populations = {"ab" : 2, "cd" : 3}
# input_str = 'axxb'
matrix = Matrix(input_str, state_populations)

t0 = time.time()
for i in range(0, 1):
    matrix.find_all_present_states()
t1 = time.time()
print(f'States found ({t1 - t0:.3f} s):\n{matrix.get_states()}\n')
print(f'Score = {matrix.get_score():,}')
