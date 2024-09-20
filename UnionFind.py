from abc import ABC, abstractmethod


class UnionFindBase(ABC):

    @abstractmethod
    def __init__(self, n: int) -> None:
        """
        Initializes union-find structure with n objects (0 to n-1)
        :param int n: number of objects
        """

    @abstractmethod
    def union(self, p: int, q: int) -> None:
        """
        Adds connection between p and q
        :param int p: index of first point to connect
        :param int q: index of second point to connect
        :return: None
        """

    @abstractmethod
    def connected(self, p: int, q: int) -> bool:
        """
        Method to check if the element with index p is connected to the element with index q
        :param int p: index of first point to check connection
        :param int q: index of second point to check connection
        :return: boolean value that says
        """
