from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    """
    Return the list in "strange" order:
      - repeatedly take the minimum of the remaining elements,
        then the maximum of the remaining elements, alternating
        until all elements are consumed.

    The input list is NOT mutated.

    Examples:
        >>> strange_sort_list([1, 2, 3, 4])
        [1, 4, 2, 3]
        >>> strange_sort_list([5, 5, 5, 5])
        [5, 5, 5, 5]
        >>> strange_sort_list([])
        []
        >>> strange_sort_list([-3, -1, -2, 0, 2])
        [-3, 2, -2, 0, -1]
    """
    n = len(lst)
    # Handle trivial lengths quickly and without mutating the input.
    if n <= 1:
        # Return a shallow copy to match "do not mutate" and be explicit.
        return lst[:]

    # Sort a COPY in ascending order; do not mutate the caller's list.
    arr = sorted(lst)

    # Two-pointer sweep: low -> current minimum, high -> current maximum.
    low, high = 0, n - 1

    # Start by taking the minimum, then alternate min/max each step.
    take_low = True

    result: List[int] = []

    # Loop until all elements are consumed.
    # Invariant: arr[low:high+1] are exactly the remaining elements in ascending order.
    while low <= high:
        if take_low:
            # Take the minimum of the remaining elements.
            result.append(arr[low])
            low += 1
        else:
            # Take the maximum of the remaining elements.
            result.append(arr[high])
            high -= 1

        # Flip the turn for next iteration.
        take_low = not take_low

    return result


# --- Optional lightweight tests (can be removed in production if not needed) ---
if __name__ == "__main__":
    cases = [
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([2, 1], [1, 2]),
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([5, 5, 5, 5], [5, 5, 5, 5]),
        ([-3, -1, -2, 0, 2], [-3, 2, -2, 0, -1]),
        ([9, 7, 7, 1, 3], [1, 9, 3, 7, 7]),
    ]
    for inp, expected in cases:
        out = strange_sort_list(inp)
        assert out == expected, f"Input: {inp} | Expected: {expected} | Got: {out}"
    print("All tests passed.")
