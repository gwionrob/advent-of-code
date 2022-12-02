"""Advent of Code 2 solution"""

with open("input", "r", encoding="utf-8") as input_file:

    strategy: str = input_file.read()

strategy_arr = strategy.splitlines()


def result(game: str) -> int:
    """Get the resulting points from given rock, paper, scissors game

    Args:
        game: str representing a rps game

    Returns:
        int: integer representing the score from the game

    """
    elf_choice = game[0]
    our_choice = game[-1]
    score = 0
    if our_choice == "X":
        if elf_choice == "A":
            score += 4
        elif elf_choice == "B":
            score += 1
        else:
            score += 7
    elif our_choice == "Y":
        if elf_choice == "A":
            score += 8
        elif elf_choice == "B":
            score += 5
        else:
            score += 2
    else:
        if elf_choice == "A":
            score += 3
        elif elf_choice == "B":
            score += 9
        else:
            score += 6
    return score


print(sum(list(map(result, strategy_arr))))  # solution to part 1


def best_strat_result(game: str) -> int:
    """Get the resulting points from given rock, paper, scissors game
        as per the best strategy

    Args:
        game: str representing a rps game

    Returns:
        int: integer representing the score from the game

    """
    elf_choice = game[0]
    our_choice = game[-1]
    score = 0
    if our_choice == "X":
        if elf_choice == "A":
            score += 3
        elif elf_choice == "B":
            score += 1
        else:
            score += 2
    elif our_choice == "Y":
        if elf_choice == "A":
            score += 4
        elif elf_choice == "B":
            score += 5
        else:
            score += 6
    else:
        if elf_choice == "A":
            score += 8
        elif elf_choice == "B":
            score += 9
        else:
            score += 7
    return score


print(sum(list(map(best_strat_result, strategy_arr))))  # solution to part 2
