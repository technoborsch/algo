import random
import os

from timing_decorator import timer

from UnionFind import UnionFindBase
from QuickFind import QuickFind
from QuickUnion import QuickUnion
from WeightedQuickUnion import WeightedQuickUnion
from WeightedQUPathCompression import WeightedQUPathCompression


def generate_test_case() -> None:
    with open("testcase.txt", "w") as f:
        number_of_elements = 10_000_000
        number_of_unions = 9_000_000
        f.write(f"{number_of_elements}\n")
        for i in range(number_of_unions):
            first_node = random.randint(0, number_of_elements - 1)
            second_node = random.randint(0, number_of_elements - 1)
            f.write(f"{first_node} {second_node}\n")

@timer
def test(union_find_class: type[UnionFindBase]) -> None:
    with open("testcase.txt", "r") as f:
        number_of_elements = int(f.readline())
        union_find_object = union_find_class(number_of_elements)

        for line in f.readlines():
            a, b = map(lambda x: int(x), line.split(" "))
            union_find_object.union(a, b)

        for _ in range(1000):
            a = random.randint(0, number_of_elements - 1)
            b = random.randint(0, number_of_elements - 1)
            union_find_object.connected(a, b)


if __name__ == "__main__":
    generate_test_case()
    for class_ in [
        # QuickFind,
        # QuickUnion,
        WeightedQuickUnion,
        WeightedQUPathCompression
    ]:
        print(f"Class {class_.__name__} result:")
        test(class_)
    os.remove("testcase.txt")
