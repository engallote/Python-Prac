import sys

N = int(sys.stdin.readline())
ju = sys.stdin.readline().rstrip()
juk = sys.stdin.readline().rstrip()
ia = sys.stdin.readline().rstrip()
iak = sys.stdin.readline().rstrip()

ans = ""
for i in range(N):
    if ju[i] == ia[i]:
        if juk[i] != iak[i]:
            ans = "htg!"
            break
        ans += juk[i]

print(ans)