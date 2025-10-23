#!/usr/bin/env python3
"""
Central Street Antennas — Minimum Coins to Cover [1..m]

Plan recap (implemented below):
- Dynamic programming over covered prefixes: dp[i] = min cost to cover [1..i].
- For each i (1..m), consider finishing with any antenna (x, s) that also covers i
  after possibly increasing its scope. Let A = max(0, |i - x| - s) be the extra
  scope needed just to reach i. To stitch with the already covered prefix [1..p],
  the left end of the antenna's final coverage must be ≤ p+1, which requires
  extra scope ≥ x - (p+1) - s. So the extra scope required is max(A, x - (p+1) - s).
- Transition:
    dp[i] = min_{antenna (x,s)} min_{p in [0..i-1]} [ dp[p] + max(A, x-(p+1)-s) ].
- Split by whether x-(p+1)-s ≤ A or > A. With P0 = x - s - 1 - A:
    Case 1 (p ∈ [max(0,P0)..i-1]):  dp[p] + A  ⇒  A + min dp[p] over [max(0,P0)..i-1]
    Case 2 (p ∈ [0..min(i-1,P0-1)]): (x-1-s) + (dp[p]-p) ⇒ (x-1-s) + min(dp[p]-p) over [0..min(i-1,P0-1)]
- Data structures:
    • For Case 1: we need range-min over dp on [L..R] with R = i-1. We support this online via a segment tree.
    • For Case 2: we need prefix-min over (dp[p]-p). Maintain pref_min_dpp[p] = min_{0..p}(dp[q]-q).
- Complexity:
    O(n * m * log m) RMQ with small constants. With n ≤ 80 and m ≤ 1e5, this runs fast in PyPy/CPython with iterative segtree.
"""

import sys

# ---------- Fast I/O ----------
def readints():
    return map(int, sys.stdin.readline().split())

# ---------- Iterative Segment Tree for Range Min Query ----------
class SegTreeMin:
    """
    Supports:
      - point update: set position i to value v
      - range min query: min over [l, r] inclusive
    All in O(log N) time, N = number of leaves.
    """
    __slots__ = ("n", "size", "tree", "INF")

    def __init__(self, n, INF=10**18):
        self.n = n
        self.INF = INF
        size = 1
        while size < n:
            size <<= 1
        self.size = size
        self.tree = [INF] * (2 * size)

    def update(self, idx, value):
        i = idx + self.size
        self.tree[i] = value
        i >>= 1
        t = self.tree
        while i:
            # Recompute min from children
            left = i << 1
            t[i] = t[left] if t[left] <= t[left + 1] else t[left + 1]
            i >>= 1

    def query(self, l, r):
        if l > r:
            return self.INF
        l += self.size
        r += self.size
        res = self.INF
        t = self.tree
        while l <= r:
            if (l & 1) == 1:
                val = t[l]
                if val < res:
                    res = val
                l += 1
            if (r & 1) == 0:
                val = t[r]
                if val < res:
                    res = val
                r -= 1
            l >>= 1
            r >>= 1
        return res


def main():
    INF = 10**18

    # ----- Read input -----
    data = sys.stdin.read().strip().split()
    it = iter(data)
    try:
        n = int(next(it))
    except StopIteration:
        return
    m = int(next(it))

    antennas = []
    for _ in range(n):
        x = int(next(it))
        s = int(next(it))
        antennas.append((x, s))

    # ----- Initialize DP and helper structures -----
    # dp[i] = minimal cost to cover [1..i]; dp[0] = 0
    dp = [INF] * (m + 1)
    dp[0] = 0

    # pref_min_dpp[i] = min_{p in [0..i]} (dp[p] - p)  (for Case 2 prefix minima)
    pref_min_dpp = [INF] * (m + 1)
    pref_min_dpp[0] = dp[0]  # dp[0]-0 = 0

    # Segment tree for Case 1 range-min of dp over [L..R]
    seg = SegTreeMin(m + 1, INF=INF)
    seg.update(0, dp[0])

    # ----- Main DP loop -----
    # For i from 1..m, compute dp[i] via both cases for all antennas.
    for i in range(1, m + 1):
        best = INF
        R = i - 1
        # Prefix min helper for Case 2 on [0..R]
        pref_dpp_R = pref_min_dpp[R]

        # Evaluate contributions from each antenna
        # Local bindings for speed
        for x, s in antennas:
            # A = extra scope to reach point i
            dist = x - i
            if dist < 0:
                dist = -dist
            A = dist - s
            if A < 0:
                A = 0

            # P0 determines the split between the two regions
            P0 = x - s - 1 - A

            # ---- Case 1: p in [max(0,P0)..R] -> cost = A + min dp[p] over that range
            L1 = P0
            if L1 < 0:
                L1 = 0
            if L1 <= R:
                min_dp = seg.query(L1, R)
                cand1 = A + min_dp
                if cand1 < best:
                    best = cand1

            # ---- Case 2: p in [0..min(R,P0-1)] -> cost = (x-1-s) + min(dp[p]-p)
            R2 = P0 - 1
            if R2 > R:
                R2 = R
            if R2 >= 0:
                # min(dp[p]-p) over [0..R2] is just pref_min_dpp[R2]
                cand2 = (x - 1 - s) + (pref_min_dpp[R2] if R2 < R else pref_dpp_R)
                if cand2 < best:
                    best = cand2

        # Store dp[i]
        dp[i] = best

        # Update helpers with the new dp[i]
        dpp_i = best - i
        prev = pref_min_dpp[i - 1]
        pref_min_dpp[i] = dpp_i if dpp_i < prev else prev
        seg.update(i, best)

    # ----- Result -----
    print(dp[m])


if __name__ == "__main__":
    main()
