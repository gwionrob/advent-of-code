"""Advent of Code 4 solution"""

with open("data/day4.txt", "r", encoding="utf-8") as input_file:
    lines = [[[int(i) for i in k.split("-")] for k in x.split(",")] for x in input_file]

print(
    sum(a <= c <= d <= b or c <= a <= b <= d for (a, b), (c, d) in lines)
)  # solution to part 1
print(
    sum(
        any([a <= c <= b, a <= d <= b, c <= a <= d, c <= b <= d])
        for (a, b), (c, d) in lines
    )
)  # solution to part 2
