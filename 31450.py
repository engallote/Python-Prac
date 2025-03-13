import sys


M, K = map(int, sys.stdin.readline().split())

if M % K == 0:
    print("Yes")
else:
    print("No")