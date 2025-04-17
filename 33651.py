import sys


N = sys.stdin.readline().rstrip()
res = ""

if "U" not in N:
    res += "U"
if "A" not in N:
    res += "A"
if "P" not in N:
    res += "P"
if "C" not in N:
    res += "C"

print(res)