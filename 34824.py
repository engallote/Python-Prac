import sys


N = int(sys.stdin.readline())

y, k = 1000, 1000
for i in range(N):
    s = sys.stdin.readline().rstrip()

    if s == "yonsei":
        y = i
    elif s == "korea":
        k = i

if y < k:
    print("Yonsei Won!")
else:
    print("Yonsei Lost...")