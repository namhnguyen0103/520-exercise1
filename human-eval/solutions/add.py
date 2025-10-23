def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # ensure the range goes from smaller to larger
    start, end = min(a, b), max(a, b)

    # only digits 0–9 can be even digits, so clamp to [0, 9]
    evens = [x for x in range(max(0, start), min(9, end) + 1) if x % 2 == 0]
    return evens
