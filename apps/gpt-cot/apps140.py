import sys

def solve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    antennas = []
    for _ in range(n):
        x = int(next(it)); s = int(next(it))
        antennas.append((x, s))

    # Optional: sort by position (tidier iteration; not required for correctness)
    antennas.sort()

    INF = 10**18
    dp = [INF] * (m + 1)
    dp[0] = 0  # cost to cover nothing is 0

    # For each already-covered prefix [1..l], try to extend using any antenna.
    for l in range(m):
        cur = dp[l]
        if cur == INF:
            continue
        a = l + 1  # next point that must be covered

        for x, s in antennas:
            # Extra radius needed so that point a is inside [x - r', x + r']:
            # r' must be at least |x - a|
            add = 0
            d = abs(x - a) - s
            if d > 0:
                add = d

            # After paying 'add', the radius is r' = max(s, |x - a|),
            # so the right end becomes R = x + r'
            R = x + (s + add)
            if R > m:
                R = m

            if dp[R] > cur + add:
                dp[R] = cur + add

    print(dp[m])

if __name__ == "__main__":
    solve()
