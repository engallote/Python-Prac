import sys

lv, p = sys.stdin.readline().rstrip().split()

if p == 'miss':
    print(0)
elif p == 'bad':
    print(200 * int(lv))
elif p == 'cool':
    print(400 * int(lv))
elif p == 'great':
    print(600 * int(lv))
else:
    print(1000 * int(lv))