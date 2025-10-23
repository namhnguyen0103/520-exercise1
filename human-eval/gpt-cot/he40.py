from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    """
    Return True if there exist three (index-)distinct elements in `l` whose sum is zero.
    Elements may have the same value as long as they are from different indices (e.g., [0,0,0] -> True).

    Examples:
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
    """
    n = len(l)
    if n < 3:
        return False

    nums = sorted(l)  # work on a sorted copy; do not mutate caller's list

    for i in range(n - 2):
        # Small optimization: avoid repeating the same anchor value
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        lo, hi = i + 1, n - 1

        while lo < hi:
            s = nums[lo] + nums[hi]
            if s == target:
                return True  # Found nums[i] + nums[lo] + nums[hi] == 0
            elif s < target:
                lo += 1
            else:
                hi -= 1

    return False
