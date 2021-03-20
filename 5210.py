import sys

T = int(sys.stdin.readline().rstrip())

for t in range(1, T + 1):
    N = int(sys.stdin.readline().rstrip())
    arr = []
    print("Data Set %d:" %(t))
    for _ in range(N):
        arr.append(sys.stdin.readline().rstrip())

    tmp = sys.stdin.readline().rstrip()
    for i in arr:
        idx = 0
        for j in range(len(i)):
            if i[j].lower() == tmp[idx].lower():
                idx += 1
            if idx == len(tmp):
                break
        if idx == len(tmp):
            print(i)