def make_a_pile(n: int) -> list[int]:
    """
    Return a list of length n where the i-th element (1-indexed) is n + 2*(i-1).
    This creates n levels starting at n and increasing by 2 each time (parity preserved).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    >>> make_a_pile(4)
    [4, 6, 8, 10]
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    return [n + 2 * i for i in range(n - 1)]
