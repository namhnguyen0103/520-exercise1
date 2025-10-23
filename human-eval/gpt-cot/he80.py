def is_happy(s: str) -> bool:
    """
    A string is 'happy' if its length is at least 3 and
    every group of 3 consecutive characters are all distinct.

    Examples:
    >>> is_happy("a")
    False
    >>> is_happy("aa")
    False
    >>> is_happy("abcd")
    True
    >>> is_happy("aabb")
    False
    >>> is_happy("adb")
    True
    >>> is_happy("xyy")
    False
    """
    # Must have at least 3 characters to form a triple
    if len(s) < 3:
        return False

    # Check each consecutive triple for distinctness
    for i in range(len(s) - 2):
        a, b, c = s[i], s[i + 1], s[i + 2]
        if len({a, b, c}) != 3:
            return False

    return True
