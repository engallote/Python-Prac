import sys


N = sys.stdin.readline().rstrip()
M = sys.stdin.readline().rstrip()

id1, id2 = N.index('|'), M.index('|')

if len(N) - id1 - 1 == id2 or len(N) - id1 - 1 == len(M) - id2 - 1 or len(M) - id2 - 1 == id1 or id1 == id2:
    print("Yes")
else:
    print("No")