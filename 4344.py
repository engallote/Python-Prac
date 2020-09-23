import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    arr = sys.stdin.readline().rstrip().split()
    score = list(map(int, arr[1:]))
    avg = sum(score) / len(score)

    cnt = 0
    for j in score:
        if j > avg:
            cnt += 1
    cnt = cnt / len(score) * 100
    print(str("%.3f" % cnt) + "%")