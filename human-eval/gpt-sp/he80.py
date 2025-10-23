from typing import Iterable

def is_happy(s: str) -> bool:
    """
    Determine whether a string is "happy".

    A string is happy iff:
      1) Its length is at least 3, and
      2) For every contiguous triple of characters (s[i], s[i+1], s[i+2]),
         all three characters are pairwise distinct.

    The check is purely by character equality; it works for ASCII and Unicode.

    Examples
    --------
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
    >>> is_happy("abca")  # "abc" and "bca" are both triples of distinct chars
    True
    """
    # 1) Early exit for strings shorter than 3 characters.
    if len(s) < 3:
        return False

    # 2) Slide a window of size 3 across the string.
    #    For each window (a, b, c), ensure pairwise distinctness.
    #    We use direct comparisons for O(1) space and speed.
    #    Equivalent to: len({a, b, c}) == 3, but avoids set allocation.
    for i in range(len(s) - 2):
        a, b, c = s[i], s[i + 1], s[i + 2]
        if not (a != b and a != c and b != c):
            # Found a triple with a repeated character -> not happy.
            return False

    # 3) All triples were distinct -> happy string.
    return True


# Optional lightweight self-checks (not executed unless run as a script).
if __name__ == "__main__":
    tests: Iterable[tuple[str, bool]] = [
        ("", False),
        ("a", False),
        ("aa", False),
        ("adb", True),
        ("abc", True),
        ("abcd", True),
        ("aabb", False),
        ("xyy", False),
        ("xxy", False),
        ("xxx", False),
        ("abca", True),
        ("a😊b", True),  # Unicode works the same way
        ("a a", False),  # contains a space; still just chars
    ]
    for s, expected in tests:
        got = is_happy(s)
        assert got == expected, f"is_happy({s!r}) -> {got}, expected {expected}"
