import sys


N = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

print(s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u'))