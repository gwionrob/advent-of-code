"""Advent of Code 9 solution"""
with open("data/day9.txt", "r", encoding="utf-8") as input_file:
    motions = [direction.split(" ") for direction in input_file.read().splitlines()]


def move(
    model_motion: list[str],
    knots: list[str],
    model_coordinates: dict[str:tuple],
    prev_head_visits: list[tuple],
):
    """Function to apply one motion of the rope, and append coordinates
        if visited coordinates to a dictionary.

    Args:
        model_motion (list): list of strings representing the
        motion to be modelled
        points (list): list of strings representing the
        points of the rope in question
        coordinates (dictionary): dictionary with string key and value tuple
        containing the coordinates of the head and tail of the rope
    Returns:
        void
    """
    direction = model_motion[0]
    step = int(model_motion[1])
    head_visits = (
        prev_head_visits
        if len(prev_head_visits) > 0
        else [
            (
                model_coordinates[knots[0]][0]
                + (i if direction == "R" else -i if direction == "L" else 0),
                model_coordinates[knots[0]][1]
                + (i if direction == "U" else -i if direction == "D" else 0),
            )
            for i in range(1, step + 1)
        ]
    )
    if (
        abs(model_coordinates[knots[1]][0] - head_visits[-1][0]) > 1
        or abs(model_coordinates[knots[1]][1] - head_visits[-1][1]) > 1
    ):
        first_distant_head = next(
            visit
            for visit in head_visits
            if abs(model_coordinates[knots[1]][0] - visit[0]) > 1
            or abs(model_coordinates[knots[1]][1] - visit[1]) > 1
        )
        tail_visits = [
            visit
            for visit in head_visits[:-1]
            if abs(model_coordinates[knots[1]][0] - visit[0]) > 1
            or abs(model_coordinates[knots[1]][1] - visit[1]) > 1
        ]
        if head_visits.index(first_distant_head) == 0:
            tail_visits = [model_coordinates[knots[0]]] + tail_visits
        else:
            tail_visits = [
                head_visits[head_visits.index(first_distant_head) - 1]
            ] + tail_visits
        if len(tail_visits):
            if knots[1] == list(model_coordinates.keys())[-1]:
                for visit in tail_visits:
                    visited_coordinates.add(visit)
            else:
                next_knots = [knots[1], str(int(knots[1]) + 1)]
                move(
                    [direction, str(len(tail_visits))],
                    next_knots,
                    coordinates,
                    tail_visits,
                )
    else:
        pass
    coordinates[knots[0]] = head_visits[-1]
    if "tail_visits" in locals():
        coordinates[knots[1]] = tail_visits[-1]


visited_coordinates = set()
visited_coordinates.add((0, 0))
coordinates = {"H": (0, 0), "T": (0, 0)}
for motion in motions:
    move(motion, ["H", "T"], coordinates, [])
print(len(visited_coordinates))  # solution to part 1
visited_coordinates.clear()
visited_coordinates.add((0, 0))
coordinates = {
    "H": (0, 0),
    "1": (0, 0),
    "2": (0, 0),
    "3": (0, 0),
    "4": (0, 0),
    "5": (0, 0),
    "6": (0, 0),
    "7": (0, 0),
    "8": (0, 0),
    "9": (0, 0),
}
test_motions = [
    ["R", 5],
    ["U", 8],
    ["L", 8],
    ["D", 3],
    ["R", 17],
    ["D", 10],
    ["L", 25],
    ["U", 20],
]
for motion in motions:
    move(motion, ["H", "1"], coordinates, [])
print(len(visited_coordinates))  # yet to solve part 2
