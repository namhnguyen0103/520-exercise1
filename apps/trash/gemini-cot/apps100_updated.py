import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    grid = [list(row) for row in data[1:]]

    whites = [(i, j)
              for i in range(n)
              for j in range(m)
              if grid[i][j] == 'w']
    # Problem guarantees at least one white
    minr = min(r for r, _ in whites)
    maxr = max(r for r, _ in whites)
    minc = min(c for _, c in whites)
    maxc = max(c for _, c in whites)

    H = maxr - minr + 1
    W = maxc - minc + 1
    d = max(H, W)

    # Must fit on screen
    if d > n or d > m:
        print(-1)
        return

    # The square must cover the bbox and fit the screen:
    r0_low = max(0, maxr - d + 1)
    r0_high = min(minr, n - d)
    c0_low = max(0, maxc - d + 1)
    c0_high = min(minc, m - d)
    if r0_low > r0_high or c0_low > c0_high:
        print(-1)
        return

    # Collect constraints from "middle" whites
    # Middle rows -> constrain c0; middle columns -> constrain r0.
    c0_candidates_set = None  # None means unconstrained so far
    r0_candidates_set = None

    for r, c in whites:
        # If white is on a middle row, it must lie on a vertical edge
        if minr < r < maxr:
            cand = {c, c - d + 1}
            # Filter to feasible c0 range now to keep the set small
            cand = {x for x in cand if c0_low <= x <= c0_high}
            if not cand:
                print(-1)
                return
            c0_candidates_set = cand if c0_candidates_set is None else (c0_candidates_set & cand)
            if not c0_candidates_set:
                print(-1)
                return

        # If white is on a middle column, it must lie on a horizontal edge
        if minc < c < maxc:
            cand = {r, r - d + 1}
            cand = {x for x in cand if r0_low <= x <= r0_high}
            if not cand:
                print(-1)
                return
            r0_candidates_set = cand if r0_candidates_set is None else (r0_candidates_set & cand)
            if not r0_candidates_set:
                print(-1)
                return

    # If no constraints gathered in a direction, try the extremal placements there.
    if r0_candidates_set is None:
        r0_candidates = [r0_low]
        if r0_high != r0_low:
            r0_candidates.append(r0_high)
    else:
        r0_candidates = sorted(r0_candidates_set)

    if c0_candidates_set is None:
        c0_candidates = [c0_low]
        if c0_high != c0_low:
            c0_candidates.append(c0_high)
    else:
        c0_candidates = sorted(c0_candidates_set)

    # Try candidate pairs (very few: ≤4)
    def valid(r0, c0):
        left, right = c0, c0 + d - 1
        top, bot = r0, r0 + d - 1
        # Quick coverage check (guaranteed by ranges, but keep for safety)
        if not (top <= minr and bot >= maxr and left <= minc and right >= maxc):
            return False
        for r, c in whites:
            on_border = (
                (top <= c <= right and (r == top or r == bot)) or
                (left <= r <= bot and (c == left or c == right))
            )  # (typo check would be wrong; correct below)
            # ↑ that line is intentionally wrong; fix:
        return True  # placeholder

    # Fix the valid() implementation (correctly check borders)
    def valid(r0, c0):
        left, right = c0, c0 + d - 1
        top, bot = r0, r0 + d - 1
        for r, c in whites:
            if not (
                ((r == top or r == bot) and left <= c <= right) or
                ((c == left or c == right) and top <= r <= bot)
            ):
                return False
        return True

    # Paint function
    def output_square(r0, c0):
        top, left = r0, c0
        bot, right = r0 + d - 1, c0 + d - 1
        # Top and bottom rows
        for c in range(left, right + 1):
            if grid[top][c] == '.':
                grid[top][c] = '+'
            if grid[bot][c] == '.':
                grid[bot][c] = '+'
        # Left and right columns
        for r in range(top, bot + 1):
            if grid[r][left] == '.':
                grid[r][left] = '+'
            if grid[r][right] == '.':
                grid[r][right] = '+'
        print('\n'.join(''.join(row) for row in grid))

    for r0 in r0_candidates:
        for c0 in c0_candidates:
            if valid(r0, c0):
                output_square(r0, c0)
                return

    print(-1)

if __name__ == "__main__":
    main()
