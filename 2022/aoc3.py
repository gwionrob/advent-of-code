"""Advent of Code 3 solution"""
import string

with open("data/day3.txt", "r", encoding="utf-8") as input_file:

    rucksacks: str = input_file.read()

rucksacks_arr = rucksacks.splitlines()
priority = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53)))


def splitter(s: str):
    midpoint = len(s) // 2
    first_half = s[0:midpoint]
    second_half = s[midpoint : len(s)]
    return [first_half, second_half]


rucksacks_split = list(map(splitter, rucksacks_arr))


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

elf_groups = []

for i in range(0, len(rucksacks_arr), 3):
    elf_groups.append([rucksacks_arr[i], rucksacks_arr[i + 1], rucksacks_arr[i + 2]])

group_dupes = list(map(duplicate_finder, elf_groups))

print(sum(group_dupes))  # solution to part 2
