def sum_to_n(n: int) -> int:
    """sum_to_n is a function that sums numbers from 1 to n.
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
    # Use the mathematical formula for the sum of the first n positive integers: n * (n + 1) / 2.
    # The result is guaranteed to be an integer, so integer division (//) can be used,
    # or simple multiplication followed by standard division and type conversion if n can be very large.
    # For standard integer inputs, a simple calculation suffices.
    return n * (n + 1) // 2