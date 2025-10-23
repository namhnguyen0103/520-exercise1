from typing import Iterable, Optional
import math

def next_smallest(lst: Iterable[int]) -> Optional[int]:
    """
    Return the second smallest *distinct* integer in `lst`.
    If there is no such element (e.g., list too short or all values equal), return None.

    The function does not mutate `lst` and operates in a single pass with O(1) extra space.

    Definitions:
    - Let `m1` be the smallest distinct value.
    - Let `m2` be the smallest distinct value strictly greater than `m1`.
    - Return `m2` if it exists; else return None.

    Examples:
    >>> next_smallest([1, 2, 3, 4, 5])
    2
    >>> next_smallest([5, 1, 4, 3, 2])
    2
    >>> next_smallest([])
    >>> next_smallest([1, 1])
    >>> next_smallest([2, 2, 3])
    3
    >>> next_smallest([-1, -5, -5, -2])
    -2

    Complexity:
    - Time: O(n) for n = len(lst), single pass
    - Space: O(1) auxiliary
    """

    # Sentinels representing +∞ to initialize the two minima.
    # Using float('inf') keeps comparisons valid against ints in Python.
    first = math.inf   # smallest distinct value seen so far
    second = math.inf  # second smallest distinct value (> first)

    # Iterate once and maintain the two minima with strict ordering.
    for x in lst:
        # If type robustness is desired, uncomment:
        # if not isinstance(x, int):
        #     raise TypeError(f"All elements must be int, got {type(x).__name__}")

        if x < first:
            # New global minimum found: demote previous `first` to `second`
            second = first
            first = x
        elif first < x < second:
            # x is strictly greater than `first` but smaller than current `second`
            second = x
        # else: ignore (covers x == first and x >= second)

    # If `second` was never updated to a finite number, no valid second minimum exists.
    return None if second is math.inf else int(second)


# ---------------------------
# Basic self-checks (optional)
# ---------------------------
if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5], 2),
        ([5, 1, 4, 3, 2], 2),
        ([], None),
        ([1, 1], None),
        ([2], None),
        ([2, 2, 3], 3),
        ([3, 2, 2], 3),
        ([2, 3, 2, 4, 4, 5], 3),
        ([-1, -5, -5, -2], -2),
        ([7, 7, 7, 7], None),
        ([0, 1], 1),
        ([-10, -10, -9], -9),
        ([5, 1, 1, 1], 5),
    ]

    for arr, expected in tests:
        result = next_smallest(arr)
        assert result == expected, f"next_smallest({arr}) -> {result}, expected {expected}"
    print("All tests passed.")
