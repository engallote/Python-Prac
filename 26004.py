import sys


N = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

print(min(s.count('H'), s.count('I'), s.count('A'), s.count('R'), s.count('C')))