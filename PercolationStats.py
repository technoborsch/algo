import random

from Percolation import Percolation


class PercolationStats:

    # perform independent trials on an n-by-n grid
    def __init__(self, n: int, trials: int):
        self.n = n
        self.trials = trials
        self.results = []
        self.mean_value = None
        self.stddev_value = None
        self._run()

    # sample mean of percolation threshold
    def mean(self) -> float:
        total = 0
        for result in self.results:
            total += result
        mean = total / self.trials
        self.mean_value = mean
        return mean

    # sample standard deviation of percolation threshold
    def stddev(self) -> float:
        total = 0
        if not self.mean_value:
            self.mean()
        for result in self.results:
            total += (result - self.mean_value) ** 2
        stddev = total / (self.trials - 1)
        self.stddev_value = stddev
        return stddev

    # low endpoint of 95% confidence interval
    def confidence_lo(self) -> float:
        return self.mean_value - self._deviation()

    # high endpoint of 95% confidence interval
    def confidence_hi(self) -> float:
        return self.mean_value + self._deviation()

    def _deviation(self) -> float:
        if not self.stddev:
            self.stddev()
        return (1.96 * (self.stddev_value ** 0.5)) / (self.trials ** 0.5)

    def _run(self):
        for _ in range(self.trials):
            percolation = Percolation(self.n)
            while not percolation.percolates():
                row = random.randint(0, self.n - 1)
                col = random.randint(0, self.n - 1)
                if not percolation.is_open(row, col):
                    percolation.open_(row, col)
            self.results.append(percolation.number_of_open_sites() / (self.n ** 2))
        print(f"mean\t= {self.mean()}")
        print(f"stddev\t= {self.stddev()}")
        print(f"95% confidence interval\t= [{self.confidence_lo()} {self.confidence_hi()}]")

if __name__ == "__main__":
    perc_stats = PercolationStats(200, 1000)
