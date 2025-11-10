from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    """
    Return the list in 'strange' order:
    start with the minimum, then maximum of remaining, then next minimum, etc.

    Examples:
    >>> strange_sort_list([1, 2, 3, 4])
    [1, 4, 2, 3]
    >>> strange_sort_list([5, 5, 5, 5])
    [5, 5, 5, 5]
    >>> strange_sort_list([])
    []
    """
    n = len(lst)
    if n <= 1:
        return lst[:]  # return a shallow copy for consistency

    arr = sorted(lst)
    res: List[int] = []

    i, j = 0, n - 1
    take_min = True
    while i <= j:
        if take_min:
            res.append(arr[i])
            i += 1
        else:
            res.append(arr[j])
            j -= 1
        take_min = not take_min

    return res
