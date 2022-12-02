"""Advent of Code 1 solution"""

with open("data/day1.txt", "r", encoding="utf-8") as input_file:

    calories: str = input_file.read()

calories_arr = calories.splitlines()

elves = []
START_OF_ELF = 0

for i in range(0, len(calories_arr) - 1):
    if calories_arr[i] == "":
        elves.append(sum(list(map(int, calories_arr[START_OF_ELF:i]))))
        START_OF_ELF = i + 1

print(max(elves))  # solution to part 1

elves.sort()

print(sum(elves[-3:]))  # solution to part 2
