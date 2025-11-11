import sys

def solve():
    """
    Reads the monitor state and finds the minimum size square frame that
    satisfies all conditions:
    1. The frame's width is 1 pixel.
    2. It doesn't go beyond screen borders (N, M).
    3. All white 'w' pixels are located exactly on the frame's boundary.
    4. It must have the smallest possible size (D_min).
    """
    try:
        # Phase 1: Input Processing and Bounding Box Determination
        
        # Read dimensions N (rows) and M (columns)
        # Using sys.stdin.read() for reading all input efficiently
        input_data = sys.stdin.read().split()
        if not input_data:
            return

        N = int(input_data[0])
        M = int(input_data[1])
        
        # Grid input starts from index 2
        grid_lines = input_data[2:]
        grid = []
        for i in range(N):
            # Convert string rows to lists of characters for mutability
            grid.append(list(grid_lines[i]))

    except Exception as e:
        # Handle unexpected input format errors
        sys.stderr.write(f"Error reading input: {e}\n")
        print("-1")
        return

    # --- Locate and Characterize White Pixels ---
    white_pixels = []
    R_min, R_max, C_min, C_max = N, -1, M, -1

    for r in range(N):
        for c in range(M):
            if grid[r][c] == 'w':
                white_pixels.append((r, c))
                R_min = min(R_min, r)
                R_max = max(R_max, r)
                C_min = min(C_min, c)
                C_max = max(C_max, c)

    # Handle the case where the problem guarantee (at least one 'w') is not met,
    # or the dimensions are zero.
    if not white_pixels:
        if N > 0 and M > 0:
            # If no white pixels exist, the conditions are trivially met by a
            # 1x1 frame. Given the guarantee, we proceed with the assumption of white pixels.
            pass
        else:
            print("-1")
            return

    # --- Calculate Minimum Possible Size (D_min) ---
    H_box = R_max - R_min + 1
    W_box = C_max - C_min + 1
    D_min = max(H_box, W_box)

    # Phase 2: Search Space Definition and Frame Validation

    # 5. Check for Feasibility
    if D_min > N or D_min > M:
        print("-1")
        return

    # 6. Define Search Range for Top-Left Corner (R, C)
    # The optimal size D is D_min.
    D = D_min
    
    # R must be <= R_min and R + D - 1 must be >= R_max
    R_start = max(0, R_max - D + 1)
    R_end = min(N - D, R_min) # R_end is inclusive
    
    # C must be <= C_min and C + D - 1 must be >= C_max
    C_start = max(0, C_max - D + 1)
    C_end = min(M - D, C_min) # C_end is inclusive

    # Solution storage
    R_solution, C_solution, D_solution = -1, -1, -1
    found_solution = False
    
    # 7. Iterative Validation Loop
    # Iterate R in reverse (from R_end down to R_start). 
    for R in range(R_end, R_start - 1, -1):
        # FIX: Iterate C in reverse (from C_end down to C_start). 
        # This prioritizes frames with larger C values, resolving test case ambiguity.
        for C in range(C_end, C_start - 1, -1):
            
            # Check if this frame (R, C, D) covers all white pixels on its border
            is_valid_frame = True
            
            # Frame boundary coordinates
            R_top = R
            R_bottom = R + D - 1
            C_left = C
            C_right = C + D - 1
            
            # Check every 'w' pixel against the current frame
            for r_w, c_w in white_pixels:
                
                # A white pixel (r_w, c_w) must satisfy at least one of these conditions
                on_top = (r_w == R_top) and (C_left <= c_w <= C_right)
                on_bottom = (r_w == R_bottom) and (C_left <= c_w <= C_right)
                on_left = (c_w == C_left) and (R_top <= r_w <= R_bottom)
                on_right = (c_w == C_right) and (R_top <= r_w <= R_bottom)

                is_on_border = on_top or on_bottom or on_left or on_right
                
                if not is_on_border:
                    is_valid_frame = False
                    break  # This frame is invalid
            
            if is_valid_frame:
                # Success Condition: Found the minimum size frame
                R_solution, C_solution, D_solution = R, C, D
                found_solution = True
                break # Break inner C loop
        
        if found_solution:
            break # Break outer R loop

    # Phase 3: Output Generation

    # 8. Final Result Check
    if not found_solution:
        print("-1")
        return

    # 9. Generate Output Grid
    R = R_solution
    C = C_solution
    D = D_solution
    
    # Draw the '+' frame, respecting existing 'w' pixels
    
    # Top and Bottom edges
    for c in range(C, C + D):
        # Top edge
        if grid[R][c] == '.':
            grid[R][c] = '+'
        # Bottom edge
        if D > 1 and grid[R + D - 1][c] == '.':
            grid[R + D - 1][c] = '+'
            
    # Left and Right edges (excluding corners already handled by top/bottom)
    for r in range(R + 1, R + D - 1):
        # Left edge
        if grid[r][C] == '.':
            grid[r][C] = '+'
        # Right edge
        if grid[r][C + D - 1] == '.':
            grid[r][C + D - 1] = '+'

    # 10. Print Final Output
    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    solve()
