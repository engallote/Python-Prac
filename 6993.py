import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    a, b = sys.stdin.readline().rstrip().split()
    num = int(b)
    arr = ['.' for _ in range(len(a))]
    idx, idx2 = num, num * 2 % len(a)
    while True:
        arr[idx2] = a[idx]
        idx += 1
        idx2 += 1
        idx %= len(a)
        idx2 %= len(a)
        if idx == num:
            break

    print("Shifting %s by %s positions gives us: %s" %(a, b, ''.join(arr)))