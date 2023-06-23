import sys

N = int(sys.stdin.readline())

while N > 0:
    s = sys.stdin.readline().rstrip()

    if s == '':
        continue
    arr = list(map(int, s))
    arr = sorted(arr)
    arr.reverse()
    a, b = 0, arr[-1]
    for i in range(len(arr) - 1):
        a *= 10
        a += arr[i]

    print(a + b)
    N -= 1