def sum_to_n(n: int) -> int:
    """
    Calculates the sum of all positive integers from 1 up to n using Gauss's formula.

    This implementation uses the O(1) arithmetic series formula: n * (n + 1) / 2.

    Args:
        n: The upper bound integer. 

    Returns:
        The sum of integers from 1 to n. Returns 0 if n is less than 1.

    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    >>> sum_to_n(0)
    0
    """
    
    # --- Input Validation and Constraints (Plan Step 3) ---
    # The function is defined for summing positive integers (1 to n).
    # If n is less than 1 (0 or negative), the sum of the series is 
    # considered 0, representing the sum over an empty set of positive integers.
    if n < 1:
        return 0

    # --- Core Logic (Plan Steps 1, 2, 4) ---
    # Calculate the sum using the direct mathematical formula (O(1) complexity):
    # S = n * (n + 1) / 2
    
    # 1. Calculate the product n * (n + 1).
    # 2. Perform integer division (//) by 2. This is crucial because n * (n + 1) 
    #    is always an even number, and integer division guarantees the result 
    #    remains an integer, fulfilling the required return type.
    result = (n * (n + 1)) // 2

    # --- Return Value (Plan Step 5) ---
    return result
