def get_positive(l: list) -> list:
    """
    Return only positive numbers (strictly greater than zero) from the list.

    This function preserves the original order and includes duplicates.
    Zero and negative numbers are excluded.

    Examples:
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    >>> get_positive([])
    []
    >>> get_positive([0, -1])
    []
    """

    # Initialize an empty list to store the positive numbers
    positives = []

    # Iterate through each element in the input list
    for x in l:
        # Check if the element is strictly greater than zero
        # Note: 0 is not included; True counts as 1 (positive) by Python semantics.
        if x > 0:
            positives.append(x)

    # Return the list containing only positive numbers
    return positives
