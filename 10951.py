import sys

for i in sys.stdin:
    a, b = map(int, i.rstrip().split())
    print(a + b)