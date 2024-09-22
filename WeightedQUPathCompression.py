from WeightedQuickUnion import WeightedQuickUnion


class WeightedQUPathCompression(WeightedQuickUnion):

    def _root(self, p: int) -> tuple[int, int]:
        current_element = self.id_array[p]
        counter = 0

        while current_element != self.id_array[current_element]:
            self.id_array[current_element] = self.id_array[self.id_array[current_element]]
            current_element = self.id_array[current_element]
            counter += 1

        return current_element, counter

