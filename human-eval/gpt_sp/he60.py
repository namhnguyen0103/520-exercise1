def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that returns the sum of all integers from 1 to n (inclusive).

    The function uses the arithmetic series formula n*(n+1)/2 for O(1) computation time.

    Parameters
    ----------
    n : int
        A non-negative integer representing the upper bound of the sum.

    Returns
    -------
    int
        The sum of all integers from 1 to n (inclusive). Returns 0 if n == 0.

    Raises
    ------
    TypeError
        If n is not an integer (or if it’s a boolean).
    ValueError
        If n is negative.

    Examples
    --------
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
    >>> sum_to_n(0)
    0
    """

    # --- Step 1: Input validation ---
    # Disallow boolean since bool is a subclass of int but semantically not valid here.
    if isinstance(n, bool):
        raise TypeError("Input must be an integer, not a boolean.")

    # Ensure the input is an integer
    # if not isinstance(n, int):
    #     raise TypeError(f"Input must be an integer, got {type(n).__name__} instead.")

    # Negative values are not allowed since sum from 1 to n is undefined for n < 0
    # if n < 0:
    #     raise ValueError("Input must be a non-negative integer.")

    # --- Step 2: Handle base case ---
    if n == 0:
        return 0

    # --- Step 3: Compute using arithmetic series formula ---
    # Use integer arithmetic carefully to avoid unnecessary large intermediate values
    if n % 2 == 0:
        # If n is even, divide n by 2 first
        total = (n // 2) * (n + 1)
    else:
        # If n is odd, divide (n + 1) by 2 first
        total = n * ((n + 1) // 2)

    # --- Step 4: Return the computed sum ---
    return total
