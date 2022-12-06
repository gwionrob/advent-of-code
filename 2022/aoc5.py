"""Advent of Code 5 solution"""

with open("data/day5.txt", "r", encoding="utf-8") as input_file:
    lines = input_file.read().splitlines()
    ship = lines[: lines.index("") - 1]
    steps = [
        [int(step.split(" ")[i]) for i in range(1, 7, 2)]
        for step in lines[lines.index("") + 1 :]
    ]
    cargo = [
        "".join([c[i] for c in ship]).lstrip() for i in range(1, (len(ship) + 1) * 4, 4)
    ]


def crane_instructions(stock, instruction, one_by_one):
    crates_to_move = stock[instruction[1] - 1][: instruction[0]]
    stock[instruction[1] - 1] = stock[instruction[1] - 1][instruction[0] :]
    stock[instruction[2] - 1] = (
        crates_to_move[:: (1 if one_by_one else -1)] + stock[instruction[2] - 1]
    )


for step in steps:
    crane_instructions(cargo, step, False)
print("".join([s[0] for s in cargo]))  # solution to part 1
cargo = [
    "".join([c[i] for c in ship]).lstrip() for i in range(1, (len(ship) + 1) * 4, 4)
]
for step in steps:
    crane_instructions(cargo, step, True)
print("".join([s[0] for s in cargo]))  # solution to part 2
