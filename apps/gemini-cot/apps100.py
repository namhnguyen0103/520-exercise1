import sys

def solve():
    """
    Finds the smallest square frame (represented by '+') that encloses all 'w' pixels,
    such that all 'w' pixels lie exactly on the frame border.
    """
    
    # Read input N, M
    try:
        # Read the first line N, M
        line = sys.stdin.readline().split()
        if not line:
            return
        N, M = map(int, line)
    except Exception:
        # Handle potential read error
        return

    grid = []
    white_pixels = []
    
    # Read the grid and find all 'w' pixels
    for r in range(N):
        row = sys.stdin.readline().strip()
        if not row:
            # Handle unexpected EOF
            return
        grid.append(list(row))
        for c in range(M):
            if row[c] == 'w':
                white_pixels.append((r, c))

    # Problem guarantees at least one 'w' exists.
    if not white_pixels:
        # This path should not be reached based on problem constraints.
        print("-1") 
        return

    # 1. Find the bounding box of all 'w' pixels (R_min, R_max, C_min, C_max).
    R_min = N
    R_max = -1
    C_min = M
    C_max = -1

    for r, c in white_pixels:
        R_min = min(R_min, r)
        R_max = max(R_max, r)
        C_min = min(C_min, c)
        C_max = max(C_max, c)

    # 2. Determine the minimum size (D_min) required to enclose the bounding box.
    H = R_max - R_min + 1
    W = C_max - C_min + 1
    D = max(H, W) # D is the size of the square frame

    # 3. Check for immediate impossibility due to screen size.
    # If the required minimum size D is larger than the screen dimensions, it's impossible.
    if D > N or D > M:
        print("-1")
        return
    
    # 4. Determine the search ranges for the top-left corner (r, c).
    # The starting row 'r' must satisfy two conditions:
    # a) It must enclose the top edge (r <= R_min) and the bottom edge (r + D - 1 >= R_max).
    # b) It must stay within the screen bounds (r >= 0 and r + D - 1 < N, i.e., r <= N - D).
    r_low = max(0, R_max - D + 1)
    r_high = min(N - D, R_min)
    
    # Similarly for the starting column 'c'.
    c_low = max(0, C_max - D + 1)
    c_high = min(M - D, C_min)
    
    # 5. Search for a valid starting position (r, c)
    found_frame = False
    start_r, start_c = -1, -1

    # Check if a valid range for the top-left corner exists
    if r_low > r_high or c_low > c_high:
        print("-1")
        return

    # Iterate through all possible minimal starting positions
    for r in range(r_low, r_high + 1):
        for c in range(c_low, c_high + 1):
            is_valid_frame = True
            
            # Check Condition: All 'w' pixels must be ON the border of the square [r, r+D-1] x [c, c+D-1].
            r_end = r + D - 1
            c_end = c + D - 1
            
            for r_w, c_w in white_pixels:
                # A pixel (r_w, c_w) is on the border if its row or column matches one of the frame edges
                is_on_border = (r_w == r) or \
                               (r_w == r_end) or \
                               (c_w == c) or \
                               (c_w == c_end)
                               
                if not is_on_border:
                    is_valid_frame = False
                    break 
            
            if is_valid_frame:
                # Found the smallest possible valid frame
                start_r, start_c = r, c
                found_frame = True
                break
        if found_frame:
            break
            
    # 6. Output result
    if not found_frame:
        print("-1")
    else:
        # Mark the frame pixels '+' on the grid copy
        r = start_r
        c = start_c
        r_end = r + D - 1
        c_end = c + D - 1
        
        for i in range(r, r_end + 1):
            for j in range(c, c_end + 1):
                # Check if pixel (i, j) is on the border
                is_border = (i == r) or \
                            (i == r_end) or \
                            (j == c) or \
                            (j == c_end)
                
                # Only mark '+' if it's a border pixel and not already 'w'
                if is_border and grid[i][j] != 'w':
                    grid[i][j] = '+'

        # Print the final grid
        for row in grid:
            print("".join(row))

if __name__ == "__main__":
    solve()
