"""Small calculator used in the tutorial."""


def calculate_average(numbers):
    """Calculate the arithmetic mean of a non-empty list.

    Raises ValueError when the input list is empty.
    """
    if not numbers:
        raise ValueError("numbers must not be empty")
    return sum(numbers) / len(numbers)
