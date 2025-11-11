import sys

def solve():
    """
    Calculates the minimum cost (coins) required to ensure all integer positions
    from 1 to M are covered by at least one antenna.

    This problem is solved using Dynamic Programming (DP). The complexity is O(N * M),
    where N is the number of antennas and M is the required coverage length.
    """
    # Read all input from stdin for faster processing
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # --- 1. Preprocessing and Input Reading ---
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    antennas = []
    idx = 2
    for _ in range(N):
        x_i = int(input_data[idx])
        s_i = int(input_data[idx+1])
        # Store antenna as (position, initial_scope)
        antennas.append((x_i, s_i))
        idx += 2
        
    # --- 2. Dynamic Programming Initialization ---
    
    # dp[i] represents the minimum total cost to cover the entire range [1, i].
    # Using a large number to represent infinity (cost is at most N*M, so 10^9 is safe)
    INF = 10**12
    dp = [INF] * (M + 1)
    
    # Base case: Cost to cover the empty range [1, 0] is 0.
    dp[0] = 0
    
    # --- 3. DP Transition ---
    
    # Iterate through every required position 'i' from 1 to M.
    for i in range(1, M + 1):
        
        # We find the best transition by considering every antenna 'k' 
        # as the one that provides the essential coverage for the current position 'i',
        # extending from a previous covered prefix [1, p_prev].
        
        for x_k, s_k in antennas:
            
            # The minimum final scope (s'_k) required for antenna k to cover position i
            s_prime_k = abs(x_k - i)
            
            # The cost (C_k(i)) to achieve this scope: max(0, increase_needed)
            cost_k_i = max(0, s_prime_k - s_k)
            
            # The leftmost position (p_left) covered by antenna k with scope s'_k:
            # p_left = x_k - s'_k = x_k - |x_k - i|
            p_left = x_k - s_prime_k
            
            # The previous fully-covered prefix index (p_prev) needed: [1, p_left - 1]
            # We take max(0, ...) to handle cases where p_left <= 1 (e.g., covering [1, i] from dp[0]).
            p_prev = max(0, p_left - 1)
            
            # Update dp[i] with the minimum cost found so far
            if dp[p_prev] != INF:
                current_total_cost = dp[p_prev] + cost_k_i
                dp[i] = min(dp[i], current_total_cost)

    # --- 4. Final Result ---
    
    # dp[M] is the minimum cost to cover the entire required range [1, M].
    result = dp[M]
    
    print(result)

if __name__ == "__main__":
    solve()
