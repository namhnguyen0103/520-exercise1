#!/usr/bin/env python3
"""
Solve the "broken monitor frame" problem.

Given an n×m screen where some pixels are white ('w') and others black ('.'),
we must overlay an axis-aligned square frame (border width = 1 pixel, side length d ≥ 1)
such that:

  1) The frame lies entirely within the screen.
  2) Every existing white pixel lies on the border of that square (none outside, none inside).
  3) Among all frames satisfying 1–2, choose one with the smallest side length d.
  4) Print the resulting screen: keep original 'w' as 'w'; draw frame pixels as '+'
     (but never overwrite a 'w' with '+'). All other pixels remain as they were.
  5) If no such frame exists, print -1.

We implement this by:
  - Computing the bounding box of all white pixels.
  - Using a 2D prefix sum over whites to allow O(1) queries of counts in rectangles.
  - Iterating side lengths d starting from the theoretical minimum d0 = max(height, width) + 1,
    and searching feasible top-left corners (r0, c0) derived from containment constraints.
  - For a candidate (r0, c0, d), quickly check:
       S == K  (all K whites lie within the closed square),
       I == 0  (no white is strictly inside; i.e., all whites are on the border).
    The check uses the prefix sums in O(1).
  - On the first valid candidate (ensuring minimality), draw and print the frame.
  - If none found up to d = min(n, m), print -1.

Time: O(n*m) to build prefix sums + fast pruning search across candidates.
Constraints: n, m ≤ 2000.

Author: (following the step-by-step plan)
"""
import sys

def build_prefix_sum(grid):
    """
    Build a (n+1) x (m+1) integer prefix sum array over indicator of 'w'.
    psum[r+1][c+1] = number of 'w' in submatrix [0..r][0..c], inclusive.

    Returns:
        psum: list of lists (n+1) x (m+1)
        K: total number of white pixels
        bbox: (rmin, rmax, cmin, cmax) bounding box of whites
    """
    n = len(grid)
    m = len(grid[0])
    psum = [[0]*(m+1) for _ in range(n+1)]
    K = 0
    rmin, rmax = n, -1
    cmin, cmax = m, -1

    for r in range(n):
        row_sum = 0
        for c in range(m):
            is_w = 1 if grid[r][c] == 'w' else 0
            row_sum += is_w
            psum[r+1][c+1] = psum[r][c+1] + row_sum
            if is_w:
                K += 1
                if r < rmin: rmin = r
                if r > rmax: rmax = r
                if c < cmin: cmin = c
                if c > cmax: cmax = c

    return psum, K, (rmin, rmax, cmin, cmax)

def rect_sum(psum, r1, c1, r2, c2):
    """
    Sum over rectangle [r1..r2] x [c1..c2], inclusive.
    Returns 0 if the rectangle is empty/invalid.
    psum uses 1-based indexing internally.
    """
    if r1 > r2 or c1 > c2:
        return 0
    # Clamp to non-negative; caller ensures within bounds normally.
    r1p, c1p, r2p, c2p = r1+1, c1+1, r2+1, c2+1
    return psum[r2p][c2p] - psum[r1p-1][c2p] - psum[r2p][c1p-1] + psum[r1p-1][c1p-1]

