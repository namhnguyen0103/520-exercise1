# s = input()
# n = len(s)
# ind = -1
# f = False
# for i in range(n):
#     if s[i] == '[':
#         f = True
#     elif s[i] == ':':
#         if f:
#             ind = i
#             break
# bind = -1
# f = False
# for i in range(n-1,-1,-1):
#     if s[i] == ']':
#         f = True
#     elif s[i] == ':':
#         if f:
#             bind = i
#             break
# # print(ind,bind)
# if ind == -1 or bind == -1:
#     print(-1)
# elif ind >= bind:
#     print(-1)
# else:
#     ans = 4
#     for i in range(ind+1,bind):
#         if s[i] == '|':
#             ans += 1
#     print(ans)
import sys

def solve():
    s = sys.stdin.readline().rstrip('\n')

    n = len(s)

    # 1) leftmost '['
    L = s.find('[')
    if L == -1:
        print(-1); return

    # 2) first ':' after L
    C1 = s.find(':', L + 1)
    if C1 == -1:
        print(-1); return

    # 3) rightmost ']'
    R = s.rfind(']')
    if R == -1 or R <= C1:
        print(-1); return

    # 4) last ':' before R
    C2 = s.rfind(':', L + 1, R)
    if C2 == -1 or C2 <= C1:
        print(-1); return

    # 5) count '|' between the two colons
    pipes = s.count('|', C1 + 1, C2)

    # length = '[' + ':' + pipes*'|' + ':' + ']'
    print(4 + pipes)

if __name__ == "__main__":
    solve()
