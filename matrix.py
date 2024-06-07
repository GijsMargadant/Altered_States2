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

        self.states_population = states_population
        self.mtrx = self.__convert_to_mtrx(str)
        self.possible_states = self.__possible_states_in_grid(str)
        self.max_length = max(map(lambda s: len(s), self.possible_states), default=0)

        # print(f'Possible states:{self.possible_states}\nMatrix:\n{self.mtrx}')


    def is_valid_input(self, str):
        return math.floor(math.sqrt(len(str))) == math.ceil(math.sqrt(len(str)))

    def compute_score(self, states):
        return functools.reduce(operator.add, map(lambda s: self.states_population[s], states))

    def find_unique_states(self):
        flat_mtrx = self.mtrx.flatten()
        stack: list[list[int]] = [[x] for x in range(0, len(flat_mtrx))]
        found_states = []

        while stack:
            address = stack.pop()
            if len(address) > self.max_length:
                continue
            
            name = self.__convert_address_to_string(address, flat_mtrx)

            if not self.__is_name_possible(name):
                continue

            state = self.__get_matching_state(name)
            if state:
                found_states.append({"name": state, "address": address})

            stack.extend(self.__get_new_addresses(address))
            
        # print(f'Found the following states:\n{found_states}')
        return set(map(lambda s: s["name"], found_states))


    def __is_name_possible(self, name):
        # return len(list(filter(lambda s: s.startswith(name), self.possible_states))) > 0
        return len(list(filter(lambda s: self.__is_similar(name, s[0:len(name)]), self.possible_states))) > 0

    
    
    def __get_matching_state(self, name):
        state = list(filter(lambda s: self.__is_similar(name, s), self.possible_states))
        if len(state) > 0:
            return state.pop()
        else:
            return None


    def __is_similar(self, str1, str2):
        try:
            zip_list = zip([x for x in str1], [y for y in str2], strict=True)
            return len(list(filter(lambda p: p[0] != p[1], zip_list))) <= 1
        except ValueError:
            return False

    def __get_new_addresses(self, address):
        result = []
        m, n = self.get_2d_pos_of_last_index(address)
        for i in range(max(0, m - 1), min(m + 2, self.mtrx.shape[0])):
            for j in range(max(0, n - 1), min(n + 2, self.mtrx.shape[0])):
                if i == m and j == n:
                    continue
                new_address = address.copy()
                new_address.append(i * self.mtrx.shape[0] + j)
                result.append(new_address)
        return result


    def get_2d_pos_of_last_index(self, address):
        m = math.floor(address[-1] / self.mtrx.shape[0])
        n = address[-1] % self.mtrx.shape[0]
        return m,n
                    

    def __convert_address_to_string(self, address: list[int], flat_mtrx: np.array):
        chars = map(lambda i: flat_mtrx[i], address)
        return functools.reduce(operator.add, chars)


    def __possible_states_in_grid(self, grid) -> list[str]:
        states = []
        for state in self.states_population.keys():
            if(self.__all_or_all_but_one_letters_in_string(state, grid)):
                states.append(state)

        return states
    

    def __convert_to_mtrx(self, str) -> np.array:
        array = np.array(list(str))
        k = (int) (math.sqrt(len(str)))
        return array.reshape(-1, k)


    def __all_or_all_but_one_letters_in_string(self, short_string, long_string) -> bool:
        short_counter = Counter(short_string)
        long_counter = Counter(long_string)
        
        missing_count = 0
        
        for char, count in short_counter.items():
            if long_counter[char] < 1: #if not in long string add one to count
                missing_count += 1
            if missing_count > 1:
                return False
        
        return True
    

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
# # input_str = 'alaskxmbxaxxxxxxxxxxxxxxx'
input_str = 'codhclutaniorkssnabodietl'
# input_str = 'thoainesl'
# # state_populations = {"ab" : 2, "cd" : 3}
# # input_str = 'axxb'
matrix = Matrix(input_str, state_populations)

t0 = time.time()
for i in range(0, 1):
    states = matrix.find_unique_states()
t1 = time.time()
print(f'States found ({t1 - t0:.3f} s):\n{states}\n')
score = matrix.compute_score(states)
print(f'Score = {score:,}')
