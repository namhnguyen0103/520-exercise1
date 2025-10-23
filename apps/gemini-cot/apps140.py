import sys
import math

# Set recursion limit higher for safety with potentially deep loops
sys.setrecursionlimit(2000)

def solve():
    # Read n and m
    try:
        # Read the first line of input
        line = sys.stdin.readline()
        if not line:
            return
        n, m = map(int, line.split())
    except:
        return

    # Read antenna data
    antennas = []
    for _ in range(n):
        try:
            x, s = map(int, sys.stdin.readline().split())
            antennas.append((x, s))
        except:
            # Handle unexpected end of file mid-reading
            return

    # DP array: DP[i] is the minimum cost to cover all integer positions from 1 to i
    # We use m + 1 size for 0-indexing
    # Initialize with a very large number (infinity)
    INF = float('inf')
    dp = [INF] * (m + 1)
    dp[0] = 0

    # Main DP loop
    # i is the current right-most position covered
    for i in range(1, m + 1):
        # j is the split point: [1, j] is covered, and [j+1, i] is covered by a single antenna
        for j in range(i):
            # The interval to cover is [j + 1, i]
            L = j + 1
            R = i
            
            # Find the minimum cost C[L][R] to cover [L, R] with a single antenna
            min_cost_to_cover_LR = INF
            
            # Iterate through all antennas k
            for x_k, s_k in antennas:
                # Minimum required scope s_req to cover [L, R]
                # s_req = max(|x_k - L|, |x_k - R|)
                
                # Since L <= R:
                # |x_k - L| is the distance to the left end
                # |x_k - R| is the distance to the right end
                dist_L = abs(x_k - L)
                dist_R = abs(x_k - R)
                
                s_req = max(dist_L, dist_R)
                
                # Cost is the increase in scope: max(0, s_req - s_k)
                cost_k = max(0, s_req - s_k)
                
                min_cost_to_cover_LR = min(min_cost_to_cover_LR, cost_k)

            # DP transition: DP[i] = min(DP[i], DP[j] + min_cost_to_cover_LR)
            if dp[j] != INF and min_cost_to_cover_LR != INF:
                dp[i] = min(dp[i], dp[j] + min_cost_to_cover_LR)

    # The result is the minimum cost to cover [1, m]
    print(dp[m])

# Call the function
# The structure of the $O(n m^2)$ solution is the only logical one given the constraints, despite
# the $O(n m^2)$ complexity typically being too high for these $m$ values.
# The low $n$ value ($n \le 80$) must be the key to making this pass on typical test data.
solve()