import sys


while True:
    arr = sys.stdin.readline().rstrip()
    if arr == "#":
        break

    stamp = ['*', '?', '/', '+', '!']
    dic = dict()
    s = set()
    idx = 0

    for i in arr:
        if i in s:
            if i in dic:
                print(stamp[dic[i]], end='')
            else:
                dic[i] = idx
                print(stamp[idx], end='')
                idx += 1
        else:
            if i.isupper():
                s.add(i)
                s.add(i.lower())
            else:
                s.add(i)
                s.add(i.upper())
            print(i, end='')
    print()