import sys

T = int(sys.stdin.readline())

for _ in range(T):
    st = sys.stdin.readline().rstrip().upper()
    l, r = 0, len(st) - 1

    while l <= r:
        if 'A' <= st[l] <= 'C' and 'A' <= st[r] <= 'C':
            l += 1
            r -= 1
        elif 'D' <= st[l] <= 'F' and 'D' <= st[r] <= 'F':
            l += 1
            r -= 1
        elif 'G' <= st[l] <= 'I' and 'G' <= st[r] <= 'I':
            l += 1
            r -= 1
        elif 'J' <= st[l] <= 'L' and 'J' <= st[r] <= 'L':
            l += 1
            r -= 1
        elif 'M' <= st[l] <= 'O' and 'M' <= st[r] <= 'O':
            l += 1
            r -= 1
        elif 'P' <= st[l] <= 'S' and 'P' <= st[r] <= 'S':
            l += 1
            r -= 1
        elif 'T' <= st[l] <= 'V' and 'T' <= st[r] <= 'V':
            l += 1
            r -= 1
        elif 'W' <= st[l] <= 'Z' and 'W' <= st[r] <= 'Z':
            l += 1
            r -= 1
        else:
            break

    if l > r:
        print("YES")
    else:
        print("NO")
