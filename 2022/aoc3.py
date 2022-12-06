"""Advent of Code 3 solution"""
from string import ascii_letters
from more_itertools import chunked

with open("data/day3.txt", "r", encoding="utf-8") as input_file:
    rucksacks_arr = input_file.read().splitlines()
    rucksacks_split = [
        [s[0 : len(s) // 2], s[len(s) // 2 : len(s)]] for s in rucksacks_arr
    ]
    elf_groups = list(chunked(rucksacks_arr, 3))
    priority = dict(zip(ascii_letters, range(1, 53)))


def duplicate_finder(l: list[str]):
    def condition(compartments: list, letter: str) -> bool:
        result = True
        for compartment in compartments:
            if compartment.count(letter) == 0:
                result = False
        return result

    list_of_dupe = list(set(priority[i] for i in "".join(l) if condition(l, i)))
    return list_of_dupe[0]


rucksacks_dupes = list(map(duplicate_finder, rucksacks_split))
print(sum(rucksacks_dupes))  # solution to part 1
group_dupes = list(map(duplicate_finder, elf_groups))
print(sum(group_dupes))  # solution to part 2
