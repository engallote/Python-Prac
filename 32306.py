import sys


o1, o2, o3 = map(int, sys.stdin.readline().split())
t1, t2, t3 = map(int, sys.stdin.readline().split())

if o1 + o2 * 2 + o3 * 3 > t1 + t2 * 2 + t3 * 3:
    print(1)
elif o1 + o2 * 2 + o3 * 3 == t1 + t2 * 2 + t3 * 3:
    print(0)
else:
    print(2)