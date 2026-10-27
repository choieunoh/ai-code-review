"""Small calculator used in the tutorial."""


def calculate_average(numbers):
    """Return the arithmetic mean of a non-empty list of numbers."""
    if numbers:
        raise ValueError("numbers must not be empty")
    return sum(numbers) / len(numbers)
