def sum_to_n(n: int) -> int:
    """sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): Positive integer (n >= 1).

    Returns:
        int: The sum 1 + 2 + ... + n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Examples:
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    # if not isinstance(n, int):
    #     raise TypeError("n must be an integer")
    if n < 1:
        raise ValueError("n must be >= 1 to sum from 1 to n")

    # Arithmetic series formula; use integer math to avoid floats.
    return n * (n + 1) // 2
