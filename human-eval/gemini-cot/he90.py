def next_smallest(lst):
    """
    Given a list of integers, this function returns the 2nd smallest unique
    element of the list.
    Returns None if there are fewer than two unique elements.
    """
    # Step 1: Convert to a set to efficiently find all unique elements.
    unique_elements = set(lst)

    # Step 2: Convert the unique set back to a list and sort it in ascending order.
    # This places the smallest unique element at index 0, and the second smallest at index 1.
    unique_sorted = sorted(list(unique_elements))

    # Step 3: Check if there are at least two unique elements.
    # If the length is 0 (empty list) or 1 (e.g., [1] or [1, 1]), return None.
    if len(unique_sorted) < 2:
        return None
    else:
        # Step 4: The second smallest unique element is at index 1.
        return unique_sorted[1]

# Example usage and tests (as requested in the prompt)
# print(f"Test 1: [1, 2, 3, 4, 5] -> {next_smallest([1, 2, 3, 4, 5])}")
# print(f"Test 2: [5, 1, 4, 3, 2] -> {next_smallest([5, 1, 4, 3, 2])}")
# print(f"Test 3: [] -> {next_smallest([])}")
# print(f"Test 4: [1, 1] -> {next_smallest([1, 1])}")
# print(f"Test 5: [2, 1, 1, 3] -> {next_smallest([2, 1, 1, 3])}") # Should be 2
# print(f"Test 6: [100] -> {next_smallest([100])}") # Should be None
