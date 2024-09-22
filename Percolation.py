from WeightedQUPathCompression import WeightedQUPathCompression


class Percolation(WeightedQUPathCompression):

    # creates n-by-n grid, with all sites initially blocked
    def __init__(self, n: int) -> None:
        if n <= 0:
            raise ValueError()
        self.size = n
        self.open_sites_count = 0
        self.number_of_elements = (n ** 2) + 2  # last two elements - upper and lower virtual points
        super().__init__(self.number_of_elements)
        self.grid = [[False for _ in range(n)] for _ in range(n)]

    # opens the site (row, col) if it is not open already
    def open_(self, row: int, col: int) -> None:
        self._validate_coordinates(row, col)
        if not self.grid[row][col]:
            self.grid[row][col] = True
            this_cell_index = self._get_i(row, col)
            for neighbour_open_cell in self._get_neighbour_open_cells(row, col):
                self.union(this_cell_index, neighbour_open_cell)
            self.open_sites_count += 1

    # is the site (row, col) open?
    def is_open(self, row: int, col: int) -> bool:
        self._validate_coordinates(row, col)
        return self.grid[row][col]

    # is the site (row, col) full?
    def is_full(self, row: int, col: int) -> bool:
        self._validate_coordinates(row, col)
        return self.connected(self.number_of_elements - 2, self._get_i(row, col))

    # returns the number of open sites
    def number_of_open_sites(self) -> int:
        return self.open_sites_count

    # does the system percolate?
    def percolates(self) -> bool:
        return self.connected(self.number_of_elements - 2, self.number_of_elements - 1)

    def _get_neighbour_open_cells(self, row: int, col: int) -> list[int]:
        result = []
        # get upper cell
        if row > 0 and self.grid[row - 1][col]:
            result.append(self._get_i(row - 1, col))
        # get lower cell
        if row < self.size - 1 and self.grid[row + 1][col]:
            result.append(self._get_i(row + 1, col))
        # get left cell
        if col > 0 and self.grid[row][col - 1]:
            result.append(self._get_i(row, col - 1))
        # get right cell
        if col < self.size - 1 and self.grid[row][col + 1]:
            result.append(self._get_i(row, col + 1))
        # if upper row, connect to upper virtual point
        if row == 0:
            result.append(self.number_of_elements - 2)
        # if lower row, connect to lower virtual point
        if row == self.size - 1:
            result.append(self.number_of_elements - 1)
        return result

    def _get_i(self, row: int, col: int) -> int:
        return row * self.size + col

    def _validate_coordinates(self, row: int, col: int) -> None:
        if row < 0 or col < 0 or row > self.size or col > self.size:
            raise ValueError()

    def _print_grid(self):
        for row in self.grid:
            print("\t".join(map(lambda x: str(x), row)))
        print("\n")


if __name__ == "__main__":
    solver = Percolation(10)
