#!/usr/bin/env python3
import sys

def build_prefix_sum(grid):
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
    if r1 > r2 or c1 > c2:
        return 0
    r1p, c1p, r2p, c2p = r1+1, c1+1, r2+1, c2+1
    return psum[r2p][c2p] - psum[r1p-1][c2p] - psum[r2p][c1p-1] + psum[r1p-1][c1p-1]

def find_min_frame(grid):
    n = len(grid)
    m = len(grid[0])

    psum, K, bbox = build_prefix_sum(grid)
    rmin, rmax, cmin, cmax = bbox

    # Spread and starting side length (must cover bbox)
    h = rmax - rmin
    w = cmax - cmin
    d_start = max(h, w) + 1
    d_limit = min(n, m)

    for d in range(d_start, d_limit + 1):
        # Feasible top-left ranges from containment + screen bounds
        r0_lo = max(0, rmax - d + 1)
        r0_hi = min(rmin, n - d)
        c0_lo = max(0, cmax - d + 1)
        c0_hi = min(cmin, m - d)

        if r0_lo > r0_hi or c0_lo > c0_hi:
            continue

        # Enumerate **descending** to prefer largest (r0, c0) -> bottom/right alignment
        for r0 in range(r0_hi, r0_lo - 1, -1):
            r1 = r0 + d - 1
            for c0 in range(c0_hi, c0_lo - 1, -1):
                c1 = c0 + d - 1

                # Count whites in closed square
                S = rect_sum(psum, r0, c0, r1, c1)
                if S != K:
                    continue

                # Count whites in interior
                if d <= 2:
                    I = 0
                else:
                    I = rect_sum(psum, r0+1, c0+1, r1-1, c1-1)

                if I != 0:
                    continue

                # Valid minimal frame found
                return (r0, c0, d)

    return None

def draw_and_print(grid, r0, c0, d):
    n = len(grid)
    m = len(grid[0])
    out = [list(row) for row in grid]
    r1 = r0 + d - 1
    c1 = c0 + d - 1

    # Top
    for c in range(c0, c1 + 1):
        if out[r0][c] != 'w':
            out[r0][c] = '+'
    # Bottom
    for c in range(c0, c1 + 1):
        if out[r1][c] != 'w':
            out[r1][c] = '+'
    # Left
    for r in range(r0, r1 + 1):
        if out[r][c0] != 'w':
            out[r][c0] = '+'
    # Right
    for r in range(r0, r1 + 1):
        if out[r][c1] != 'w':
            out[r][c1] = '+'

    for r in range(n):
        sys.stdout.write(''.join(out[r]) + '\n')

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    n, m = map(int, data[0].split())
    grid = data[1:1+n]
    assert len(grid) == n and all(len(row) == m for row in grid)

    res = find_min_frame(grid)
    if res is None:
        sys.stdout.write("-1\n")
    else:
        r0, c0, d = res
        draw_and_print(grid, r0, c0, d)

if __name__ == "__main__":
    main()
