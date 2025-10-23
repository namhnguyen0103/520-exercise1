def get_positive(l: list):
    """Return only positive numbers in the list.

    This function iterates through the input list and filters out any number
    that is not strictly greater than zero. Zero and negative numbers are excluded.

    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    # Implementation Step 2, 3, 4, 5: Core Logic via List Comprehension
    # This technique iterates through the input list 'l' and efficiently constructs
    # a new list based on a filtering condition, adhering to the plan's strategy.

    # Iteration: for number in l
    # Filtering Condition: if number > 0 (strictly positive)
    # Expression: number (the element itself is included if the condition is met)
    positive_numbers = [number for number in l if number > 0]

    # Implementation Step 6: Return the result.
    # The new list contains only the elements that satisfied the positive constraint.
    return positive_numbers

# Example usage and verification
if __name__ == '__main__':
    # A small demonstration to ensure the function works as expected
    test_cases = [
        ([-1, 2, -4, 5, 6], "Example 1"),
        ([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], "Example 2"),
        ([-10, -5, -1, 0], "Only negatives and zero"),
        ([1, 5, 10], "All positives"),
        ([], "Empty list")
    ]

    print("--- Running get_positive tests ---")
    for input_list, label in test_cases:
        result = get_positive(input_list)
        print(f"Test: {label}")
        print(f"  Input: {input_list}")
        print(f"  Output: {result}")
        print("-" * 20)

    # Optional: Run doctests for formal verification of examples in the docstring
    import doctest
    doctest.testmod(verbose=False)
