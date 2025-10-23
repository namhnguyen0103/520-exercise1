import collections

def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest unique element of the list.
    Returns None if there is no such element (i.e., less than two unique elements).

    Args:
        lst (list[int]): The input list of integers.

    Returns:
        int | None: The second smallest unique element, or None if not found.
    """
    # Phase 1: Data Pre-processing and Deduplication
    # Convert the list to a set to efficiently eliminate all duplicate elements.
    unique_elements_set = set(lst)

    # Convert the set back to a list. This step is necessary as sets are unordered
    # and do not support indexing required for the sorting and selection phase.
    unique_elements = list(unique_elements_set)

    # Phase 2: Edge Case Validation
    # Check if there are at least two unique elements remaining.
    # If the length is 0 (empty list), 1 (e.g., [5]), or 1 (e.g., [1, 1, 1]),
    # there is no "second smallest unique" element.
    if len(unique_elements) < 2:
        return None

    # Phase 3: Sorting and Element Selection
    # Sort the list of unique elements in ascending order.
    # This places the smallest element at index 0 and the second smallest at index 1.
    unique_elements.sort()

    # Access the element at index 1, which represents the second smallest unique value.
    second_smallest = unique_elements[1]

    # Phase 4: Final Output
    return second_smallest

# --- Example Usage and Verification ---

# Example 1: Standard case
print(f"next_smallest([1, 2, 3, 4, 5]) -> {next_smallest([1, 2, 3, 4, 5])}")
# Expected: 2

# Example 2: Unsorted case with duplicates
print(f"next_smallest([5, 1, 4, 3, 2, 3, 4, 5]) -> {next_smallest([5, 1, 4, 3, 2, 3, 4, 5])}")
# Expected: 2 (Unique elements: [1, 2, 3, 4, 5])

# Example 3: Empty list (Edge Case)
print(f"next_smallest([]) -> {next_smallest([])}")
# Expected: None

# Example 4: List with only one unique element (Edge Case)
print(f"next_smallest([1, 1]) -> {next_smallest([1, 1])}")
# Expected: None

# Example 5: List with negative numbers
print(f"next_smallest([-5, -1, -4, -3, -2]) -> {next_smallest([-5, -1, -4, -3, -2])}")
# Expected: -4 (Unique and sorted: [-5, -4, -3, -2, -1]. Index 1 is -4)

# Example 6: Two unique elements
print(f"next_smallest([10, 20, 10]) -> {next_smallest([10, 20, 10])}")
# Expected: 20
