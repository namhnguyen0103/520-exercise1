import sys

def main():
    data = sys.stdin.read().splitlines()
    n, m = map(int, data[0].split())
    grid = [list(row) for row in data[1:]]

    whites = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'w':
                whites.append((i, j))

    # Problem guarantees at least one white
    minr = min(i for i, _ in whites)
    maxr = max(i for i, _ in whites)
    minc = min(j for _, j in whites)
    maxc = max(j for _, j in whites)

    H = maxr - minr + 1
    Ww = maxc - minc + 1
    d = max(H, Ww)

    # The square must fit on the screen
    if d > n or d > m:
        print(-1)
        return

    # Helper to emit result once we have r0, c0, d
    def output_square(r0, c0):
        # Paint border with '+', preserving 'w'
        r1, c1 = r0 + d - 1, c0 + d - 1
        # Top and bottom rows
        for c in range(c0, c1 + 1):
            if grid[r0][c] == '.':
                grid[r0][c] = '+'
            if grid[r1][c] == '.':
                grid[r1][c] = '+'
        # Left and right columns
        for r in range(r0, r1 + 1):
            if grid[r][c0] == '.':
                grid[r][c0] = '+'
            if grid[r][c1] == '.':
                grid[r][c1] = '+'
        print('\n'.join(''.join(row) for row in grid))

    # Case 1: H >= Ww -> r0 is fixed to minr
    if H >= Ww:
        r0 = minr
        # Collect middle-row white columns and validate
        mid_cols = set()
        if H > 1:
            for r, c in whites:
                if minr < r < maxr:
                    if c != minc and c != maxc:
                        print(-1)
                        return
                    mid_cols.add(c)

        # Determine c0 based on mid_cols constraints
        # Allowed c0 range must cover [minc..maxc] and fit the screen
        c0_low = max(0, maxc - d + 1)
        c0_high = min(minc, m - d)
        if c0_low > c0_high:
            print(-1)
            return

        c0_candidates = []

        if mid_cols == {minc, maxc}:
            # edges must be exactly at minc and maxc -> requires H == Ww and c0 = minc
            if H != Ww:
                print(-1)
                return
            c0 = minc
            if not (c0_low <= c0 <= c0_high):
                print(-1)
                return
            c0_candidates = [c0]
        elif mid_cols == {minc}:
            c0 = minc
            if not (c0_low <= c0 <= c0_high):
                print(-1)
                return
            c0_candidates = [c0]
        elif mid_cols == {maxc}:
            c0 = maxc - d + 1
            if not (c0_low <= c0 <= c0_high):
                print(-1)
                return
            c0_candidates = [c0]
        else:
            # No middle-row whites: any c0 in range works; choose the leftmost
            c0_candidates = [c0_low]

        # Final sanity check: all whites lie on the border for chosen c0
        for c0 in c0_candidates:
            left, right = c0, c0 + d - 1
            ok = True
            for r, c in whites:
                on_border = (
                    (r == r0 or r == r0 + d - 1) and (left <= c <= right)
                ) or (
                    (c == left or c == right) and (r0 <= r <= r0 + d - 1)
                )
                if not on_border:
                    ok = False
                    break
            if ok:
                output_square(r0, c0)
                return

        print(-1)
        return

    # Case 2: Ww > H -> c0 is fixed to minc
    else:
        c0 = minc
        # Collect middle-column white rows and validate
        mid_rows = set()
        if Ww > 1:
            for r, c in whites:
                if minc < c < maxc:
                    if r != minr and r != maxr:
                        print(-1)
                        return
                    mid_rows.add(r)

        # Allowed r0 range must cover [minr..maxr] and fit the screen
        r0_low = max(0, maxr - d + 1)
        r0_high = min(minr, n - d)
        if r0_low > r0_high:
            print(-1)
            return

        r0_candidates = []

        if mid_rows == {minr, maxr}:
            if H != Ww:
                print(-1)
                return
            r0 = minr
            if not (r0_low <= r0 <= r0_high):
                print(-1)
                return
            r0_candidates = [r0]
        elif mid_rows == {minr}:
            r0 = minr
            if not (r0_low <= r0 <= r0_high):
                print(-1)
                return
            r0_candidates = [r0]
        elif mid_rows == {maxr}:
            r0 = maxr - d + 1
            if not (r0_low <= r0 <= r0_high):
                print(-1)
                return
            r0_candidates = [r0]
        else:
            # No middle-column whites: any r0 in range works; choose the topmost
            r0_candidates = [r0_low]

        for r0 in r0_candidates:
            top, bot = r0, r0 + d - 1
            ok = True
            for r, c in whites:
                on_border = (
                    (r == top or r == bot) and (c0 <= c <= c0 + d - 1)
                ) or (
                    (c == c0 or c == c0 + d - 1) and (top <= r <= bot)
                )
                if not on_border:
                    ok = False
                    break
            if ok:
                output_square(r0, c0)
                return

        print(-1)

if __name__ == "__main__":
    main()
