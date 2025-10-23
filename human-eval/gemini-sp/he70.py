def strange_sort_list(lst: list[int]) -> list[int]:
    '''
    Given a list of integers, return a new list in "strange" order.
    Strange sorting is achieved by starting with the minimum value, then 
    the maximum of the remaining integers, then the minimum, and so on.

    The original input list remains unchanged.

    Args:
        lst: The input list of integers.

    Returns:
        A new list of integers sorted in the strange min-max alternating order.
    '''
    
    # 1. Initialization and Input Handling

    # 1. Handle Edge Case: If the list is empty, return an empty list immediately.
    if not lst:
        return []

    # 2. Create Working Copy and Initial Sort: 
    # Sorting the list allows for O(1) retrieval of the current minimum (at index 0)
    # and the current maximum (at index -1) in each iteration.
    sorted_list = sorted(lst)

    # 3. Initialize Result List: This will store the output in the strange order.
    result = []

    # 4. Initialize Toggle Flag: 
    # True indicates the next element to pick is the minimum (pop from the start).
    # False indicates the next element to pick is the maximum (pop from the end).
    is_min_turn = True

    # 2. Core Alternating Selection Algorithm

    # 1. Iterative Loop: Continue until the working list is empty.
    while sorted_list:
        if is_min_turn:
            # 2. Minimum Selection Phase
            
            # Select and remove the minimum element (always at the start of the sorted list).
            # pop(0) has O(N) complexity but is necessary here for the min/max strategy.
            element = sorted_list.pop(0)
            
            # Append to the result list.
            result.append(element)
            
            # Toggle Flag: Prepare for the maximum selection phase.
            is_min_turn = False
        else:
            # 3. Maximum Selection Phase
            
            # Check for Remaining Element: This condition handles the case where the list
            # had an odd number of elements and the last element was already popped in 
            # the minimum phase. If this check is omitted, an IndexError might occur.
            if sorted_list:
                # Select and remove the maximum element (always at the end of the sorted list).
                # pop(-1) is an efficient O(1) operation.
                element = sorted_list.pop(-1)
                
                # Append to the result list.
                result.append(element)
            
            # Toggle Flag: Prepare for the minimum selection phase for the next iteration.
            is_min_turn = True

    # 3. Final Output

    # 1. Return: Return the final list in the strange sort order.
    return result

# --- Example Usage (Optional for testing) ---
# print(f"Test 1: [1, 2, 3, 4] -> {strange_sort_list([1, 2, 3, 4])}")
# # Expected: [1, 4, 2, 3]

# print(f"Test 2: [5, 5, 5, 5] -> {strange_sort_list([5, 5, 5, 5])}")
# # Expected: [5, 5, 5, 5]

# print(f"Test 3: [] -> {strange_sort_list([])}")
# # Expected: []

# print(f"Test 4: [10, 2, 8, 4, 6] -> {strange_sort_list([10, 2, 8, 4, 6])}")
# # Sorted: [2, 4, 6, 8, 10]
# # Expected: [2, 10, 4, 8, 6]
