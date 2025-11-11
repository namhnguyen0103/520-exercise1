from typing import List

def make_a_pile(n: int) -> List[int]:
    """
    Build a list of stone counts for a pile with `n` levels.

    The first level has `n` stones. Each subsequent level increases by 2, which
    preserves the parity of `n` (odd stays odd, even stays even). This forms an
    arithmetic progression of length `n`, first term `n`, common difference `2`.

    Parameters
    ----------
    n : int
        Positive integer (>= 1) specifying both the first level size and the
        number of levels.

    Returns
    -------
    List[int]
        A list `levels` where levels[i] = n + 2*i for i in [0, n-1].

    Raises
    ------
    TypeError
        If `n` is not an integer.
    ValueError
        If `n` < 1.

    Examples
    --------
    >>> make_a_pile(3)
    [3, 5, 7]
    >>> make_a_pile(4)
    [4, 6, 8, 10]
    >>> make_a_pile(1)
    [1]
    """
    # --- Input validation (strict policy) ---
    # Ensure the type is exactly int (no silent coercion). This avoids surprises
    # like floats being truncated and keeps API behavior explicit and predictable.
    if not isinstance(n, int):
        raise TypeError(f"n must be an int, got {type(n).__name__}")
    if n < 1:
        raise ValueError("n must be >= 1")

    # --- Sequence generation ---
    # This is an arithmetic progression of length n:
    # term_i (0-indexed) = n + 2*i
    # Complexity: O(n) time, O(n) space.
    levels = [n + 2 * i for i in range(n - 1)]

    # --- Return result ---
    return levels