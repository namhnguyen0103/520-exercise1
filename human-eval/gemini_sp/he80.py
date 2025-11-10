def is_happy(s):
    """
    Checks if a string is "happy".
    A string is happy if its length is at least 3 and every 3 consecutive
    letters are distinct.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is happy, False otherwise.
    """
    # 1. Initial Constraint Validation (Length Check)
    # A string must have a length of at least 3 to be considered happy.
    string_length = len(s)
    if string_length < 3:
        # If the length is less than 3, it fails the primary condition.
        return False

    # 2. Iteration Setup (Sliding Window)
    # We iterate through the string using a sliding window of size 3.
    # The loop stops at the index i where the triplet (s[i], s[i+1], s[i+2])
    # is the last possible triplet in the string.
    # This range is from 0 up to (length - 3). In Python, range(len - 2)
    # covers indices 0 to len - 3.
    for i in range(string_length - 2):

        # 3. Consecutive Triplet Check
        # Extract the current 3 consecutive characters.
        c1, c2, c3 = s[i], s[i+1], s[i+2]

        # Use a set to efficiently check for distinctness. A set only stores
        # unique elements. If all three characters are distinct, the set size
        # will be 3.
        char_set = {c1, c2, c3}

        # 4. Failure Handling (Early Exit)
        # If the size of the set is less than 3, it means there is a duplicate
        # character within the triplet (e.g., 'aa', 'aba', 'xyy').
        if len(char_set) < 3:
            # We found a non-happy triplet, so the entire string is not happy.
            return False

    # 4. Success Handling (Default Return)
    # If the loop completes without finding any non-happy triplets, it means
    # every 3 consecutive letters were distinct.
    return True
