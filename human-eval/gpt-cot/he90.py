from math import inf
from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    """
    Return the 2nd smallest *distinct* element of lst.
    Return None if it does not exist.
    Examples:
        next_smallest([1, 2, 3, 4, 5]) == 2
        next_smallest([5, 1, 4, 3, 2]) == 2
        next_smallest([]) == None
        next_smallest([1, 1]) == None
    """
    if not lst:
        return None

    m1, m2 = inf, inf  # m1 = smallest, m2 = second-smallest distinct

    for x in lst:
        if x < m1:
            m1, m2 = x, m1
        elif m1 < x < m2:
            m2 = x
        # else: x == m1 or x >= m2 → no update

    return None if m2 is inf else m2


# Quick self-checks
if __name__ == "__main__":
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) is None
    assert next_smallest([1, 1]) is None
    assert next_smallest([2, 2, 3]) == 3
    assert next_smallest([7, 7, 7, 7]) is None
