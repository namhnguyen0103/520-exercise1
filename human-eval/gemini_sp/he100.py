def make_a_pile(n):
    """
    Given a positive integer n, this function calculates the number of stones 
    in each of the n levels of a stone pile.

    The rules for the number of stones in each subsequent level are:
    1. The first level has n stones.
    2. Subsequent levels increase by 2 (next odd or next even number), 
       maintaining the parity of n.

    Args:
        n (int): The number of levels in the pile (must be a positive integer).

    Returns:
        list[int]: A list where each element is the number of stones in the 
                   corresponding level, from level 1 to level n.

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    >>> make_a_pile(4)
    [4, 6, 8, 10]
    """
    # 1. Function Definition and Initialization
    # Initialize an empty list to store the number of stones in each level.
    pile_stones = []

    # Check if n is a positive integer, although the prompt implies valid input.
    if n <= 0:
        # Returning an empty list for non-positive inputs
        return pile_stones

    # 2. Base Case and Iteration Setup
    # The first level (Level 1) always has 'n' stones.
    current_stones = n
    pile_stones.append(current_stones)

    # The rule is that the next level's stone count must maintain the parity 
    # of 'n' while being the next number of that parity. Since the difference 
    # between consecutive odd numbers is 2, and the difference between 
    # consecutive even numbers is also 2, the number of stones always increases 
    # by 2, regardless of n's initial parity.

    # 3. Iterative Calculation of Subsequent Levels
    # We need to calculate stones for the remaining n-1 levels (from level 2 to n).
    # The loop runs for i = 1, 2, ..., n-1 times.
    for i in range(1, n - 1):
        # Determine the number of stones for the next level.
        # Since the parity is already established by 'n', and we always need the 
        # *next* number of that same parity, we simply add 2 to the previous level's count.
        
        # Case 1: n is Odd (e.g., 3 -> 5 -> 7)
        # Case 2: n is Even (e.g., 4 -> 6 -> 8)
        # In both cases, the increment is +2.
        next_stones = current_stones + 2
        
        # Update the list with the calculated stone count.
        pile_stones.append(next_stones)
        
        # Update the working variable for the next iteration.
        current_stones = next_stones

    # 4. Return Value
    return pile_stones