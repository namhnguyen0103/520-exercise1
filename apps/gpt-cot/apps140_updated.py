import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    xs = []
    ss = []
    for _ in range(n):
        x = int(next(it))
        s = int(next(it))
        xs.append(x)
        ss.append(s)

    # covered[i] = True if position i (1-based) is already covered initially
    covered = [False] * (m + 1)
    for x, s in zip(xs, ss):
        L = max(1, x - s)
        R = min(m, x + s)
        if L <= R:
            # mark as covered
            covered[L:R+1] = [True] * (R - L + 1)

    INF = 10**18
    best = [INF] * (m + 1)
    best[0] = 0

    # Forward DP with relaxations
    for i in range(m):
        # If next point is already covered by original ranges, we can move for free
        if covered[i + 1]:
            if best[i] < best[i + 1]:
                best[i + 1] = best[i]
            # Also allow doing an expansion anyway (it might still be beneficial to jump farther),
            # so we do not `continue` here.

        # Try using each antenna to cover position i+1 by expanding its left reach if needed,
        # and jump to the rightmost point it then covers.
        need_pos = i + 1
        for x, s in zip(xs, ss):
            # Amount to expand so that left boundary <= need_pos
            add = x - s - need_pos
            if add < 0:
                add = 0
            # Right boundary after expansion
            r = x + s + add
            if r > m:
                r = m
            # Relax jump to r
            cand = best[i] + add
            if cand < best[r]:
                best[r] = cand

    print(best[m])

if __name__ == "__main__":
    solve()
