import sys


s = sys.stdin.readline().rstrip()

if s[len(s) - 3:] == "eh?":
    print("Canadian!")
else:
    print("Imposter!")