from QuickUnion import QuickUnion


class WeightedQuickUnion(QuickUnion):

    def union(self, p: int, q: int) -> None:
        """
        Cost: lg(N)
        """
        p_root, p_height = self._root(p)
        q_root, q_height = self._root(q)
        if p_root == q_root:
            return
        if p_height < q_height:
            self.id_array[p_root] = q_root
        else:
            self.id_array[q_root] = p_root

    def connected(self, p: int, q: int) -> bool:
        """
        Cost: lg(N)
        """
        return self._root(p)[0] == self._root(q)[0]

    def _root(self, p: int) -> tuple[int, int]:
        """
        Cost: lg(N)
        Takes N-1 operations at most in theory, but in weighted option the root is never
        further than lg(N).
        """
        current_element = self.id_array[p]
        counter = 0

        while current_element != self.id_array[current_element]:
            current_element = self.id_array[current_element]
            counter += 1

        return current_element, counter
