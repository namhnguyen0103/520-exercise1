from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    """
    Return True iff there exist three distinct elements in the list whose sum is zero.

    This implementation follows the classic "sort + two-pointer" 3-sum pattern:
    - Sort the array (enables pruning and two-pointer sweeps)
    - Fix one value a[i], then scan the remaining range with two pointers (left, right)
    - Early-exit on the first valid triple; otherwise return False after exhaustion

    The indices i < left < right are always distinct, so distinctness is guaranteed.

    Args:
        l: List of integers (may contain negatives, zeros, positives, and duplicates).

    Returns:
        True if a triple summing to zero exists; False otherwise.

    Complexity:
        Time  : O(n^2) in the worst case (sorting is O(n log n), dominated by the scan).
        Space : O(n) due to making a sorted copy (keeps the input list unmodified).

    Examples (doctests):
    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    >>> triples_sum_to_zero([0, 0, 0])
    True
    >>> triples_sum_to_zero([-1, -1, 2])
    True
    """

    # Fast-fail: fewer than 3 items cannot form a triple.
    if len(l) < 3:
        return False

    # Use a *copy* to avoid mutating the caller's list.
    a = sorted(l)
    n = len(a)

    # Iterate each index as the fixed element of the triple.
    for i in range(n - 2):
        x = a[i]

        # Pruning: if the fixed value is > 0, all following values are >= x (sorted),
        # so any sum x + ... + ... will be > 0 and cannot reach 0.
        if x > 0:
            return False

        # Optional optimization: skip duplicate fixed values to reduce redundant scans.
        if i > 0 and a[i] == a[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            s = x + a[left] + a[right]
            if s == 0:
                # Found a valid triple; existence is sufficient.
                return True
            if s < 0:
                # Sum too small; move left forward to increase the total.
                left += 1
                # Optional duplicate-skip on the left pointer.
                while left < right and a[left] == a[left - 1]:
                    left += 1
            else:
                # s > 0: Sum too large; move right backward to decrease the total.
                right -= 1
                # Optional duplicate-skip on the right pointer.
                while left < right and a[right] == a[right + 1]:
                    right -= 1

    # Exhausted all candidates without finding any triple.
    return False
