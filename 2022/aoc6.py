"""Advent of Code 6 solution"""

with open("data/day6.txt", "r", encoding="utf-8") as input_file:
    SIGNAL = input_file.read()
    packet_marker = next(
        i + 4
        for i in range(len(SIGNAL) - 3)
        if len(set(SIGNAL[i : i + 4])) == len(SIGNAL[i : i + 4])
    )
    message_marker = next(
        i + 14
        for i in range(len(SIGNAL) - 13)
        if len(set(SIGNAL[i : i + 14])) == len(SIGNAL[i : i + 14])
    )

print(packet_marker)  # solution to part 1
print(message_marker)  # solution to part 2
