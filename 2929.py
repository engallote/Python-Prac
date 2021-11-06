import sys


code = sys.stdin.readline().rstrip()
cnt, res = 0, 0

for i in range(0, len(code)):
    if 'A' <= code[i] <= 'Z':
        if (i + cnt) % 4 == 0:
            continue
        while (i + cnt) % 4 != 0:
            cnt += 1

print(cnt)