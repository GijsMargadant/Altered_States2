import math
import functools
import operator
import StatesPopulation


class Matrix:

    def __init__(self, input: str, states_population=None, alturations=1) -> None:
        if not self.__is_valid_input(input):
            raise ValueError(f'Can not make matrix, string length not perfect square: {len(input)}')

        self.input = input
        self.states_population = StatesPopulation.state_populations if states_population == None else states_population
        self.alturations = alturations
        self.solution: list[str] = None
        self.cell_contributions: list[int] = None

    def __is_valid_input(self, str):
        return math.floor(math.sqrt(len(str))) == math.ceil(math.sqrt(len(str)))

    def get_score(self):
        return functools.reduce(operator.add, map(lambda s: self.states_population[s], self.solution), 0)
    
    def get_states(self):
        return self.solution
    
    def get_cell_contributions(self):
        return self.cell_contributions
    
    def get_string(self):
        return self.input
    
    def find_all_present_states(self):
        self.solution = []
        self.cell_contributions = [0] * len(self.input)
        for state in self.__get_possible_states():
            if self.__is_state_present(state):
                self.solution.append(state)
    
    def __get_possible_states(self):
        possible_states = []
        input_chars= set(self.input)
        for state in self.states_population.keys():
            state_chars = set(state)
            diff = state_chars.union(input_chars)
            if len(diff) >= len(state) - self.alturations:
                possible_states.append(state)
        return possible_states
    
    def __is_state_present(self, state):
        result = False
        for i in range(len(self.input)):
            result = self._is_state_present_helper(state, i, self.alturations) or result
        return result
    
    def _is_state_present_helper(self, state: str, cur_cell: int, alterings) -> bool:

        if self.input[cur_cell] == state or (len(state) == 1 and alterings == 1):
            self.cell_contributions[cur_cell] = self.cell_contributions[cur_cell] + 1
            return True
        elif self.input[cur_cell] != state[0] and alterings == 0:
            return False
        elif self.input[cur_cell] != state[0] and alterings > 0:
            alterings = alterings - 1

        state = state[1:]
        result = False
        for i in self.__get_neighbourin_cell_indices(cur_cell, len(self.input)):
            if self._is_state_present_helper(state, i, alterings):
                result = True
                self.cell_contributions[cur_cell] = self.cell_contributions[cur_cell] + 1
        return result

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
