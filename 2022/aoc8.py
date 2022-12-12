"""Advent of Code 8 solution"""
from math import prod

with open("data/day8.txt", "r", encoding="utf-8") as input_file:
    trees = [[int(h) for h in r] for r in [list(i[:-1]) for i in input_file]]
    ROWS = len(trees)
    COLUMNS = len(trees[0])


def visible(row: int, column: int) -> bool:
    """Function to determine whether a tree is visible.

    Args:
        row (int): integer representing a given trees row
        column (int): integer representing a given trees column

    Returns:
        boolean: True if the tree is visible, false if not
    """
    trees_to_edge = [
        trees[row][:column],
        trees[row][column + 1 :],
        [trees[i][column] for i in range(row)],
        [trees[i][column] for i in range(row + 1, len(trees))],
    ]
    return any(map(lambda x: trees[row][column] > max(x), trees_to_edge))


def scenic_score(row: int, column: int) -> int:
    """Function to determine a tree's scenic score.

    Args:
        row (int): integer representing a given trees row
        column (int): integer representing a given trees column

    Returns:
        int representing a tree's scenic score
    """
    trees_to_edge = [
        trees[row][:column],
        trees[row][column + 1 :],
        [trees[i][column] for i in range(row)],
        [trees[i][column] for i in range(row + 1, len(trees))],
    ]
    trees_to_edge[0].reverse()
    trees_to_edge[2].reverse()
    smaller_trees = [
        list(map(lambda tree: tree < trees[row][column], tte)) for tte in trees_to_edge
    ]

    def false_finder(array: list):
        try:
            scenery = len(array[: array.index(False) + 1])
        except ValueError:
            scenery = len(array)
        return scenery

    count_of_visible_trees = [false_finder(tte) for tte in smaller_trees]
    return prod(count_of_visible_trees)


visible_trees = [
    trees[column][row]
    for row in range(ROWS)
    for column in range(COLUMNS)
    if column in [0, ROWS - 1] or row in [0, COLUMNS - 1] or visible(row, column)
]
tree_scenery = [
    scenic_score(row, column) for row in range(ROWS) for column in range(COLUMNS)
]

print(len(visible_trees))  # solution to part 1
print(max(tree_scenery))  # solution to part 2
