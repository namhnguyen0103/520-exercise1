def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    if not lst:
        return []

    # 1. Sort the list to easily access the current minimum and maximum.
    sorted_lst = sorted(lst)

    # 2. Initialize pointers for the smallest (left) and largest (right) remaining elements.
    left = 0
    right = len(sorted_lst) - 1
    result = []

    # 3. Iterate, alternating between the minimum and maximum remaining values.
    while left <= right:
        # Append the current minimum (smallest remaining element)
        result.append(sorted_lst[left])
        left += 1

        # Check if there's a maximum remaining element to append next.
        # This prevents an index error and handles lists of odd length correctly.
        if left <= right:
            # Append the current maximum (largest remaining element)
            result.append(sorted_lst[right])
            right -= 1

    return result