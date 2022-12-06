"""Advent of Code 6 solution"""

with open("data/day6.txt", "r", encoding="utf-8") as input_file:
    SIGNAL = input_file.read()
    packet_marker = next(
        SIGNAL[i : i + 4]
        for i in range(0, len(SIGNAL) - 5)
        if len(set(SIGNAL[i : i + 4])) == len(SIGNAL[i : i + 4])
    )
    message_marker = next(
        SIGNAL[i : i + 14]
        for i in range(0, len(SIGNAL) - 15)
        if len(set(SIGNAL[i : i + 14])) == len(SIGNAL[i : i + 14])
    )

print(SIGNAL.index(packet_marker) + 4)  # solution to part 1
print(SIGNAL.index(message_marker) + 14)  # solution to part 2
