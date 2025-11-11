import sys

# Set a high recursion limit for safety, though not strictly needed here
# sys.setrecursionlimit(2000)

def solve():
    # Fast input reading
    try:
        # Read n and m
        line = sys.stdin.readline().split()
        if not line:
            return
        n = int(line[0])
        m = int(line[1])
    except EOFError:
        return
    except Exception:
        return

    # Read antenna data
    antennas = []
    for _ in range(n):
        try:
            x, s = map(int, sys.stdin.readline().split())
            antennas.append((x, s))
        except EOFError:
            break
        except Exception:
            break

    # 1. Sort antennas by position x_i
    # The problem statement implies x_i values are distinct, making the sort stable.
    # We'll use 1-based indexing for the logic to match DP[i], but 0-based for the array.
    antennas.sort(key=lambda item: item[0])
    
    # Prepend a dummy antenna for the base case (k=0)
    # The logic requires k to be the index of a previous covering set.
    # Let DP[k] be the minimum cost for the max coverage R_k achieved by a subset of antennas up to k.
    # R_0 = 0 (max covered right position by an empty set)
    # DP[0] = 0 (cost for R_0)
    
    # DP[i] will store the minimum cost to achieve R_i (the max covered right position)
    # R[i] will store the max covered right position
    
    # We use (n+1) size arrays for 1-based logic (index 0 is the dummy case)
    # R[0] = 0, DP[0] = 0
    
    # Initialize DP and R arrays
    # A large number for initial cost (m is up to 100,000, so 10^9 is safe for infinity)
    INF = 10**18 
    
    # DP[i]: minimum cost to achieve R[i] (max covered right position)
    DP = [INF] * (n + 1)
    # R[i]: max covered right position by a subset of antennas {1, ..., i}
    R = [-1] * (n + 1)

    # Base case: empty set of antennas covers up to R=0 with cost 0
    R[0] = 0
    DP[0] = 0

    # 4. Loop i=1 to n
    for i in range(1, n + 1):
        x_i, s_i = antennas[i-1] # antennas is 0-indexed, so use i-1
        
        # 5. Loop k=0 to i-1
        for k in range(i):
            R_k = R[k]
            
            # Antenna i must cover R_k + 1
            # Required final scope s'_i,k
            # Required initial coverage left boundary: L_i = x_i - s'_i,k <= R_k + 1
            # x_i - s'_i,k <= R_k + 1  =>  s'_i,k >= x_i - R_k - 1
            
            # Since s'_i,k must be at least s_i
            required_scope = x_i - R_k - 1
            s_prime_i_k = max(s_i, required_scope)
            
            # Cost to achieve this scope
            C_i_k = s_prime_i_k - s_i
            
            # New right covered position R_new
            R_new = x_i + s_prime_i_k
            
            # New total cost C_new
            C_new = DP[k] + C_i_k
            
            # 6. Update DP[i] and R[i]
            if R_new > R[i]:
                R[i] = R_new
                DP[i] = C_new
            elif R_new == R[i]:
                DP[i] = min(DP[i], C_new)

    # 7. Find the final minimum cost
    min_cost = INF
    for i in range(1, n + 1):
        if R[i] >= m:
            min_cost = min(min_cost, DP[i])
            
    print(min_cost)

# Execute the solution function
solve()