def find_min_frame(grid):
    """
    Core search routine.
    Returns:
        (r0, c0, d) for a valid minimal frame, or None if impossible.
    """
    n = len(grid)
    m = len(grid[0])

    psum, K, bbox = build_prefix_sum(grid)
    # At least one white is guaranteed by problem statement.
    rmin, rmax, cmin, cmax = bbox

    if K == 1:
        # Trivially, the 1x1 square at the only white pixel is valid and minimal.
        # We'll still confirm via general loop; this is kept for clarity.
        pass

    # The square must span the white bounding box in both dimensions.
    # The smallest possible side length:
    h = rmax - rmin  # vertical spread
    w = cmax - cmin  # horizontal spread
    d_start = max(h, w) + 1
    d_limit = min(n, m)

    for d in range(d_start, d_limit + 1):
        # For containment:
        # r0 ≤ rmin and r0 + d - 1 ≥ rmax  ⇒ r0 ∈ [rmax - d + 1, rmin]
        # c0 ≤ cmin and c0 + d - 1 ≥ cmax  ⇒ c0 ∈ [cmax - d + 1, cmin]
        # Also must fit in screen: r0 ∈ [0, n - d], c0 ∈ [0, m - d].
        r0_lo = max(0, rmax - d + 1)
        r0_hi = min(rmin, n - d)
        c0_lo = max(0, cmax - d + 1)
        c0_hi = min(cmin, m - d)

        if r0_lo > r0_hi or c0_lo > c0_hi:
            continue  # no placement possible for this d

        # Choose iteration order (micro-optimization): iterate the shorter range in the outer loop.
        r_count = r0_hi - r0_lo + 1
        c_count = c0_hi - c0_lo + 1

        if r_count <= c_count:
            r_range = range(r0_lo, r0_hi + 1)
            c_range = range(c0_lo, c0_hi + 1)
            outer_is_r = True
        else:
            r_range = range(r0_lo, r0_hi + 1)
            c_range = range(c0_lo, c0_hi + 1)
            outer_is_r = False  # we'll swap iteration manually below

        if outer_is_r:
            for r0 in r_range:
                r1 = r0 + d - 1
                # Precompute vertical coordinates for interior checks to avoid repetition
                ri1 = r0 + 1
                ri2 = r1 - 1
                for c0 in c_range:
                    c1 = c0 + d - 1
                    # Count whites in the closed square
                    S = rect_sum(psum, r0, c0, r1, c1)
                    if S != K:
                        continue
                    # Count whites in the interior (if any interior exists)
                    if d <= 2:
                        I = 0
                    else:
                        ci1 = c0 + 1
                        ci2 = c1 - 1
                        I = rect_sum(psum, ri1, ci1, ri2, ci2)
                    if I != 0:
                        continue
                    # Valid and minimal
                    return (r0, c0, d)
        else:
            # Iterate columns as the outer loop
            for c0 in c_range:
                c1 = c0 + d - 1
                ci1 = c0 + 1
                ci2 = c1 - 1
                for r0 in r_range:
                    r1 = r0 + d - 1
                    S = rect_sum(psum, r0, c0, r1, c1)
                    if S != K:
                        continue
                    if d <= 2:
                        I = 0
                    else:
                        ri1 = r0 + 1
                        ri2 = r1 - 1
                        I = rect_sum(psum, ri1, ci1, ri2, ci2)
                    if I != 0:
                        continue
                    return (r0, c0, d)

    return None  # no valid frame found

def draw_and_print(grid, r0, c0, d):
    """
    Produce and print the final screen with the frame overlaid.
    Keep 'w' as 'w'. Draw '+' on border cells that are not 'w'.
    """
    n = len(grid)
    m = len(grid[0])
    out = [list(row) for row in grid]
    r1 = r0 + d - 1
    c1 = c0 + d - 1

    # Top edge
    for c in range(c0, c1 + 1):
        if out[r0][c] != 'w':
            out[r0][c] = '+'
    # Bottom edge
    for c in range(c0, c1 + 1):
        if out[r1][c] != 'w':
            out[r1][c] = '+'
    # Left edge
    for r in range(r0, r1 + 1):
        if out[r][c0] != 'w':
            out[r][c0] = '+'
    # Right edge
    for r in range(r0, r1 + 1):
        if out[r][c1] != 'w':
            out[r][c1] = '+'

    # Print
    for r in range(n):
        sys.stdout.write(''.join(out[r]) + '\n')

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    n, m = map(int, data[0].split())
    grid = data[1:1+n]
    # Defensive: ensure all rows are length m
    assert len(grid) == n and all(len(row) == m for row in grid)

    res = find_min_frame(grid)
    if res is None:
        # No valid frame exists
        sys.stdout.write("-1\n")
    else:
        r0, c0, d = res
        draw_and_print(grid, r0, c0, d)

if __name__ == "__main__":
    main()
