import sys


s = list(sys.stdin.readline().rstrip())

a, b = s.count('A'), s.count('B')
print(a, ":", b)