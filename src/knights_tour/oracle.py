from typing import List

BOARD_SIZE = 8

def is_valid_tour(tour: List[int]) -> bool:

    check_tour_structure(tour)
    current = tour[0]

    for i, step in enumerate(tour[1:]):
        if step not in valid_next_positions(current):
            print(f"Step {i} from position {current} to {step} is not a Knight's move.")
            return False

        current = step

    print("Provided tour is valid!")
    return True

def check_tour_structure(tour: List[int]):
    """Ensures the tour has the correnct representation."""
    err_msg = ("Knight's tour must be represented as a list of integers of "
               "length 64. Each item must be a number between 0 and 63, "
               "inclusive and must be unique.")
    if not isinstance(tour, list):
        raise ValueError(err_msg + " Not a list.")

    if len(tour) != BOARD_SIZE**2:
        raise ValueError(err_msg + f" Tour length: {len(tour)}")

    mask = [False] * BOARD_SIZE**2
    for i, step in enumerate(tour):
        if not isinstance(step, int):
            raise ValueError(err_msg + f" Step {step} at index {i} is {type(step)} instead of int")

        if mask[i]:
            raise ValueError(err_msg + f" Step {step} at index {i} occurs more than once.")
        mask[i] = True

def valid_next_positions(position: int) -> List[int]:
    """Get's a list of valid next positions"""
    row, col = position // BOARD_SIZE, position % BOARD_SIZE

    moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    positions = []
    for row_change, col_change in moves:
        if 0 <= row + row_change < BOARD_SIZE and 0 <= col + col_change < BOARD_SIZE:
            positions.append(8 * (row + row_change) + (col + col_change))

    return positions
