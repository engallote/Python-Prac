import sys


T = int(sys.stdin.readline())

for _ in range(T):
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()
    alp = [False for _ in range(200)]
    for i in s1:
        alp[ord(i)] = True

    ans = "YES"
    for i in s2:
        if not alp[ord(i)]:
            ans = "NO"
            break

    print(ans)