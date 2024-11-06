import sys


N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(sys.stdin.readline().rstrip())

ans = 0
for i in range(N):
    if arr[i] == "Present!":
        continue
    if i + 1 < N and arr[i + 1] == "Present!":
        continue
    else:
        ans += 1
        print(arr[i])

if ans == 0:
    print("No Absences")