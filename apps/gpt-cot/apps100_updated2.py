import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    grid = [list(row) for row in data[1:]]

    whites = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 'w']
    minr = min(r for r, _ in whites)
    maxr = max(r for r, _ in whites)
    minc = min(c for _, c in whites)
    maxc = max(c for _, c in whites)

    H = maxr - minr + 1
    W = maxc - minc + 1
    d = max(H, W)

    # Must fit
    if d > n or d > m:
        print(-1)
        return

    # Feasible ranges so the square covers the bbox and stays on screen
    r0_low = max(0, maxr - d + 1)
    r0_high = min(minr, n - d)
    c0_low = max(0, maxc - d + 1)
    c0_high = min(minc, m - d)
    if r0_low > r0_high or c0_low > c0_high:
        print(-1)
        return

    # Gather constraints from "middle" whites
    r0_set = None  # candidate set for r0 if constrained
    c0_set = None  # candidate set for c0 if constrained

    for r, c in whites:
        # Whites in middle rows force c to lie on a vertical edge
        if minr < r < maxr:
            cand = {c, c - d + 1}
            cand = {x for x in cand if c0_low <= x <= c0_high}
            if not cand:
                print(-1); return
            c0_set = cand if c0_set is None else (c0_set & cand)
            if not c0_set:
                print(-1); return

        # Whites in middle columns force r to lie on a horizontal edge
        if minc < c < maxc:
            cand = {r, r - d + 1}
            cand = {x for x in cand if r0_low <= x <= r0_high}
            if not cand:
                print(-1); return
            r0_set = cand if r0_set is None else (r0_set & cand)
            if not r0_set:
                print(-1); return

    # Tie-break when unconstrained: prefer whites on the TOP and LEFT edges
    def clamp(val, lo, hi): 
        return max(lo, min(val, hi))

    if r0_set is None:
        r0_candidates = [clamp(minr, r0_low, r0_high)]
    else:
        r0_candidates = sorted(r0_set)

    if c0_set is None:
        c0_candidates = [clamp(minc, c0_low, c0_high)]
    else:
        c0_candidates = sorted(c0_set)

    def valid(r0, c0):
        top, bot = r0, r0 + d - 1
        left, right = c0, c0 + d - 1
        for r, c in whites:
            if not (
                ((r == top or r == bot) and left <= c <= right) or
                ((c == left or c == right) and top <= r <= bot)
            ):
                return False
        return True

    def paint_and_print(r0, c0):
        top, bot = r0, r0 + d - 1
        left, right = c0, c0 + d - 1
        # Top & bottom edges
        for j in range(left, right + 1):
            if grid[top][j] == '.': grid[top][j] = '+'
            if grid[bot][j] == '.': grid[bot][j] = '+'
        # Left & right edges
        for i in range(top, bot + 1):
            if grid[i][left] == '.': grid[i][left] = '+'
            if grid[i][right] == '.': grid[i][right] = '+'
        print('\n'.join(''.join(row) for row in grid))

    # Try (very few) candidates; with our tie-break it's usually a single pair
    for r0 in r0_candidates:
        for c0 in c0_candidates:
            if valid(r0, c0):
                paint_and_print(r0, c0)
                return

    print(-1)

if __name__ == "__main__":
    main()
