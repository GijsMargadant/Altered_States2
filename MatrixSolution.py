from TabuSearch import Solution
from Matrix import Matrix
import random
import string

class MatrixSolution(Solution):

    def __init__(self, input: str, random = random) -> None:
        super().__init__()
        self.matrix = Matrix(input)
        self.matrix.find_all_present_states()

    def get_mtrx(self) -> Matrix:
        return self.matrix

    def get_obj_val(self) -> float:
        return self.matrix.get_score()

    def perform_exploitation(self) -> 'MatrixSolution':
        old_str = self.matrix.get_string()
        contributions = self.matrix.get_cell_contributions()
        i = contributions.index(min(contributions))
        new_str = self.__replace_nth_char(old_str, i, random.choice(string.ascii_lowercase))
        return MatrixSolution(new_str)

    def perform_exploration(self) -> 'MatrixSolution':
        old_str = self.matrix.get_string()
        new_str = self.__replace_nth_char(old_str, random.randint(0, len(old_str) - 1), random.choice(string.ascii_lowercase))
        return MatrixSolution(new_str)

    def __replace_nth_char(self, string, n, c):
        assert 0 <= n and n < len(string)
        return string[0:n] + c + string[n + 1:]