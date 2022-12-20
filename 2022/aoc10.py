"""Advent of Code 10 solution"""
with open("data/day10.txt", "r", encoding="utf-8") as input_file:
    instructions = [
        instruction.split(" ") for instruction in input_file.read().splitlines()
    ]

cycle_execution = {}
for cycle, i in enumerate(instructions, 1):
    instruction_type = i[0]
    VALUE = 0 if instruction_type == "noop" else int(i[1])
    if len(cycle_execution) == 0:
        cycle_execution[cycle + (0 if VALUE == 0 else 1)] = VALUE
    else:
        cycle_execution[
            list(cycle_execution.keys())[-1] + (1 if VALUE == 0 else 2)
        ] = VALUE
X = 1
SIGNAL_STRENGTH = 0
CRT = ""
for cycle in range(1, list(cycle_execution.keys())[-1] + 1):
    if (cycle - 20) % 40 == 0 and cycle <= 220:
        SIGNAL_STRENGTH += cycle * X
    if (cycle - 1) % 40 in range(X - 1 % 40, X + 2 % 40):
        CRT += "#"
    else:
        CRT += "."
    if cycle in cycle_execution:
        X += cycle_execution[cycle]
print(SIGNAL_STRENGTH)  # solution to part 1
crt_rows = [CRT[i : i + 40] for i in range(0, len(CRT), 40)]
print(*crt_rows, sep="\n")  # solution to part 2
