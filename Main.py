from TabuSearch import TabuSearch
from Matrix import Matrix
from MatrixSolution import MatrixSolution as Solution
import numpy as np
import random
import string

random.seed(1234)
exploitation_iter = 10
exploration_iter = 2
max_iter = 1500

str = cur_sol = ''.join(random.choices(string.ascii_lowercase, k=25))
initial_solution = Solution(str)
ts = TabuSearch(max_iter, exploitation_iter, exploration_iter)
solution: Solution = ts.search(initial_solution)

def list_to_mtrx(ls: list):
    arr = np.array(ls)
    mtrx = np.reshape(arr, ((int)(len(ls) ** 0.5), -1))
    return mtrx

mtrx: Matrix = solution.get_mtrx()
print(f'solved!\nScore = {mtrx.get_score():,}')
print(f'States: {mtrx.get_states()}')
print(f'Cell contributions:\n{list_to_mtrx(mtrx.get_cell_contributions())}')
print(f'Solution:\n{list_to_mtrx(list(mtrx.get_string()))}')
print(mtrx.get_string())