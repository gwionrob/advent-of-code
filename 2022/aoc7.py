"""Advent of Code 7 solution"""
from more_itertools import split_at, collapse

with open("data/day7.txt", "r", encoding="utf-8") as input_file:
    executions = input_file.read().splitlines()
    executions_depth = [
        (
            executions[i],
            sum(
                1
                for exec in executions[:i]
                if exec.startswith("$ cd") and exec[5].isalpha()
            )
            - executions[:i].count("$ cd .."),
        )
        for i in range(len(executions))
    ]
    directories = list(split_at(executions_depth, lambda x: x[0] == "$ ls"))
    dir_list = [
        [
            (
                int(file.split(" ")[0])
                if file.split(" ")[0].isnumeric()
                else file.split(" ")[1]
                if file.split(" ")[1] != "cd"
                else file.split(" ")[2],
                depth,
            )
            for file, depth in dir
        ]
        for dir in directories
    ]
    dir_list = [[(e, d) for e, d in dir if e != ".."] for dir in dir_list]
    dir_list.reverse()
    dir_dict = [
        (
            dir_list[i + 1][-1],
            dir_list[i][:-1] if len(dir_list[i]) != 1 else dir_list[i],
        )
        for i in range(len(dir_list) - 1)
    ]
    dir_sizes = {}
    for directory, sizes in dir_dict:
        sizes_copy = sizes
        for i, size in enumerate(sizes_copy):
            if isinstance(size[0], str):
                sizes_copy[i] = (dir_sizes[size][-1], size[1])
        if directory in dir_sizes:
            dir_sizes[directory].append(sum(s for s, d in sizes_copy))
        else:
            dir_sizes[directory] = [sum(s for s, d in sizes_copy)]

desired_sizes = [i for i in list(collapse(dir_sizes.values())) if i < 100000]
filesysytem_size = dir_sizes[("/", 0)][0]
list_of_all_sizes = list(collapse(dir_sizes.values()))
closest_size = min(
    list_of_all_sizes, key=lambda x: abs(x - (filesysytem_size - 40000000))
)

print(sum(desired_sizes))  # solution to part 1
print(closest_size)  # solution to part 2
