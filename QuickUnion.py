from UnionFind import UnionFindBase


class QuickUnion(UnionFindBase):
    """
    As a result, it is expensive to keep the tree flat (in array)
    """

    def __init__(self, n):
        """
        Cost: N
        :param n:
        """
        self.id_array = [i for i in range(n)]

    def union(self, p: int, q: int) -> None:
        """
        Cost: best case 1, worst case N

        Too expensive
        :param p:
        :param q:
        :return:
        """
        p_root = self._root(p)
        q_root = self._root(q)
        self.id_array[p_root] = q_root

    def connected(self, p: int, q: int) -> bool:
        """
        Cost: best case 1, worst case N
        :param p:
        :param q:
        :return:
        """
        return self._root(p) == self._root(q)

    def _root(self, p: int) -> int:
        """
        Gets index of root for element with index p
        :param p:
        :return:
        """
        current_element = p
        while current_element != self.id_array[current_element]:
            current_element = self.id_array[current_element]
        return current_element
