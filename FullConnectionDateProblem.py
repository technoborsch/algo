from os import PathLike
from datetime import datetime

from WeightedQUPathCompression import WeightedQUPathCompression


class FullConnectionDateProblem(WeightedQUPathCompression):

    def __init__(self, number_of_participants: int, log_file_path: PathLike) -> None:
        super().__init__(number_of_participants)
        self.file_path = log_file_path
        self.roots_counter = number_of_participants

    def solve(self) -> datetime:
        with open(self.file_path, "r") as f:
            for line in f.readlines():
                split_line = line.split(" ")
                first = int(split_line[1])
                second = int(split_line[2])
                self.union(first, second)
                if self.roots_counter == 1:
                    return datetime.fromtimestamp(int(split_line[0]))

    def union(self, p: int, q: int) -> None:
        super().union(p, q)
        self.roots_counter -= 1
