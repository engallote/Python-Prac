import sys
import math


N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    ans = ""

    if num % 2 != 0:
        ans += "O"

    if num ** 0.5 % 1 == 0:
        ans += "S"

    if ans == "":
        print("EMPTY")
    else:
        print(ans)