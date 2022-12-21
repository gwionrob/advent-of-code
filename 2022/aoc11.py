"""Advent of Code 11 solution"""
from heapq import nlargest
from math import prod

with open("data/day11test.txt", "r", encoding="utf-8") as input_file:
    input_data = input_file.read().splitlines()
    monkeys = {
        int(input_data[i][7]): {
            "items": [item[:2] for item in input_data[i + 1].split(" ")[4:]],
            "operation": eval(
                input_data[i + 2]
                .lstrip()
                .split(" ", 1)[1]
                .replace("new =", "lambda old:")
            ),
            "test": lambda worry, item, i=i: monkeys[
                int(input_data[i + 4].split(" ")[-1])
            ]["items"].append(worry)
            if worry % int(input_data[i + 3].split(" ")[-1]) == 0
            else monkeys[int(input_data[i + 5].split(" ")[-1])]["items"].append(worry),
            "modulo": lambda item, i=i: item % int(input_data[i + 3].split(" ")[-1]),
        }
        for i in range(0, len(input_data), 7)
    }

inspect_count = {monkey: 0 for monkey in monkeys}
for _ in range(20):
    print(_)
    for i in monkeys:
        inspect_count[i] += len(monkeys[i]["items"])
        original_length = len(monkeys[i]["items"])
        for item in monkeys[i]["items"]:
            worry = monkeys[i]["operation"](int(item)) // 3
            monkeys[i]["test"](worry, item)
        monkeys[i]["items"] = monkeys[i]["items"][original_length:]
print(prod(nlargest(2, inspect_count.values())))  # solution to part 1
inspect_count = {monkey: 0 for monkey in monkeys}
for _ in range(10000):
    print(_)
    for i in monkeys:
        inspect_count[i] += len(monkeys[i]["items"])
        original_length = len(monkeys[i]["items"])
        for item in monkeys[i]["items"]:
            worry = monkeys[i]["operation"](monkeys[i]["modulo"](int(item)))
            monkeys[i]["test"](worry, item)
        monkeys[i]["items"] = monkeys[i]["items"][original_length:]
print(prod(nlargest(2, inspect_count.values())))  # solution to part 2
