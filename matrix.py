import math
import functools
import operator
import time
import StatesPopulation


class matrix:

    def __init__(self, str: str) -> None:
        if not self.__is_valid_input(str):
            raise ValueError(f'Can not make matrix, string length not perfect square: {len(str)}')

        self.input = str
        self.states_population = StatesPopulation.state_populations
        self.solution = None

    def __is_valid_input(self, str):
        return math.floor(math.sqrt(len(str))) == math.ceil(math.sqrt(len(str)))

    def get_score(self):
        return functools.reduce(operator.add, map(lambda s: self.states_population[s], self.solution), 0)
    
    def get_states(self):
        return self.solution
    
    def get_string(self):
        return self.input
    
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
        
        if not state or input[cur_pos] == state:
            return True
        elif input[cur_pos] != state[0] and alterings == 0:
            return False
        elif input[cur_pos] != state[0] and alterings > 0:
            alterings = alterings - 1
        
        
        state = state[1:]
        for i in self.__get_neighbourin_cell_indices(cur_pos, len(input)):
            if (self.__is_state_present_helper(input, state, i, alterings)):
                return True
        return False

    def __get_neighbourin_cell_indices(self, idx, str_len):
        mtrx_dim = int(str_len ** 0.5)
        result = []
        m = idx // mtrx_dim
        n = idx % mtrx_dim
        m_start = max(0, m - 1)
        m_end = min(m + 2, mtrx_dim)
        n_start = max(0, n - 1)
        n_end = min(n + 2, mtrx_dim)
        
        for i in range(m_start, m_end):
            for j in range(n_start, n_end):
                if i != m or j != n:
                    result.append(i * mtrx_dim + j)
                    
        return result
