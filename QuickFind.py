from UnionFind import UnionFindBase


class QuickFind(UnionFindBase):

    def __init__(self, n: int) -> None:
        """
        Cost: N
        :param n:
        """
        self.id_array = [i for i in range(n)]

    def union(self, p: int, q: int) -> None:
        """
        Cost: N
        too expensive
        :param p:
        :param q:
        :return:
        """
        p_id = self.id_array[p]
        q_id = self.id_array[q]
        for i, id_ in enumerate(self.id_array):
            if id_ == q_id:
                self.id_array[i] = p_id

    def connected(self, p: int, q: int) -> bool:
        """
        Cost: 1
        :param p:
        :param q:
        :return:
        """
        return self.id_array[p] == self.id_array[q]
