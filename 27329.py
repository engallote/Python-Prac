import sys


N = int(sys.stdin.readline()) * 2 - 1
S = sys.stdin.readline().rstrip()
s1, s2 = S[:len(S)//2], S[len(S)//2:]

if s1 == s2:
    print("Yes")
else:
    print("No")