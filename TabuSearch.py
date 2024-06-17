from abc import ABC, abstractmethod
from progressbar import progressbar

class TabuSearch:

    def __init__(self, max_iter, exploitation, exploration) -> None:
        self.max_iter = max_iter
        self.exploitation = exploitation
        self.exploration = exploration
        self.is_exploitation_phase = True

    def search(self, initial_solution: 'Solution') -> 'Solution':
        cur_sol = initial_solution
        best_sol = cur_sol
        self.iter_temp = 0
        for iter in progressbar(range(self.max_iter)):
            cur_sol = self.__perform_exploitation_exploration(cur_sol)
            best_sol = self.__get_best_sol(cur_sol, best_sol)
            self.__update_exploitation_exploration()
        return best_sol

    def __get_best_sol(self, sol_a: 'Solution', sol_b: 'Solution') -> 'Solution':
        if sol_a.get_obj_val() > sol_b.get_obj_val():
            return sol_a
        else:
            return sol_b

    def __perform_exploitation_exploration(self, sol: 'Solution') -> 'Solution':
        if self.is_exploitation_phase:
            return sol.perform_exploitation()
        else:
            return sol.perform_exploration()

    def __update_exploitation_exploration(self):
        self.iter_temp = self.iter_temp + 1
        if self.__is_exploration_exploitation_limit_reached():
            self.is_exploitation_phase = not self.is_exploitation_phase
            self.iter_temp = 0

    def __is_exploration_exploitation_limit_reached(self):
        is_exploitation_phase = self.iter_temp == self.exploitation and self.is_exploitation_phase
        is_exploration_phase = self.iter_temp == self.exploration and not self.is_exploitation_phase
        return is_exploitation_phase or is_exploration_phase

class Solution(ABC):
    @abstractmethod
    def get_obj_val(self) -> float:
        pass

    @abstractmethod
    def perform_exploitation(self) -> 'Solution':
        pass

    @abstractmethod
    def perform_exploration(self) -> 'Solution':
        pass