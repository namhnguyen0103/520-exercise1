def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).
    """
    
    # 1. Initialize the list with the number of stones in the first level, which is n.
    pile = [n]
    
    # 2. Start the current stone count with the first level's count.
    current_stones = n
    
    # 3. Iterate n-1 times to generate the remaining levels.
    # The total number of levels is n, so we need n-1 more levels after the first one.
    for _ in range(n):
        # 4. In each iteration, the next level has 2 more stones than the previous.
        current_stones += 2
        
        # 5. Append the new stone count to the pile list.
        pile.append(current_stones)
        
    return pile

# Examples:
# print(make_a_pile(3))  # Expected: [3, 5, 7]
# print(make_a_pile(4))  # Expected: [4, 6, 8, 10]
# print(make_a_pile(1))  # Expected: [1]