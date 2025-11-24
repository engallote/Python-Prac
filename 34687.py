import sys


N, M = map(int, sys.stdin.readline().split())

if M >= N * 81/100:
    print("yaho")
else:
    print("no")